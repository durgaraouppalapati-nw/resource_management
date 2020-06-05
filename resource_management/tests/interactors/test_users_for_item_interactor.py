import pytest
from unittest.mock import create_autospec

from django_swagger_utils.drf_server.exceptions import BadRequest, NotFound

from resource_management.interactors.users_for_item_interactor import \
    UsersForItemInteractor
from resource_management.interactors.storages.user_interface import \
    UserInterface
from resource_management.interactors.storages.item_interface import \
    ItemInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from resource_management.interactors.storages.dtos import \
    UsersWithCountDetailsDto


def test_users_for_item_interactor_with_users_return_users_details(
        item_dtos,
        users_with_access_level_dtos,
        users_count_dto,
        users_with_access_level_response):
    # Arrange
    item_id = 1
    offset = 0
    limit = 10
    user_id = 1
    expected_output = users_with_access_level_response

    user_storage = create_autospec(UserInterface)
    item_storage = create_autospec(ItemInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = UsersForItemInteractor(
        user_storage=user_storage,
        item_storage=item_storage,
        presenter=presenter
    )
    users_with_count_dto = UsersWithCountDetailsDto(
        users_count_dto=users_count_dto,
        user_dtos=users_with_access_level_dtos    
    )

    user_storage.check_is_user_admin.return_value = True
    item_storage.check_is_resource_item_exists.return_value = True
    user_storage.get_users_for_item.return_value = users_with_count_dto
    presenter.get_response_for_get_users_for_item.return_value = \
        users_with_access_level_response

    # Act
    actual_output = interactor.get_users_for_item(
        item_id=item_id, offset=offset, limit=limit, user_id=user_id   
    )

    # Assert
    user_storage.check_is_user_admin.assert_called_once_with(
        user_id=user_id    
    )
    user_storage.get_users_for_item.assert_called_once_with(
        item_id=item_id, offset=offset, limit=limit    
    )
    presenter.get_response_for_get_users_for_item.assert_called_once_with(
        users_with_count_dto=users_with_count_dto    
    )
    assert expected_output == actual_output


def test_users_for_item_interactor_with_invalid_offset_raise_invalid_offset_exception():
    # Arrange
    item_id = 1
    offset = -1
    limit = 10
    user_id = 1

    user_storage = create_autospec(UserInterface)
    item_storage = create_autospec(ItemInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = UsersForItemInteractor(
        user_storage=user_storage,
        item_storage=item_storage,
        presenter=presenter
    )

    presenter.raise_exception_for_invalid_offset_length.side_effect = BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.get_users_for_item(
            item_id=item_id, offset=offset, limit=limit, user_id=user_id   
        )

    # Assert
    presenter.raise_exception_for_invalid_offset_length.assert_called_once()


def test_users_for_item_interactor_with_invalid_limit_raise_invalid_limit_exception():
    # Arrange
    item_id = 1
    offset = 0
    limit = -1
    user_id = 1

    user_storage = create_autospec(UserInterface)
    item_storage = create_autospec(ItemInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = UsersForItemInteractor(
        user_storage=user_storage,
        item_storage=item_storage,
        presenter=presenter
    )

    presenter.raise_exception_for_invalid_limit_length.side_effect = BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.get_users_for_item(
            item_id=item_id, offset=offset, limit=limit , user_id=user_id   
        )

    # Assert
    presenter.raise_exception_for_invalid_limit_length.assert_called_once()


def test_users_for_item_interactor_without_resource_item_raise_exception():
    # Arrange
    item_id = 1
    offset = 0
    limit = 10
    user_id = 1

    user_storage = create_autospec(UserInterface)
    item_storage = create_autospec(ItemInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = UsersForItemInteractor(
        user_storage=user_storage,
        item_storage=item_storage,
        presenter=presenter
    )

    user_storage.check_is_user_admin.return_value = True
    item_storage.check_is_resource_item_exists.return_value = False
    presenter.raise_exception_for_resource_item_not_found.side_effect = \
        NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.get_users_for_item(
            item_id=item_id, offset=offset, limit=limit, user_id=user_id
        )

    # Assert
    user_storage.check_is_user_admin.assert_called_once_with(
        user_id=user_id    
    )
    item_storage.check_is_resource_item_exists.assert_called_once_with(
        item_id=item_id
    )
    presenter.raise_exception_for_resource_item_not_found.assert_called_once()


def test_users_for_item_interactor_wit_user_raise_exception():
    # Arrange
    item_id = 1
    offset = 0
    limit = 10
    user_id = 1

    user_storage = create_autospec(UserInterface)
    item_storage = create_autospec(ItemInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = UsersForItemInteractor(
        user_storage=user_storage,
        item_storage=item_storage,
        presenter=presenter
    )

    user_storage.check_is_user_admin.return_value = False
    presenter.raise_exception_for_unauthorized_user.side_effect = BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.get_users_for_item(
            item_id=item_id, offset=offset, limit=limit, user_id=user_id
        )

    # Assert
    user_storage.check_is_user_admin.assert_called_once_with(
        user_id=user_id    
    )
    presenter.raise_exception_for_unauthorized_user.assert_called_once()
