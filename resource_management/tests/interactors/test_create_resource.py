import pytest

from unittest.mock import create_autospec
from django_swagger_utils.drf_server.exceptions import \
    Forbidden, ExpectationFailed

from resource_management.interactors.create_resource_interactor import \
    CreateResourceInteractor
from resource_management.interactors.storages.resource_interface import \
    ResourceInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface


def test_create_resource_interactor_with_user_raise_unauthorized_user_exception():
    # Arrange
    user_id = 1
    name = "Resource 1"
    resource_pic = "www.resource1/pic.com"
    link = "www.resource.com"
    description = "This is About Resource"
    resource_storage = create_autospec(ResourceInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = CreateResourceInteractor(
        resource_storage=resource_storage,
        presenter=presenter
    )
    resource_storage.check_is_user_admin.return_value = False
    presenter.raise_exception_for_unauthorized_user.side_effect = Forbidden

    # Act
    with pytest.raises(Forbidden):
        interactor.create_resource(
            user_id=user_id,
            name=name,
            resource_pic=resource_pic,
            link=link,
            description=description
        )

    # Assert
    resource_storage.check_is_user_admin.assert_called_once_with(
        user_id=user_id
    )
    presenter.raise_exception_for_unauthorized_user.assert_called_once()


def test_create_resource_interactor_with_resource_name_already_exists_user_exception():
    # Arrange
    user_id = 1
    name = "Resource 1"
    resource_pic = "www.resource1/pic.com"
    link = "www.resource.com"
    description = "This is About Resource"
    resource_storage = create_autospec(ResourceInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = CreateResourceInteractor(
        resource_storage=resource_storage,
        presenter=presenter
    )
    resource_storage.check_is_user_admin.return_value = True
    resource_storage.check_is_resource_name_already_exists.return_value = True
    presenter.raise_exception_for_resource_name_already_exists.side_effect = \
        ExpectationFailed

    # Act
    with pytest.raises(ExpectationFailed):
        interactor.create_resource(
            user_id=user_id,
            name=name,
            resource_pic=resource_pic,
            link=link,
            description=description
        )

    # Assert
    resource_storage.check_is_user_admin.assert_called_once_with(
        user_id=user_id
    )
    resource_storage.check_is_resource_name_already_exists\
        .assert_called_once_with(resource_name=name)
    presenter.raise_exception_for_resource_name_already_exists\
        .assert_called_once()


def test_create_resource_interactor_with_admin_create_post():
    # Arrange
    user_id = 1
    name = "Resource 1"
    resource_pic = "www.resource1/pic.com"
    link = "www.resource.com"
    description = "This is About Resource"
    resource_storage = create_autospec(ResourceInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = CreateResourceInteractor(
        resource_storage=resource_storage,
        presenter=presenter
    )
    resource_storage.check_is_user_admin.return_value = True
    resource_storage.check_is_resource_name_already_exists.return_value = False

    # Act
    interactor.create_resource(
        user_id=user_id,
        name=name,
        resource_pic=resource_pic,
        link=link,
        description=description
    )

    # Assert
    resource_storage.check_is_user_admin.assert_called_once_with(
        user_id=user_id
    )
    resource_storage.check_is_resource_name_already_exists\
        .assert_called_once_with(resource_name=name)
    resource_storage.create_resource.assert_called_once_with(
        name=name,
        resource_pic=resource_pic,
        link=link,
        description=description
    )