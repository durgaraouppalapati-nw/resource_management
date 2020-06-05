from typing import List

from resource_management.interactors.storages.item_interface import \
    ItemInterface
from resource_management.interactors.storages.user_interface import \
    UserInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface


class DeleteResourceItemsInteractor:

    def __init__(self, item_storage: ItemInterface,
                 user_storage: UserInterface,
                 presenter: PresenterInterface):
        self.user_storage = user_storage
        self.item_storage = item_storage
        self.presenter = presenter
    
    def delete_resource_items(self, user_id: int, item_ids: List[int]):
        is_user_not_admin = \
            not self.user_storage.check_is_user_admin(user_id=user_id)
        if is_user_not_admin:
            self.presenter.raise_exception_for_unauthorized_user()
            return

        self.item_storage.delete_resource_items(item_ids=item_ids)
        return
