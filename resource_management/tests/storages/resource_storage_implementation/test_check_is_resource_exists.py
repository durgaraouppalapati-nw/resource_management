import pytest

from resource_management.storages.resource_storage_implementation import \
    ResourceStorageImplementation


@pytest.mark.django_db
def test_check_is_resource_exists_with_resource_return_true(resource):
    # Arrange
    resource_id = 1
    resource_storage = ResourceStorageImplementation()
    expected_output = True

    # Act
    actual_output = resource_storage.check_is_resource_exists(
        resource_id=resource_id
    )

    # Assert
    assert expected_output == actual_output
