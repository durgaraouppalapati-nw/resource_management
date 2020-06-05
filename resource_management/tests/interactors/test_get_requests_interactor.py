import pytest
from unittest.mock import create_autospec

from django_swagger_utils.drf_server.exceptions import BadRequest

from resource_management.interactors.get_requests_interactor import \
    GetRequestsInteractor
from resource_management.interactors.storages.request_interface import \
    RequestInterface
from resource_management.interactors.storages.user_interface import \
    UserInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from resource_management.interactors.storages.dtos import \
    GetRequestsParametersDto


def test_get_requests_interactor_return_requests_details(
        request_dtos, requests_count_dto, requests_details_dto):
    # Arrange
    offset = 0
    limit = 5                   
    sortby = "DUE_DATETIME"
    filterby = "RESOURCE"
    value = "Resource 1"
    user_id = 1
    request_storage = create_autospec(RequestInterface)
    user_storage = create_autospec(UserInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetRequestsInteractor(request_storage=request_storage,
                                       user_storage=user_storage,
                                       presenter=presenter
                                      )

    user_storage.check_is_user_admin.return_value = True
    request_storage.get_requests.return_value = requests_count_dto, request_dtos

    # Act
    interactor.get_requests(
        offset=offset, limit=limit,
        sortby=sortby, filterby=filterby,
        value=value, user_id=user_id
    )

    # Assert
    user_storage.check_is_user_admin.assert_called_once_with(user_id=user_id)
    request_storage.get_requests.assert_called_once()
    presenter.get_response_for_get_requests.assert_called_once_with(
        requests_details_dto=requests_details_dto    
    )


def test_get_requests_interactor_with_invalid_offset_raise_invalid_offset_exception():
    # Arrange
    offset = -1
    limit = 5                   
    sortby = "DUE_DATETIME"
    filterby = "RESOURCE"
    value = "Resource 1"
    user_id = 1

    request_storage = create_autospec(RequestInterface)
    user_storage = create_autospec(UserInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetRequestsInteractor(request_storage=request_storage,
                                       user_storage=user_storage,
                                       presenter=presenter
                                      )
    presenter.raise_exception_for_invalid_offset_length.side_effect = BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.get_requests(
            offset=offset, limit=limit,
            sortby=sortby, filterby=filterby,
            value=value, user_id=user_id
        )

    # Assert
    presenter.raise_exception_for_invalid_offset_length.assert_called_once()


def test_get_requests_interactor_with_invalid_limit_raise_invalid_limit_exception():
    # Arrange
    offset = 0
    limit = -1                  
    sortby = "DUE_DATETIME"
    filterby = "RESOURCE"
    value = "Resource 1"
    user_id = 1

    request_storage = create_autospec(RequestInterface)
    user_storage = create_autospec(UserInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetRequestsInteractor(request_storage=request_storage,
                                       user_storage=user_storage,
                                       presenter=presenter
                                      )
    presenter.raise_exception_for_invalid_limit_length.side_effect = BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.get_requests(
            offset=offset, limit=limit,
            sortby=sortby, filterby=filterby,
            value=value, user_id=user_id
        )

    # Assert
    presenter.raise_exception_for_invalid_limit_length.assert_called_once()


def test_get_requests_interactor_with_invalid_limit_raise_invalid_limit_exception():
    # Arrange
    offset = 0
    limit = 10                  
    sortby = "DUE_DATETIME"
    filterby = "RESOURCE"
    value = "Resource 1"
    user_id = 1

    request_storage = create_autospec(RequestInterface)
    user_storage = create_autospec(UserInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetRequestsInteractor(request_storage=request_storage,
                                       user_storage=user_storage,
                                       presenter=presenter
                                      )
    user_storage.check_is_user_admin.return_value = False
    presenter.raise_exception_for_unauthorized_user.side_effect = BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.get_requests(
            offset=offset, limit=limit,
            sortby=sortby, filterby=filterby,
            value=value, user_id=user_id
        )

    # Assert
    user_storage.check_is_user_admin.assert_called_once_with(user_id=user_id)
    presenter.raise_exception_for_unauthorized_user.assert_called_once()
