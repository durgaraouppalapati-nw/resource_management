import pytest

from resource_management.storages.resource_storage_implementation import \
    ResourceStorageImplementation


@pytest.mark.django_db
def test_search_resources_with_individual_name_return_resource(
        create_resources, search_resources_by_individual_name):
    # Arrange
    search = "aws"
    resource_storage = ResourceStorageImplementation()
    expected_output = search_resources_by_individual_name

    # Act
    actual_output = resource_storage.search_resources(search=search)

    # Assert
    assert expected_output == actual_output


@pytest.mark.django_db
def test_search_resources_with_common_name_return_resources(
        create_resources, search_resources_by_common_name):
    # Arrange
    search = "it"
    resource_storage = ResourceStorageImplementation()
    expected_output = search_resources_by_common_name

    # Act
    actual_output = resource_storage.search_resources(search=search)

    # Assert
    assert expected_output == actual_output


@pytest.mark.django_db
def test_search_resources_with_unknown_name_return_empty(
        create_resources, search_resources_by_unknown_name):
    # Arrange
    search = "redit"
    resource_storage = ResourceStorageImplementation()
    expected_output = search_resources_by_unknown_name

    # Act
    actual_output = resource_storage.search_resources(search=search)

    # Assert
    assert expected_output == actual_output
