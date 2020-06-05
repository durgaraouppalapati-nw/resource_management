from resource_management.interactors.storages.user_interface import \
    UserInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface


class UserProfileInteractor:

    def __init__(self, user_storage: UserInterface,
                 presenter: PresenterInterface):
        self.user_storage = user_storage
        self.presenter = presenter

    def get_user_details(self, user_id: int):
        user_dto = self.user_storage.get_user_details(user_id=user_id)
        return self.presenter.get_user_details_response(user_dto=user_dto)
