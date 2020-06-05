import pytest

from resource_management.storages.resource_storage_implementation import \
    ResourceStorageImplementation


@pytest.mark.django_db
def test_get_all_resources_with_resources_return_resources_details_dto(
        resources, resources_details_dto):
    # Arrange
    offset = 0
    limit = 5
    resource_storage = ResourceStorageImplementation()
    expected_output = resources_details_dto

    # Act
    actual_output = resource_storage.get_all_resources(
        offset=offset, limit=limit
    )

    # Assert
    assert expected_output == actual_output


@pytest.mark.django_db
def test_get_all_resources_with_no_resources_return_empty(
        resources_details_dto_with_empty):
    # Arrange
    offset = 0
    limit = 5
    resource_storage = ResourceStorageImplementation()
    expected_output = resources_details_dto_with_empty

    # Act
    actual_output = resource_storage.get_all_resources(
        offset=offset, limit=limit    
    )

    # Assert
    assert expected_output == actual_output
