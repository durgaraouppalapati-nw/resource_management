from resource_management.interactors.storages.user_interface import \
    UserInterface
from resource_management.interactors.storages.item_interface import \
    ItemInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface


class UsersForItemInteractor:

    def __init__(self, user_storage: UserInterface,
                 item_storage: ItemInterface,
                 presenter: PresenterInterface):
        self.user_storage = user_storage
        self.item_storage = item_storage
        self.presenter = presenter

    def get_users_for_item(self,
            item_id: int, offset: int, limit: int, user_id: int):

        if offset < 0:
            self.presenter.raise_exception_for_invalid_offset_length()
            return

        if limit < 0:
            self.presenter.raise_exception_for_invalid_limit_length()
            return
        
        is_user_not_admin = \
            not self.user_storage.check_is_user_admin(user_id=user_id)
        if is_user_not_admin:
            self.presenter.raise_exception_for_unauthorized_user()
            return

        is_resource_item_not_exists = \
            not self.item_storage.check_is_resource_item_exists(item_id)
        if is_resource_item_not_exists:
            self.presenter.raise_exception_for_resource_item_not_found()
            
        users_with_count_dto = \
            self.user_storage.get_users_for_item(
                item_id=item_id, offset=offset, limit=limit    
            )

        return self.presenter.get_response_for_get_users_for_item(
            users_with_count_dto=users_with_count_dto    
        )
