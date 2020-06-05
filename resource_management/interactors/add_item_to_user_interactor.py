from resource_management.interactors.storages.user_interface import \
    UserInterface
from resource_management.interactors.storages.item_interface import \
    ItemInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface


class AddResourceItemToUserInteractor:

    def __init__(self, user_storage: UserInterface,
                 item_storage: ItemInterface,
                 presenter: PresenterInterface
                ):
        self.user_storage = user_storage
        self.item_storage = item_storage
        self.presenter = presenter

    def add_resource_item_to_user(self, user_id: int,
            item_id: int, access_level: str,
            requested_user_id: int):

        is_requested_user_not_admin = \
            not self.user_storage.check_is_user_admin(
                user_id=requested_user_id
            )
        if is_requested_user_not_admin:
            self.presenter.raise_exception_for_unauthorized_user()
            return

        is_user_not_exists = \
            not self.user_storage.check_is_user_exists(user_id=user_id)
        if is_user_not_exists:
            self.presenter.raise_exception_for_invalid_user()
            return

        is_resource_item_not_exists = \
            not self.item_storage.check_is_resource_item_exists(item_id=item_id)
        if is_resource_item_not_exists:
            self.presenter.raise_exception_for_resource_item_not_found()
            return

        self.item_storage.add_resource_item_to_user(
            item_id=item_id, user_id=user_id, access_level=access_level
        )
        return
