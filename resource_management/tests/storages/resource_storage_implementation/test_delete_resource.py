import pytest

from resource_management.storages.resource_storage_implementation import \
    ResourceStorageImplementation
from resource_management.models import Resource


@pytest.mark.django_db
def test_delete_resource_with_resource_deletes_resource(resource):
    # Arrange
    resource_id = 1
    resource_storage = ResourceStorageImplementation()

    # Act
    resource_storage.delete_resource(resource_id=resource_id)

    # Assert
    Resource.objects.filter(id=resource_id).exists() == False
