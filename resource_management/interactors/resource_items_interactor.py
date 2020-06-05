from resource_management.interactors.storages.item_interface import \
    ItemInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from resource_management.interactors.storages.resource_interface import \
    ResourceInterface


class ResourceItemsInteractor:

    def __init__(self, item_storage: ItemInterface,
                 resource_storage: ResourceInterface,
                 presenter: PresenterInterface):
        self.item_storage = item_storage
        self.resource_storage = resource_storage
        self.presenter = presenter

    def get_items_for_resource(self,
            resource_id: int, offset: int, limit: int, user_id: int):

        if offset < 0:
            self.presenter.raise_exception_for_invalid_offset_length()
            return

        if limit < 0:
            self.presenter.raise_exception_for_invalid_limit_length()
            return

        is_user_not_admin = \
            not self.resource_storage.check_is_user_admin(user_id=user_id)
        if is_user_not_admin:
            self.presenter.raise_exception_for_unauthorized_user()
            return

        is_resource_not_exists = \
            not self.resource_storage.check_is_resource_exists(resource_id)
        if is_resource_not_exists:
            self.presenter.raise_exception_for_resource_not_found()
            return
        
        items_details_dto = \
            self.item_storage.get_items_for_resource(
                resource_id=resource_id, offset=offset, limit=limit
            )

        return self.presenter.get_response_for_get_items_for_resource(
            items_with_count_dto=items_details_dto    
        )
