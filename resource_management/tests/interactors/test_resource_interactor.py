import pytest
from unittest.mock import create_autospec

from django_swagger_utils.drf_server.exceptions import BadRequest

from resource_management.interactors.storages.dtos import ResourcesDetailsDto
from resource_management.interactors.storages.resource_interface import \
    ResourceInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from resource_management.interactors.resources_interactor import \
    ResourceInteractor


def test_resource_intercator_with_resources_return_resources_list(
        resource_dtos,
        resources_count_dto):
    # Arrange
    offset = 0
    limit = 10
    user_id = 1

    resource_storage = create_autospec(ResourceInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = ResourceInteractor(
        resource_storage=resource_storage,
        presenter=presenter
    )
    resources_details_dto = ResourcesDetailsDto(resource_dtos=resource_dtos,
                                                resources_count_dto=resources_count_dto
                                               )

    resource_storage.check_is_user_admin.return_value = True
    resource_storage.get_all_resources.return_value = resources_details_dto

    # Act
    interactor.get_all_resources(
        offset=offset, limit=limit, user_id=user_id
    )

    # Assert
    resource_storage.get_all_resources.assert_called_once_with(
        offset=offset, limit=limit
    )
    resource_storage.check_is_user_admin.assert_called_once_with(
        user_id=user_id    
    )
    presenter.get_response_for_get_all_resources.assert_called_once()


def test_resource_intercator_with_invalid_offset_raise_exception(
        resource_dtos,
        resources_count_dto):
    # Arrange
    offset = -1
    limit = 10
    user_id=1

    resource_storage = create_autospec(ResourceInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = ResourceInteractor(
        resource_storage=resource_storage,
        presenter=presenter
    )
    presenter.raise_exception_for_invalid_offset_length.side_effect = BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.get_all_resources(
            offset=offset, limit=limit, user_id=user_id
        )

    # Assert
    presenter.raise_exception_for_invalid_offset_length.assert_called_once()


def test_resource_intercator_with_invalid_limit_raise_exception(
        resource_dtos,
        resources_count_dto):
    # Arrange
    offset = 0
    limit = -1
    user_id = 1

    resource_storage = create_autospec(ResourceInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = ResourceInteractor(
        resource_storage=resource_storage,
        presenter=presenter
    )
    presenter.raise_exception_for_invalid_limit_length.side_effect = BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.get_all_resources(
            offset=offset, limit=limit, user_id=user_id
        )

    # Assert
    presenter.raise_exception_for_invalid_limit_length.assert_called_once()


def test_resource_intercator_with_user_raise_exception(
        resource_dtos,
        resources_count_dto):
    # Arrange
    offset = 0
    limit = 10
    user_id = 1

    resource_storage = create_autospec(ResourceInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = ResourceInteractor(
        resource_storage=resource_storage,
        presenter=presenter
    )
    resource_storage.check_is_user_admin.return_value = False
    presenter.raise_exception_for_unauthorized_user.side_effect = BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.get_all_resources(
            offset=offset, limit=limit, user_id=user_id
        )

    # Assert
    resource_storage.check_is_user_admin.assert_called_once_with(
        user_id=user_id
    )
    presenter.raise_exception_for_unauthorized_user.assert_called_once()
