import pytest
from unittest.mock import create_autospec

from django_swagger_utils.drf_server.exceptions import BadRequest

from resource_management.interactors.storages.user_interface import \
    UserInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from resource_management.interactors.get_all_users_interactor import \
    GetAllUsersInteractor


def test_get_all_users_interactor_with_users_return_users_details(
        users_dto, list_of_users_response):
    # Arrange
    offset = 0
    limit = 10
    user_id = 1

    user_storage = create_autospec(UserInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetAllUsersInteractor(
        user_storage=user_storage,
        presenter=presenter
    )
    user_storage.check_is_user_admin.return_value = True
    user_storage.get_all_users.return_value = users_dto

    # Act
    interactor.get_all_users(offset=offset, limit=limit, user_id=user_id)

    # Assert
    user_storage.check_is_user_admin.assert_called_once_with(user_id=user_id)
    user_storage.get_all_users.assert_called_once()
    presenter.get_response_for_get_all_users.assert_called_once_with(
        users_dto=users_dto    
    )


def test_get_all_users_interactor_with_invalid_offset_raise_exception():
    # Arrange
    offset = -1
    limit = 10
    user_id = 1

    user_storage = create_autospec(UserInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetAllUsersInteractor(
        user_storage=user_storage,
        presenter=presenter
    )
    presenter.raise_exception_for_invalid_offset_length.side_effect = \
        BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.get_all_users(offset=offset, limit=limit, user_id=user_id)

    # Assert
    presenter.raise_exception_for_invalid_offset_length.assert_called_once()


def test_get_all_users_interactor_with_invalid_limit_raise_exception():
    # Arrange
    offset = 0
    limit = -1
    user_id = 1

    user_storage = create_autospec(UserInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetAllUsersInteractor(
        user_storage=user_storage,
        presenter=presenter
    )
    presenter.raise_exception_for_invalid_limit_length.side_effect = \
        BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.get_all_users(offset=offset, limit=limit, user_id=user_id)

    # Assert
    presenter.raise_exception_for_invalid_limit_length.assert_called_once()


def test_get_all_users_interactor_with_user_raise_exception():
    # Arrange
    offset = 0
    limit = 10
    user_id = 1

    user_storage = create_autospec(UserInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetAllUsersInteractor(
        user_storage=user_storage,
        presenter=presenter
    )
    user_storage.check_is_user_admin.return_value = False
    presenter.raise_exception_for_unauthorized_user.side_effect = \
        BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.get_all_users(offset=offset, limit=limit, user_id=user_id)

    # Assert
    user_storage.check_is_user_admin.assert_called_once_with(user_id=user_id)
    presenter.raise_exception_for_unauthorized_user.assert_called_once()
