from resource_management.interactors.storages.user_interface import \
    UserInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface


class SignUpInteractor:

    def __init__(self, user_storage=UserInterface,
                 presenter=PresenterInterface):
        self.user_storage = user_storage
        self.presenter = presenter

    def create_user(self, username: str,
                    password: str, confirm_password: str):

        is_password_and_confirm_password_not_same = \
            not password == confirm_password
        if is_password_and_confirm_password_not_same:
            self.presenter.raise_password_mismatch_exception()
            return

        is_username_already_exists = \
            self.user_storage.check_is_username_already_exists(username)
        if is_username_already_exists:
            self.presenter.raise_username_already_exists_exception()
            return

        self.user_storage.create_user(username=username, password=password)
        return
