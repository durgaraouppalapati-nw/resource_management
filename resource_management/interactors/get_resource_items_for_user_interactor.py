from resource_management.interactors.storages.item_interface import \
    ItemInterface
from resource_management.interactors.storages.user_interface import \
    UserInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface


class GetAllResourceItemsForUserInteractor:

    def __init__(self, item_storage: ItemInterface,
                 user_storage: UserInterface,
                 presenter: PresenterInterface):
        self.item_storage = item_storage
        self.user_storage = user_storage
        self.presenter = presenter

    def get_all_resource_items_for_user(self, user_id: int,
            offset: int, limit: int, requested_user_id: int):

        if offset < 0:
            self.presenter.raise_exception_for_invalid_offset_length()
            return

        if limit < 0:
            self.presenter.raise_exception_for_invalid_limit_length()
            return

        is_requested_user_not_admin = \
            not self.user_storage.check_is_user_admin(user_id=requested_user_id)
        if is_requested_user_not_admin:
            self.presenter.raise_exception_for_unauthorized_user()
            return

        is_user_not_exists = \
            not self.user_storage.check_is_user_exists(user_id=user_id)
        if is_user_not_exists:
            self.presenter.raise_exception_for_invalid_user()
            return

        user_with_resource_items_dto = \
            self.item_storage.get_all_resource_items_for_user(
                user_id=user_id, offset=offset, limit=limit
            )

        return self.presenter.get_response_for_get_all_resource_items_for_user(
            user_with_resource_items_dto=user_with_resource_items_dto    
        )
