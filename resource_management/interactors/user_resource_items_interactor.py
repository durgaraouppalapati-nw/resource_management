from resource_management.interactors.storages.item_interface import \
    ItemInterface
from resource_management.interactors.storages.user_interface import \
    UserInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface


class UserResourceItemsInteractor:

    def __init__(self, item_storage: ItemInterface,
                 user_storage: UserInterface,
                 presenter: PresenterInterface):
        self.item_storage = item_storage
        self.user_storage = user_storage
        self.presenter = presenter

    def get_resource_items_for_user(self, user_id: int,
            offset: int, limit: int, search: str):

        if offset < 0:
            self.presenter.raise_exception_for_invalid_offset_length()
            return

        if limit < 0:
            self.presenter.raise_exception_for_invalid_limit_length()
            return

        is_user_not_exists = \
            not self.user_storage.check_is_user_exists(user_id=user_id)
        if is_user_not_exists:
            self.presenter.raise_exception_for_invalid_user()
            return

        user_resource_items_dto = \
            self.item_storage.get_user_resource_items(
                user_id, offset, limit, search
            )

        return self.presenter.get_response_for_user_resource_items(
            user_resource_items_dto=user_resource_items_dto    
        )
