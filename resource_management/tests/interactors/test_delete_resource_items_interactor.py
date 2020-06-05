import pytest

from unittest.mock import create_autospec
from django_swagger_utils.drf_server.exceptions import NotFound, Forbidden

from resource_management.interactors.delete_resource_items_interactor import \
    DeleteResourceItemsInteractor
from resource_management.interactors.storages.item_interface import \
    ItemInterface
from resource_management.interactors.storages.user_interface import \
    UserInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface


def test_delete_resource_items_with_user_raise_exception():
    # Arrange
    item_ids = [1, 2, 3]
    user_id = 1

    item_storage = create_autospec(ItemInterface)
    user_storage = create_autospec(UserInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = DeleteResourceItemsInteractor(
        item_storage=item_storage,
        user_storage=user_storage,
        presenter=presenter
    )
    user_storage.check_is_user_admin.return_value = False
    presenter.raise_exception_for_unauthorized_user.side_effect = Forbidden

    # Act
    with pytest.raises(Forbidden):
        interactor.delete_resource_items(
            user_id=user_id,
            item_ids=item_ids
        )

    # Assert
    user_storage.check_is_user_admin.assert_called_once_with(
        user_id=user_id
    )
    presenter.raise_exception_for_unauthorized_user.assert_called_once()


def test_delete_resource_items_with_admin_deletes_resource_items():
    # Arrange
    item_ids = [1, 2, 3]
    user_id = 1

    item_storage = create_autospec(ItemInterface)
    user_storage = create_autospec(UserInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = DeleteResourceItemsInteractor(
        item_storage=item_storage,
        user_storage=user_storage,
        presenter=presenter
    )
    user_storage.check_is_user_admin.return_value = True

    # Act
    interactor.delete_resource_items(
        user_id=user_id,
        item_ids=item_ids,
    )

    # Assert
    user_storage.check_is_user_admin.assert_called_once_with(
        user_id=user_id
    )
    item_storage.delete_resource_items.assert_called_once_with(
        item_ids=item_ids
    )
