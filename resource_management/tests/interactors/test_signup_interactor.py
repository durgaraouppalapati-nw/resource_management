import pytest

from unittest.mock import create_autospec
from django_swagger_utils.drf_server.exceptions import \
    NotFound, ExpectationFailed

from resource_management.interactors.signup_interactor import \
    SignUpInteractor
from resource_management.interactors.storages.user_interface import \
    UserInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface


def test_signup_interactor_with_different_passwords_raise_exception():
    # Arrange
    username = "durgarao"
    password = "Durga@123"
    confirm_password = "Durga@1234"
    user_storage = create_autospec(UserInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = SignUpInteractor(
        user_storage=user_storage, presenter=presenter    
    )
    presenter.raise_password_mismatch_exception.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.create_user(
            username=username,
            password=password,
            confirm_password=confirm_password
        )

    # Assert
    presenter.raise_password_mismatch_exception.assert_called_once()



def test_signup_interactor_with_username_already_exists_raise_exception():
    # Arrange
    username = "durgarao"
    password = "Durga@123"
    confirm_password = "Durga@123"
    user_storage = create_autospec(UserInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = SignUpInteractor(
        user_storage=user_storage, presenter=presenter    
    )
    user_storage.check_is_username_already_exists.return_value = True
    presenter.raise_username_already_exists_exception.side_effect = \
        ExpectationFailed

    # Act
    with pytest.raises(ExpectationFailed):
        interactor.create_user(
            username=username,
            password=password,
            confirm_password=confirm_password
        )

    # Assert
    user_storage.check_is_username_already_exists.assert_called_once_with(
        username=username    
    )
    presenter.raise_username_already_exists_exception.assert_called_once()


def test_signup_interactor_with_valid_details_create_user():
    # Arrange
    username = "durgarao"
    password = "Durga@123"
    confirm_password = "Durga@123"
    user_storage = create_autospec(UserInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = SignUpInteractor(
        user_storage=user_storage, presenter=presenter    
    )
    user_storage.check_is_username_already_exists.return_value = False

    # Act
    interactor.create_user(
        username=username,
        password=password,
        confirm_password=confirm_password
    )

    # Assert
    user_storage.check_is_username_already_exists.assert_called_once_with(
        username=username    
    )
    user_storage.create_user.assert_called_once_with(
        username=username, password=password    
    )
