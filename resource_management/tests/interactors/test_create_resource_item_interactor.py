import pytest

from unittest.mock import create_autospec
from django_swagger_utils.drf_server.exceptions import NotFound, Forbidden

from resource_management.interactors.create_resource_item_interactor import \
    CreateResourceItemInteractor
from resource_management.interactors.storages.item_interface import \
    ItemInterface
from resource_management.interactors.storages.resource_interface import \
    ResourceInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface


def test_create_resource_item_with_invalid_resource_id_raise_exception():
    # Arrange
    resource_id = 1
    title = "Item 1"
    link = "www.item1.com"
    description = "This is about Item 1"
    user_id = 1

    item_storage = create_autospec(ItemInterface)
    resource_storage = create_autospec(ResourceInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = CreateResourceItemInteractor(
        item_storage=item_storage,
        resource_storage=resource_storage,
        presenter=presenter
    )
    resource_storage.check_is_resource_exists.return_value = False
    presenter.raise_exception_for_resource_not_found.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.create_resource_item(
            user_id=user_id,
            resource_id=resource_id,
            title=title,
            link=link,
            description=description
        )

    # Assert
    resource_storage.check_is_resource_exists.assert_called_once_with(
        resource_id=resource_id    
    )
    presenter.raise_exception_for_resource_not_found.assert_called_once()


def test_create_resource_item_with_user_raise_exception():
    # Arrange
    resource_id = 1
    title = "Item 1"
    link = "www.item1.com"
    description = "This is about Item 1"
    user_id = 1

    item_storage = create_autospec(ItemInterface)
    resource_storage = create_autospec(ResourceInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = CreateResourceItemInteractor(
        item_storage=item_storage,
        resource_storage=resource_storage,
        presenter=presenter
    )
    resource_storage.check_is_resource_exists.return_value = True
    resource_storage.check_is_user_admin.return_value = False
    presenter.raise_exception_for_unauthorized_user.side_effect = Forbidden

    # Act
    with pytest.raises(Forbidden):
        interactor.create_resource_item(
            user_id=user_id,
            resource_id=resource_id,
            title=title,
            link=link,
            description=description
        )

    # Assert
    resource_storage.check_is_resource_exists.assert_called_once_with(
        resource_id=resource_id    
    )
    resource_storage.check_is_user_admin.assert_called_once_with(
        user_id=user_id
    )
    presenter.raise_exception_for_unauthorized_user.assert_called_once()


def test_create_resource_item_with_admin_creates_resource_item():
    # Arrange
    resource_id = 1
    title = "Item 1"
    link = "www.item1.com"
    description = "This is about Item 1"
    user_id = 1

    item_storage = create_autospec(ItemInterface)
    resource_storage = create_autospec(ResourceInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = CreateResourceItemInteractor(
        item_storage=item_storage,
        resource_storage=resource_storage,
        presenter=presenter
    )
    resource_storage.check_is_resource_exists.return_value = True
    resource_storage.check_is_user_admin.return_value = True

    # Act
    interactor.create_resource_item(
        user_id=user_id,
        resource_id=resource_id,
        title=title,
        link=link,
        description=description
    )

    # Assert
    resource_storage.check_is_resource_exists.assert_called_once_with(
        resource_id=resource_id    
    )
    resource_storage.check_is_user_admin.assert_called_once_with(
        user_id=user_id
    )
    item_storage.create_resource_item.assert_called_once_with(
        resource_id=resource_id,
        title=title,
        link=link,
        description=description   
    )
    