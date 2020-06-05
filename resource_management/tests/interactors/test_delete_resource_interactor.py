import pytest

from unittest.mock import create_autospec, Mock
from django_swagger_utils.drf_server.exceptions import Forbidden, NotFound

from resource_management.interactors.delete_resource_interactor import \
    DeleteResourceInteractor
from resource_management.interactors.storages.resource_interface import \
    ResourceInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface


def test_delete_resource_interactor_with_user_raise_unauthorized_user_exception():
    # Arrange
    user_id = 1,
    resource_id = 1
    resource_storage = create_autospec(ResourceInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = DeleteResourceInteractor(
        resource_storage=resource_storage,
        presenter=presenter
    )
    resource_storage.check_is_user_admin.return_value = False
    presenter.raise_exception_for_unauthorized_user.side_effect = Forbidden

    # Act
    with pytest.raises(Forbidden):
        interactor.delete_resource(
            user_id=user_id,
            resource_id=resource_id
        )

    # Assert
    resource_storage.check_is_user_admin.assert_called_once_with(
        user_id=user_id
    )
    presenter.raise_exception_for_unauthorized_user.assert_called_once()


def test_delete_resource_interactor_without_resource_raise_resource_notfound_exception():
    # Arrange
    user_id = 1,
    resource_id = 1
    resource_storage = create_autospec(ResourceInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = DeleteResourceInteractor(
        resource_storage=resource_storage,
        presenter=presenter
    )
    resource_storage.check_is_user_admin.return_value = True
    resource_storage.check_is_resource_exists.return_value = False
    presenter.raise_exception_for_resource_not_found.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.delete_resource(
            user_id=user_id,
            resource_id=resource_id
        )

    # Assert
    resource_storage.check_is_user_admin.assert_called_once_with(
        user_id=user_id
    )
    resource_storage.check_is_resource_exists.assert_called_once_with(
        resource_id=resource_id
    )
    presenter.raise_exception_for_resource_not_found.assert_called_once()


def test_delete_resource_interactor_with_admin_deletes_resource():
    # Arrange
    user_id = 1
    resource_id = 1
    resource_storage = create_autospec(ResourceInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = DeleteResourceInteractor(
        resource_storage=resource_storage,
        presenter=presenter
    )
    resource_storage.check_is_user_admin.return_value = True
    resource_storage.check_is_resource_exists.return_value = True

    # Act
    interactor.delete_resource(
                               user_id=user_id,
                               resource_id=resource_id
                              )

    # Assert
    resource_storage.check_is_user_admin.assert_called_once_with(
        user_id=user_id
    )
    resource_storage.check_is_resource_exists.assert_called_once_with(
            resource_id=resource_id
    )
    resource_storage.delete_resource.assert_called_once_with(
        resource_id=resource_id
    )
