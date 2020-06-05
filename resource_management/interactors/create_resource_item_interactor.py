from resource_management.interactors.storages.item_interface import \
    ItemInterface
from resource_management.interactors.storages.resource_interface import \
    ResourceInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface


class CreateResourceItemInteractor:

    def __init__(self, item_storage: ItemInterface,
                 resource_storage: ResourceInterface,
                 presenter: PresenterInterface):
        self.item_storage = item_storage
        self.resource_storage = resource_storage
        self.presenter = presenter
    
    def create_resource_item(self, resource_id: int, user_id: int,
            title: str, link: str, description: str):
        is_resource_not_exists = \
            not self.resource_storage.check_is_resource_exists(
                resource_id=resource_id
            )
        if is_resource_not_exists:
            self.presenter.raise_exception_for_resource_not_found()
            return
    
        is_user_not_admin = \
            not self.resource_storage.check_is_user_admin(user_id=user_id)
        if is_user_not_admin:
            self.presenter.raise_exception_for_unauthorized_user()
            return


        self.item_storage.create_resource_item(
            resource_id=resource_id, title=title,
            link=link, description=description
        )
        return
