import pytest
from unittest.mock import create_autospec

from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest

from resource_management.interactors.delete_request_interactor import \
    DeleteRequestIntercator
from resource_management.interactors.storages.request_interface import \
    RequestInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface


def test_delete_request_interactor_without_request_raise_exception():
    # Arrange
    request_id = 1
    user_id = 2
    request_storage = create_autospec(RequestInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = DeleteRequestIntercator(
        request_storage=request_storage,
        presenter=presenter
    )
    request_storage.check_is_request_exists.return_value = False
    presenter.raise_exception_for_request_not_found.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.delete_request(user_id=user_id, request_id=request_id)

    # Assert
    request_storage.check_is_request_exists.assert_called_once_with(
        request_id=request_id    
    )
    presenter.raise_exception_for_request_not_found.assert_called_once()


def test_delete_request_interactor_with_different_user_raise_exception():
    # Arrange
    request_id = 1
    user_id = 2
    request_storage = create_autospec(RequestInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = DeleteRequestIntercator(
        request_storage=request_storage,
        presenter=presenter
    )
    request_storage.check_is_request_exists.return_value = True
    request_storage.check_is_user_creator_of_request.return_value = False
    presenter.raise_user_can_not_delete_request_exception.side_effect = \
        BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.delete_request(user_id=user_id, request_id=request_id)

    # Assert
    request_storage.check_is_request_exists.assert_called_once_with(
        request_id=request_id    
    )
    request_storage.check_is_user_creator_of_request.assert_called_once_with(
        request_id=request_id, user_id=user_id    
    )
    presenter.raise_user_can_not_delete_request_exception.assert_called_once()


def test_delete_request_interactor_when_admin_responded_raise_exception():
    # Arrange
    request_id = 1
    user_id = 2
    request_storage = create_autospec(RequestInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = DeleteRequestIntercator(
        request_storage=request_storage,
        presenter=presenter
    )
    request_storage.check_is_request_exists.return_value = True
    request_storage.check_is_user_creator_of_request.return_value = True
    request_storage.check_is_admin_responded_to_request.return_value = True
    presenter.raise_admin_already_responded_to_request_exception.side_effect = \
        BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.delete_request(user_id=user_id, request_id=request_id)

    # Assert
    request_storage.check_is_request_exists.assert_called_once_with(
        request_id=request_id    
    )
    request_storage.check_is_user_creator_of_request.assert_called_once_with(
        request_id=request_id, user_id=user_id    
    )
    request_storage.check_is_admin_responded_to_request.assert_called_once_with(
        request_id=request_id
    )
    presenter.raise_admin_already_responded_to_request_exception.assert_called_once()


def test_delete_request_interactor_with_proper_details_deletes_request():
    # Arrange
    request_id = 1
    user_id = 2
    request_storage = create_autospec(RequestInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = DeleteRequestIntercator(
        request_storage=request_storage,
        presenter=presenter
    )
    request_storage.check_is_request_exists.return_value = True
    request_storage.check_is_user_creator_of_request.return_value = True
    request_storage.check_is_admin_responded_to_request.return_value = False

    # Act
    interactor.delete_request(user_id=user_id, request_id=request_id)

    # Assert
    request_storage.check_is_request_exists.assert_called_once_with(
        request_id=request_id    
    )
    request_storage.check_is_user_creator_of_request.assert_called_once_with(
        request_id=request_id, user_id=user_id    
    )
    request_storage.check_is_admin_responded_to_request.assert_called_once_with(
        request_id=request_id
    )
    request_storage.delete_request.assert_called_once_with(
        request_id=request_id
    )
