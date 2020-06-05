from unittest.mock import create_autospec

from resource_management.interactors.update_profile_interactor import \
    UpdateProfileInteractor
from resource_management.interactors.storages.user_interface import \
    UserInterface


def test_update_profile_interactor(user_details_dto):
    # Arrange
    user_id = 1
    user_storage = create_autospec(UserInterface)
    interactor = UpdateProfileInteractor(user_storage=user_storage)

    # Act
    interactor.update_profile(
        user_id=user_id, user_details_dto=user_details_dto
    )

    # Assert
    user_storage.update_profile.assert_called_once_with(
        user_id=user_id, user_details_dto=user_details_dto    
    )
