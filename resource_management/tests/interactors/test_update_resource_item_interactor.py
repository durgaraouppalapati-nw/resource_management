import pytest

from unittest.mock import create_autospec
from django_swagger_utils.drf_server.exceptions import NotFound, Forbidden

from resource_management.interactors.update_resource_item_interactor import \
    UpdateResourceItemInteractor
from resource_management.interactors.storages.item_interface import \
    ItemInterface
from resource_management.interactors.storages.user_interface import \
    UserInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface


def test_update_resource_item_with_invalid_item_id_raise_exception():
    # Arrange
    item_id = 2
    title = "Item 1"
    link = "www.item1.com"
    description = "This is about Item 1"
    user_id = 1

    item_storage = create_autospec(ItemInterface)
    user_storage = create_autospec(UserInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = UpdateResourceItemInteractor(
        item_storage=item_storage,
        user_storage=user_storage,
        presenter=presenter
    )
    user_storage.check_is_user_admin.return_value = True
    item_storage.check_is_resource_item_exists.return_value = False
    presenter.raise_exception_for_resource_item_not_found.side_effect = \
        NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.update_resource_item(
            user_id=user_id,
            item_id=item_id,
            title=title,
            link=link,
            description=description
        )

    # Assert
    user_storage.check_is_user_admin.assert_called_once_with(
        user_id=user_id
    )
    item_storage.check_is_resource_item_exists.assert_called_once_with(
        item_id=item_id    
    )
    presenter.raise_exception_for_resource_item_not_found.assert_called_once()


def test_update_resource_item_with_user_raise_exception():
    # Arrange
    item_id = 1
    title = "Item 1"
    link = "www.item1.com"
    description = "This is about Item 1"
    user_id = 1

    item_storage = create_autospec(ItemInterface)
    user_storage = create_autospec(UserInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = UpdateResourceItemInteractor(
        item_storage=item_storage,
        user_storage=user_storage,
        presenter=presenter
    )
    user_storage.check_is_user_admin.return_value = False
    presenter.raise_exception_for_unauthorized_user.side_effect = Forbidden

    # Act
    with pytest.raises(Forbidden):
        interactor.update_resource_item(
            user_id=user_id,
            item_id=item_id,
            title=title,
            link=link,
            description=description
        )

    # Assert
    user_storage.check_is_user_admin.assert_called_once_with(
        user_id=user_id
    )
    presenter.raise_exception_for_unauthorized_user.assert_called_once()


def test_update_resource_item_with_admin_updates_resource_item():
    # Arrange
    item_id = 1
    title = "Item 1"
    link = "www.item1.com"
    description = "This is about Item 1"
    user_id = 1

    item_storage = create_autospec(ItemInterface)
    user_storage = create_autospec(UserInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = UpdateResourceItemInteractor(
        item_storage=item_storage,
        user_storage=user_storage,
        presenter=presenter
    )
    item_storage.check_is_resource_item_exists.return_value = True
    user_storage.check_is_user_admin.return_value = True

    # Act
    interactor.update_resource_item(
        user_id=user_id,
        item_id=item_id,
        title=title,
        link=link,
        description=description
    )

    # Assert
    item_storage.check_is_resource_item_exists.assert_called_once_with(
        item_id=item_id    
    )
    user_storage.check_is_user_admin.assert_called_once_with(
        user_id=user_id
    )
    item_storage.update_resource_item.assert_called_once_with(
        item_id=item_id,
        title=title,
        link=link,
        description=description   
    )
