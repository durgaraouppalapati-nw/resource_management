import pytest

from unittest.mock import create_autospec, Mock
from django_swagger_utils.drf_server.exceptions import Forbidden, NotFound

from resource_management.interactors.update_resource_interactor import \
    UpdateResourceInteractor
from resource_management.interactors.storages.resource_interface import \
    ResourceInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface


def test_update_resource_interactor_with_user_raise_unauthorized_user_exception():
    # Arrange
    user_id = 1,
    resource_id = 1
    name = "Resource 1"
    resource_pic = "www.resource1/pic.com"
    link = "www.resource.com"
    description = "This is About Resource"
    resource_storage = create_autospec(ResourceInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = UpdateResourceInteractor(
        resource_storage=resource_storage,
        presenter=presenter
    )
    resource_storage.check_is_user_admin.return_value = False
    presenter.raise_exception_for_unauthorized_user.side_effect = Forbidden

    # Act
    with pytest.raises(Forbidden):
        interactor.update_resource(
            user_id=user_id,
            resource_id=resource_id,
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


def test_update_resource_interactor_without_resource_raise_resource_notfound_exception():
    # Arrange
    user_id = 1,
    resource_id = 1
    name = "Resource 1"
    resource_pic = "www.resource1/pic.com"
    link = "www.resource.com"
    description = "This is About Resource"
    resource_storage = create_autospec(ResourceInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = UpdateResourceInteractor(
        resource_storage=resource_storage,
        presenter=presenter
    )
    resource_storage.check_is_user_admin.return_value = True
    resource_storage.check_is_resource_exists.return_value = False
    presenter.raise_exception_for_resource_not_found.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.update_resource(
            user_id=user_id,
            resource_id=resource_id,
            name=name,
            resource_pic=resource_pic,
            link=link,
            description=description
        )

    # Assert
    resource_storage.check_is_user_admin.assert_called_once_with(
        user_id=user_id
    )
    resource_storage.check_is_resource_exists.assert_called_once_with(
        resource_id=resource_id
    )
    presenter.raise_exception_for_resource_not_found.assert_called_once()


def test_create_resource_interactor_with_admin_updates_resource(resource_dto):
    # Arrange
    user_id = 1
    resource_id = 1
    name = "Resource 1"
    resource_pic = "www.resource1/pic.com"
    link = "www.resource.com"
    description = "This is About Resource"
    resource_dto = resource_dto
    resource_storage = create_autospec(ResourceInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = UpdateResourceInteractor(
        resource_storage=resource_storage,
        presenter=presenter
    )
    resource_storage.check_is_user_admin.return_value = True
    resource_storage.check_is_resource_exists.return_value = True
    resource_storage.update_resource_and_get_dto.return_value = resource_dto

    # Act
    interactor.update_resource(
                              user_id=user_id,
                              resource_id=resource_id,
                              name=name,
                              resource_pic=resource_pic,
                              link=link,
                              description=description
                            )

    # Assert
    resource_storage.check_is_user_admin.assert_called_once_with(
        user_id=user_id
    )
    resource_storage.check_is_resource_exists.assert_called_once_with(
        resource_id=resource_id
    )
    resource_storage.update_resource_and_get_dto.assert_called_once_with(
        name=name,
        resource_id=resource_id,
        resource_pic=resource_pic,
        link=link,
        description=description
    )
    presenter.get_response_for_update_resource.assert_called_once_with(
        resource_dto=resource_dto    
    )
