import pytest
from unittest.mock import create_autospec

from django_swagger_utils.drf_server.exceptions import BadRequest, NotFound

from resource_management.interactors.get_user_requests_interactor import \
    GetUserRequestsInteractor
from resource_management.interactors.storages.request_interface import \
    RequestInterface
from resource_management.interactors.storages.user_interface import \
    UserInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from resource_management.interactors.storages.dtos import \
    GetRequestsParametersDto


def test_get_user_requests_interactor_return_requests_details(
        requests_status_dtos,
        requests_count_dto,
        get_requests_parameters_dto):
    # Arrange
    user_id = 1

    request_storage = create_autospec(RequestInterface)
    user_storage = create_autospec(UserInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetUserRequestsInteractor(
        request_storage=request_storage,
        user_storage=user_storage,
        presenter=presenter
    )
    user_storage.check_is_user_exists.return_value = True
    request_storage.get_user_requests.return_value = \
        requests_count_dto, requests_status_dtos

    # Act
    interactor.get_user_requests(
        user_id, get_requests_parameters_dto
    )

    # Assert
    user_storage.check_is_user_exists.assert_called_once_with(user_id=user_id)
    request_storage.get_user_requests.assert_called_once_with(
        user_id=user_id, requests_parameters_dto=get_requests_parameters_dto
    )
    presenter.get_response_for_get_user_requests.assert_called_once_with(
        requests_details_dto=requests_status_dtos,
        requests_count_dto=requests_count_dto
    )


def test_get_user_requests_interactor_with_invalid_offset_raise_exception(
        get_requests_parameters_dto_with_invalid_offset):
    # Arrange
    user_id = 1

    request_storage = create_autospec(RequestInterface)
    user_storage = create_autospec(UserInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetUserRequestsInteractor(
        request_storage=request_storage,
        user_storage=user_storage,
        presenter=presenter
    )
    presenter.raise_exception_for_invalid_offset_length.side_effect = BadRequest
    
    # Act
    with pytest.raises(BadRequest):
        interactor.get_user_requests(
            user_id, get_requests_parameters_dto_with_invalid_offset
        )

    # Assert
    presenter.raise_exception_for_invalid_offset_length.assert_called_once()


def test_get_user_requests_interactor_with_invalid_limit_raise_exception(
        get_requests_parameters_dto_with_invalid_limit):
    # Arrange
    user_id = 1

    request_storage = create_autospec(RequestInterface)
    user_storage = create_autospec(UserInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetUserRequestsInteractor(
        request_storage=request_storage,
        user_storage=user_storage,
        presenter=presenter
    )
    presenter.raise_exception_for_invalid_limit_length.side_effect = BadRequest
    
    # Act
    with pytest.raises(BadRequest):
        interactor.get_user_requests(
            user_id, get_requests_parameters_dto_with_invalid_limit
        )

    # Assert
    presenter.raise_exception_for_invalid_limit_length.assert_called_once()


def test_get_user_requests_interactor_when_user_not_found_raise_exceeption(
        get_requests_parameters_dto):
    # Arrange
    user_id = 1

    request_storage = create_autospec(RequestInterface)
    user_storage = create_autospec(UserInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetUserRequestsInteractor(
        request_storage=request_storage,
        user_storage=user_storage,
        presenter=presenter
    )
    user_storage.check_is_user_exists.return_value = False
    presenter.raise_exception_for_invalid_user.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.get_user_requests(
            user_id, get_requests_parameters_dto
        )

    # Assert
    user_storage.check_is_user_exists.assert_called_once_with(user_id=user_id)
    presenter.raise_exception_for_invalid_user.assert_called_once()
