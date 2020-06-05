import pytest

from resource_management.storages.resource_storage_implementation import \
    ResourceStorageImplementation
from resource_management.models import Resource


@pytest.mark.django_db
def test_create_resource_creates_resource():
    # Arrange
    name = "Resource_1"
    link = "www.resource.com"
    description = "This is Resource 1"
    resource_pic = "www.resource/pic.com"
    resource_storage = ResourceStorageImplementation()

    # Act
    resource_storage.create_resource(
        name=name, link=link, description=description,
        resource_pic=resource_pic
    )

    # Assert
    resource = Resource.objects.get(id=1)

    assert resource.name == name
    assert resource.link == link
    assert resource.description == description
    assert resource.resource_pic == resource_pic
