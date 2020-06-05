import pytest
from unittest.mock import create_autospec

from django_swagger_utils.drf_server.exceptions import ExpectationFailed

from resource_management.interactors.update_password_interactor import \
    UpdatePasswordInteractor
from resource_management.interactors.storages.user_interface import \
    UserInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface


def test_update_password_with_differnt_passwords_raise_exception():
    # Arrange
    user_id = 1
    old_password = "Durga@123"
    new_password = "Durga@123"
    confirm_password = "Durga@12"

    user_storage = create_autospec(UserInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = UpdatePasswordInteractor(
        user_storage=user_storage,
        presenter=presenter
    )
    presenter.raise_password_mismatch_exception.side_effect = ExpectationFailed

    # Act
    with pytest.raises(ExpectationFailed):
        interactor.update_password(
            user_id=user_id, old_password=old_password,
            new_password=new_password, confirm_password=confirm_password
        )

    # Assert
    presenter.raise_password_mismatch_exception.assert_called_once()


def test_update_password_with_different_old_password_raise_exception():
    # Arrange
    user_id = 1
    old_password = "Durga"
    new_password = "Durga@123"
    confirm_password = "Durga@123"

    user_storage = create_autospec(UserInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = UpdatePasswordInteractor(
        user_storage=user_storage,
        presenter=presenter
    )
    user_storage.check_is_password_valid.return_value = False
    presenter.raise_exception_for_invalid_password.side_effect = \
        ExpectationFailed

    # Act
    with pytest.raises(ExpectationFailed):
        interactor.update_password(
            user_id=user_id, old_password=old_password,
            new_password=new_password, confirm_password=confirm_password
        )

    # Assert
    user_storage.check_is_password_valid.assert_called_once_with(
        user_id=user_id, password=old_password    
    )
    presenter.raise_exception_for_invalid_password.assert_called_once()


def test_update_password_with_valid_details_updates_password():
    # Arrange
    user_id = 1
    old_password = "Durga"
    new_password = "Durga@123"
    confirm_password = "Durga@123"

    user_storage = create_autospec(UserInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = UpdatePasswordInteractor(
        user_storage=user_storage,
        presenter=presenter
    )
    user_storage.check_is_password_valid.return_value = True

    # Act
    interactor.update_password(
        user_id=user_id, old_password=old_password,
        new_password=new_password, confirm_password=confirm_password
    )

    # Assert
    user_storage.check_is_password_valid.assert_called_once_with(
        user_id=user_id, password=old_password    
    )
    user_storage.update_password.assert_called_once_with(
        user_id=user_id, new_password=new_password    
    )
