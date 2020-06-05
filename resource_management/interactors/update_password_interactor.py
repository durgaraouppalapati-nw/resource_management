from resource_management.interactors.storages.user_interface import \
    UserInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface


class UpdatePasswordInteractor:

    def __init__(self, user_storage: UserInterface,
                 presenter: PresenterInterface):
        self.user_storage = user_storage
        self.presenter = presenter

    def update_password(self, user_id: int, old_password: str,
            new_password: str, confirm_password: str):
        is_new_password_and_confirm_password_not_same = \
            not new_password == confirm_password
        if is_new_password_and_confirm_password_not_same:
            self.presenter.raise_password_mismatch_exception()
            return

        is_old_password_not_valid = \
            not self.user_storage.check_is_password_valid(
                user_id=user_id, password=old_password
            )
        if is_old_password_not_valid:
            self.presenter.raise_exception_for_invalid_password()
            return

        self.user_storage.update_password(
            user_id=user_id, new_password=new_password    
        )
        return
