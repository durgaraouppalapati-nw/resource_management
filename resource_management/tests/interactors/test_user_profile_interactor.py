from unittest.mock import create_autospec

from resource_management.interactors.storages.dtos import UserDetailsDto
from resource_management.interactors.storages.user_interface import \
    UserInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from resource_management.interactors.user_profile_interactor import \
    UserProfileInteractor


def test_user_profile_interactor_with_user_id_return_user_details(
        user_details_dto):
    # Arrange
    user_id = 1
    user_storage = create_autospec(UserInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = UserProfileInteractor(
        user_storage=user_storage, presenter=presenter    
    )
    user_dto = user_details_dto
    user_storage.get_user_details.return_value = user_dto

    # Act
    interactor.get_user_details(user_id=user_id)

    # Assert
    user_storage.get_user_details.assert_called_once_with(user_id=user_id)
    presenter.get_user_details_response.assert_called_once_with(
        user_dto=user_dto
    )
