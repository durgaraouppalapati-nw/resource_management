import pytest
from unittest.mock import create_autospec

from django_swagger_utils.drf_server.exceptions import BadRequest, NotFound

from resource_management.interactors.storages.dtos import \
    ItemsWithCountDetailsDto
from resource_management.interactors.storages.item_interface import \
    ItemInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from resource_management.interactors.resource_items_interactor import \
    ResourceItemsInteractor
from resource_management.interactors.storages.resource_interface import \
    ResourceInterface


def test_resource_items_intercator_with_resource_items_return_items_list(
        item_dtos, items_count_dto,
        resource_dto, items_with_count_dtos_response):
    # Arrange
    resource_id = 1
    offset = 0
    limit = 10
    user_id = 1
    expected_output = items_with_count_dtos_response

    item_storage = create_autospec(ItemInterface)
    resource_storage = create_autospec(ResourceInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = ResourceItemsInteractor(
        item_storage=item_storage,
        resource_storage=resource_storage,
        presenter=presenter
    )

    items_with_count_dto = ItemsWithCountDetailsDto(
        items_count_dto=items_count_dto,
        item_dtos=item_dtos,
        resource_dto=resource_dto
    )

    resource_storage.check_is_user_admin.return_value = True
    resource_storage.check_is_resource_exists.return_value = True
    item_storage.get_items_for_resource.return_value = items_with_count_dto
    presenter.get_response_for_get_items_for_resource.return_value = \
        items_with_count_dtos_response

    # Act
    actual_output = interactor.get_items_for_resource(
        resource_id=resource_id, offset=offset, limit=limit, user_id=user_id 
    )

    # Assert
    resource_storage.check_is_user_admin.assert_called_once_with(
        user_id=user_id    
    )
    resource_storage.check_is_resource_exists.assert_called_once_with(
        resource_id=resource_id    
    )
    item_storage.get_items_for_resource.assert_called_once_with(
        resource_id=resource_id, offset=offset, limit=limit    
    )
    presenter.get_response_for_get_items_for_resource.assert_called_once_with(
        items_with_count_dto=items_with_count_dto    
    )
    assert expected_output == actual_output


def test_resource_items_intercator_with_invalid_offset_raise_invalid_offset_exception():
    # Arrange
    resource_id = 1
    offset = -1
    limit = 10
    user_id = 1

    item_storage = create_autospec(ItemInterface)
    resource_storage = create_autospec(ResourceInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = ResourceItemsInteractor(
        item_storage=item_storage,
        resource_storage=resource_storage,
        presenter=presenter
    )
    presenter.raise_exception_for_invalid_offset_length.side_effect = BadRequest 

    # Act
    with pytest.raises(BadRequest):
        interactor.get_items_for_resource(
            resource_id=resource_id, offset=offset, limit=limit, user_id=user_id   
        )

    # Assert
    presenter.raise_exception_for_invalid_offset_length.assert_called_once()


def test_resource_items_intercator_with_invalid_limit_raise_invalid_limit_exception():
    # Arrange
    resource_id = 1
    offset = 0
    limit = -1
    user_id = 1

    item_storage = create_autospec(ItemInterface)
    resource_storage = create_autospec(ResourceInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = ResourceItemsInteractor(
        item_storage=item_storage,
        resource_storage=resource_storage,
        presenter=presenter
    )
    presenter.raise_exception_for_invalid_limit_length.side_effect = BadRequest 

    # Act
    with pytest.raises(BadRequest):
        interactor.get_items_for_resource(
            resource_id=resource_id, offset=offset, limit=limit, user_id=user_id   
        )

    # Assert
    presenter.raise_exception_for_invalid_limit_length.assert_called_once()


def test_resource_items_intercator_when_resource_not_found_raise_resource_not_found_exception():
    # Arrange
    resource_id = 1
    offset = 0
    limit = 10
    user_id = 1

    item_storage = create_autospec(ItemInterface)
    resource_storage = create_autospec(ResourceInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = ResourceItemsInteractor(
        item_storage=item_storage,
        resource_storage=resource_storage,
        presenter=presenter
    )
    resource_storage.check_is_user_admin.return_value = True
    resource_storage.check_is_resource_exists.return_value = False
    presenter.raise_exception_for_resource_not_found.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.get_items_for_resource(
            resource_id=resource_id, offset=offset, limit=limit, user_id=user_id   
        )

    # Assert
    resource_storage.check_is_resource_exists.assert_called_once_with(
        resource_id=resource_id    
    )
    presenter.raise_exception_for_resource_not_found.assert_called_once()


def test_resource_items_intercator_with_user_raise_unauthorized_user_exception():
    # Arrange
    resource_id = 1
    offset = 0
    limit = 10
    user_id = 1

    item_storage = create_autospec(ItemInterface)
    resource_storage = create_autospec(ResourceInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = ResourceItemsInteractor(
        item_storage=item_storage,
        resource_storage=resource_storage,
        presenter=presenter
    )
    resource_storage.check_is_user_admin.return_value = False
    presenter.raise_exception_for_unauthorized_user.side_effect = BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.get_items_for_resource(
            resource_id=resource_id, offset=offset, limit=limit, user_id=user_id   
        )

    # Assert
    resource_storage.check_is_user_admin.assert_called_once_with(
        user_id=user_id
    )
    presenter.raise_exception_for_unauthorized_user.assert_called_once()
