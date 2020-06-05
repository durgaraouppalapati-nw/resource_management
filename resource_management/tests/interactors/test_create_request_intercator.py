import pytest
from unittest.mock import create_autospec

from datetime import datetime

from django_swagger_utils.drf_server.exceptions import \
    NotFound, ExpectationFailed

from resource_management.interactors.create_request_interactor import \
    CreateRequestInteractor
from resource_management.interactors.storages.request_interface import \
    RequestInterface
from resource_management.interactors.storages.item_interface import \
    ItemInterface
from resource_management.interactors.storages.resource_interface import \
    ResourceInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from resource_management.interactors.storages.dtos import RequestDto


def test_create_request_interactor_with_invalid_resource_raise_exception():
    # Arrange
    user_id = 1
    resource_id = 1
    item_id = 2
    access_level = "READ"
    due_datetime = datetime(2020, 6, 1, 10, 0)
    reason_for_access = "Wanted to do work"
    
    request_dto = RequestDto(resource_id=resource_id,
                             item_id=item_id,
                             access_level=access_level,
                             due_datetime=due_datetime,
                             reason_for_access=reason_for_access
                            )

    resource_storage = create_autospec(ResourceInterface)
    item_storage = create_autospec(ItemInterface)
    request_storage = create_autospec(RequestInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = CreateRequestInteractor(
        resource_storage=resource_storage,
        request_storage=request_storage,
        item_storage=item_storage,
        presenter=presenter
    )
    resource_storage.check_is_resource_exists.return_value = False
    presenter.raise_exception_for_resource_not_found.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.create_request(user_id=user_id, request_dto=request_dto)

    # Assert
    resource_storage.check_is_resource_exists.assert_called_once_with(
        resource_id=resource_id    
    )
    presenter.raise_exception_for_resource_not_found.assert_called_once()


def test_create_request_interactor_with_invalid_item_raise_exception():
    # Arrange
    user_id = 1
    resource_id = 1
    item_id = 2
    access_level = "READ"
    due_datetime = datetime(2020, 6, 1, 10, 0)
    reason_for_access = "Wanted to do work"
    
    request_dto = RequestDto(resource_id=resource_id,
                             item_id=item_id,
                             access_level=access_level,
                             due_datetime=due_datetime,
                             reason_for_access=reason_for_access
                            )

    resource_storage = create_autospec(ResourceInterface)
    item_storage = create_autospec(ItemInterface)
    request_storage = create_autospec(RequestInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = CreateRequestInteractor(
        resource_storage=resource_storage,
        request_storage=request_storage,
        item_storage=item_storage,
        presenter=presenter
    )
    resource_storage.check_is_resource_exists.return_value = True
    item_storage.check_is_resource_item_exists.return_value = False
    presenter.raise_exception_for_resource_item_not_found.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.create_request(user_id=user_id, request_dto=request_dto)

    # Assert
    resource_storage.check_is_resource_exists.assert_called_once_with(
        resource_id=resource_id    
    )
    item_storage.check_is_resource_item_exists.assert_called_once_with(
        item_id=item_id
    )
    presenter.raise_exception_for_resource_item_not_found.assert_called_once()


def test_create_request_interactor_with_item_not_belongs_to_resource_raise_exception():
    # Arrange
    user_id = 1
    resource_id = 1
    item_id = 2
    access_level = "READ"
    due_datetime = datetime(2020, 6, 1, 10, 0)
    reason_for_access = "Wanted to do work"
    
    request_dto = RequestDto(resource_id=resource_id,
                             item_id=item_id,
                             access_level=access_level,
                             due_datetime=due_datetime,
                             reason_for_access=reason_for_access
                            )

    resource_storage = create_autospec(ResourceInterface)
    item_storage = create_autospec(ItemInterface)
    request_storage = create_autospec(RequestInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = CreateRequestInteractor(
        resource_storage=resource_storage,
        request_storage=request_storage,
        item_storage=item_storage,
        presenter=presenter
    )
    resource_storage.check_is_resource_exists.return_value = True
    item_storage.check_is_resource_item_exists.return_value = True
    item_storage.check_is_resource_item_belongs_to_resource.return_value = False
    presenter.raise_exception_for_item_not_belongs_to_resource.side_effect = \
        ExpectationFailed

    # Act
    with pytest.raises(ExpectationFailed):
        interactor.create_request(user_id=user_id, request_dto=request_dto)

    # Assert
    resource_storage.check_is_resource_exists.assert_called_once_with(
        resource_id=resource_id    
    )
    item_storage.check_is_resource_item_exists.assert_called_once_with(
        item_id=item_id
    )
    item_storage.check_is_resource_item_belongs_to_resource\
        .assert_called_once_with(
            resource_id=resource_id, item_id=item_id 
        )
    presenter.raise_exception_for_item_not_belongs_to_resource.assert_called_once()


def test_create_request_interactor_with_valid_details_creates_request():
    # Arrange
    user_id = 1
    resource_id = 1
    item_id = 2
    access_level = "READ"
    due_datetime = datetime(2020, 6, 1, 10, 0)
    reason_for_access = "Wanted to do work"
    
    request_dto = RequestDto(resource_id=resource_id,
                             item_id=item_id,
                             access_level=access_level,
                             due_datetime=due_datetime,
                             reason_for_access=reason_for_access
                            )

    resource_storage = create_autospec(ResourceInterface)
    item_storage = create_autospec(ItemInterface)
    request_storage = create_autospec(RequestInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = CreateRequestInteractor(
        resource_storage=resource_storage,
        request_storage=request_storage,
        item_storage=item_storage,
        presenter=presenter
    )
    resource_storage.check_is_resource_exists.return_value = True
    item_storage.check_is_resource_item_exists.return_value = True
    item_storage.check_is_resource_item_belongs_to_resource.return_value = True

    # Act
    interactor.create_request(user_id=user_id, request_dto=request_dto)

    # Assert
    resource_storage.check_is_resource_exists.assert_called_once_with(
        resource_id=resource_id    
    )
    item_storage.check_is_resource_item_exists.assert_called_once_with(
        item_id=item_id
    )
    item_storage.check_is_resource_item_belongs_to_resource\
        .assert_called_once_with(
            resource_id=resource_id, item_id=item_id 
        )
    request_storage.create_request.assert_called_once_with(
        user_id=user_id, request_dto=request_dto
    )
