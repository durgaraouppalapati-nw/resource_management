from resource_management.interactors.storages.item_interface import \
    ItemInterface
from resource_management.interactors.storages.user_interface import \
    UserInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface


class UpdateResourceItemInteractor:

    def __init__(self, item_storage: ItemInterface,
                 user_storage: UserInterface,
                 presenter: PresenterInterface):
        self.user_storage = user_storage
        self.item_storage = item_storage
        self.presenter = presenter
    
    def update_resource_item(self, user_id: int, item_id: int,
            title: str, link: str, description: str):
        is_user_not_admin = \
            not self.user_storage.check_is_user_admin(user_id=user_id)
        if is_user_not_admin:
            self.presenter.raise_exception_for_unauthorized_user()
            return

        is_resource_item_not_exists = \
            not self.item_storage.check_is_resource_item_exists(item_id=item_id)
        if is_resource_item_not_exists:
            self.presenter.raise_exception_for_resource_item_not_found()
            return

        self.item_storage.update_resource_item(
            item_id=item_id, title=title, link=link, description=description
        )
        return
