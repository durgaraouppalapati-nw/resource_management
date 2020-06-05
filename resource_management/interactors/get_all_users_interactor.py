from resource_management.interactors.storages.user_interface import \
    UserInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface


class GetAllUsersInteractor:

    def __init__(self, user_storage: UserInterface,
                 presenter: PresenterInterface):
        self.user_storage = user_storage
        self.presenter = presenter

    def get_all_users(self, offset: int, limit: int, user_id: int):
        
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

        users_dto = self.user_storage.get_all_users(
            offset=offset, limit=limit    
        )
        return self.presenter.get_response_for_get_all_users(
            users_dto=users_dto
        )
