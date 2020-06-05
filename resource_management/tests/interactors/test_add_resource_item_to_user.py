import pytest
from unittest.mock import create_autospec

from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest

from resource_management.interactors.add_item_to_user_interactor import \
    AddResourceItemToUserInteractor
from resource_management.interactors.storages.user_interface import \
    UserInterface
from resource_management.interactors.storages.item_interface import \
    ItemInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface


def test_add_item_to_user_interactor_with_invalid_user_raise_exception():
    # Arrange
    user_id = 1
    item_id = 2
    access_level = "READ"
    requested_user_id = 1

    user_storage = create_autospec(UserInterface)
    item_storage = create_autospec(ItemInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = AddResourceItemToUserInteractor(
        user_storage=user_storage,
        item_storage=item_storage,
        presenter=presenter
    )
    user_storage.check_is_user_admin.return_value = True
    user_storage.check_is_user_exists.return_value = False
    presenter.raise_exception_for_invalid_user.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.add_resource_item_to_user(
            user_id=user_id, item_id=item_id, access_level=access_level,
            requested_user_id=requested_user_id
        )

    # Assert
    user_storage.check_is_user_admin.assert_called_once_with(
        user_id=requested_user_id    
    )
    user_storage.check_is_user_exists.assert_called_once_with(user_id=user_id)
    presenter.raise_exception_for_invalid_user.assert_called_once()


def test_add_item_to_user_interactor_with_invalid_item_id_raise_exception():
    # Arrange
    user_id = 1
    item_id = 2
    access_level = "READ"
    requested_user_id = 1

    user_storage = create_autospec(UserInterface)
    item_storage = create_autospec(ItemInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = AddResourceItemToUserInteractor(
        user_storage=user_storage,
        item_storage=item_storage,
        presenter=presenter
    )
    user_storage.check_is_user_admin.return_value = True
    user_storage.check_is_user_exists.return_value = True
    item_storage.check_is_resource_item_exists.return_value = False
    presenter.raise_exception_for_resource_item_not_found.side_effect = \
        NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.add_resource_item_to_user(
            user_id=user_id, item_id=item_id, access_level=access_level,
            requested_user_id=requested_user_id
        )

    # Assert
    user_storage.check_is_user_admin.assert_called_once_with(
        user_id=requested_user_id    
    )
    user_storage.check_is_user_exists.assert_called_once_with(user_id=user_id)
    item_storage.check_is_resource_item_exists.assert_called_once_with(
        item_id=item_id
    )
    presenter.raise_exception_for_resource_item_not_found.assert_called_once()


def test_add_item_to_user_interactor_with_valid_details_add_item_to_user():
    # Arrange
    user_id = 1
    item_id = 2
    access_level = "READ"
    requested_user_id = 1

    user_storage = create_autospec(UserInterface)
    item_storage = create_autospec(ItemInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = AddResourceItemToUserInteractor(
        user_storage=user_storage,
        item_storage=item_storage,
        presenter=presenter
    )
    user_storage.check_is_user_admin.return_value = True
    user_storage.check_is_user_exists.return_value = True
    item_storage.check_is_resource_item_exists.return_value = True

    # Act
    interactor.add_resource_item_to_user(
        user_id=user_id, item_id=item_id, access_level=access_level,
        requested_user_id=requested_user_id
    )

    # Assert
    user_storage.check_is_user_admin.assert_called_once_with(
        user_id=requested_user_id    
    )
    user_storage.check_is_user_exists.assert_called_once_with(user_id=user_id)
    item_storage.check_is_resource_item_exists.assert_called_once_with(
        item_id=item_id
    )
    item_storage.add_resource_item_to_user.assert_called_once_with(
        user_id=user_id, item_id=item_id, access_level=access_level    
    )


def test_add_item_to_user_interactor_with_user_raise_exception():
    # Arrange
    user_id = 1
    item_id = 2
    access_level = "READ"
    requested_user_id = 1

    user_storage = create_autospec(UserInterface)
    item_storage = create_autospec(ItemInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = AddResourceItemToUserInteractor(
        user_storage=user_storage,
        item_storage=item_storage,
        presenter=presenter
    )
    user_storage.check_is_user_admin.return_value = False
    presenter.raise_exception_for_unauthorized_user.side_effect = BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.add_resource_item_to_user(
            user_id=user_id, item_id=item_id, access_level=access_level,
            requested_user_id=requested_user_id
        )

    # Assert
    user_storage.check_is_user_admin.assert_called_once_with(
        user_id=requested_user_id    
    )
    presenter.raise_exception_for_unauthorized_user.assert_called_once()
