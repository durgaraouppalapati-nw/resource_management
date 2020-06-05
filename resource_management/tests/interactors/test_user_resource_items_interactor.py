import pytest

from unittest.mock import create_autospec
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest

from resource_management.interactors.storages.user_interface import \
    UserInterface
from resource_management.interactors.storages.item_interface import \
    ItemInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from resource_management.interactors.user_resource_items_interactor import \
    UserResourceItemsInteractor


def test_user_resource_items_interactor_with_invalid_user_raise_exception():
    # Arrange
    user_id = 1
    offset = 0
    limit = 2
    search = ""
    user_storage = create_autospec(UserInterface)
    item_storage = create_autospec(ItemInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = UserResourceItemsInteractor(
        user_storage=user_storage,
        item_storage = item_storage,
        presenter=presenter
    )
    user_storage.check_is_user_exists.return_value = False
    presenter.raise_exception_for_invalid_user.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.get_resource_items_for_user(
            user_id=user_id,
            offset=offset,
            limit=limit,
            search=search
        )

    # Assert
    user_storage.check_is_user_exists.assert_called_once_with(user_id=user_id)
    presenter.raise_exception_for_invalid_user.assert_called_once()


def test_user_resource_items_interactor_with_invalid_offset_raise_exception():
    # Arrange
    user_id = 1
    offset = -1
    limit = 2
    search = ""
    user_storage = create_autospec(UserInterface)
    item_storage = create_autospec(ItemInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = UserResourceItemsInteractor(
        user_storage=user_storage,
        item_storage = item_storage,
        presenter=presenter
    )
    presenter.raise_exception_for_invalid_offset_length.side_effect = BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.get_resource_items_for_user(
            user_id=user_id,
            offset=offset,
            limit=limit,
            search=search
        )

    # Assert
    presenter.raise_exception_for_invalid_offset_length.assert_called_once()


def test_user_resource_items_interactor_with_invalid_limit_raise_exception():
    # Arrange
    user_id = 1
    offset = 0
    limit = -1
    search = ""
    user_storage = create_autospec(UserInterface)
    item_storage = create_autospec(ItemInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = UserResourceItemsInteractor(
        user_storage=user_storage,
        item_storage = item_storage,
        presenter=presenter
    )
    presenter.raise_exception_for_invalid_limit_length.side_effect = BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.get_resource_items_for_user(
            user_id=user_id,
            offset=offset,
            limit=limit,
            search=search
        )

    # Assert
    presenter.raise_exception_for_invalid_limit_length.assert_called_once()



def test_user_resource_items_interactor_with_user_return_user_resource_items(
        users_resource_items_dto):
    # Arrange
    user_id = 1
    offset = 0
    limit = 2
    search = ""
    user_storage = create_autospec(UserInterface)
    item_storage = create_autospec(ItemInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = UserResourceItemsInteractor(
        user_storage=user_storage,
        item_storage=item_storage,
        presenter=presenter
    )
    user_storage.check_is_user_exists.return_value = True
    item_storage.get_user_resource_items.return_value = \
        users_resource_items_dto

    # Act
    interactor.get_resource_items_for_user(
        user_id=user_id,
        offset=offset,
        limit=limit,
        search=search
    )

    # Assert
    user_storage.check_is_user_exists.assert_called_once_with(user_id=user_id)
    item_storage.get_user_resource_items.assert_called_once_with(
        user_id=user_id, offset=offset, limit=limit, search=search
    )
    presenter.get_response_for_user_resource_items\
        .assert_called_once_with(
            user_resource_items_dto=users_resource_items_dto
        )
