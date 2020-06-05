import pytest

from resource_management.storages.resource_storage_implementation import \
    ResourceStorageImplementation


@pytest.mark.django_db
def test_update_resource_and_get_dto_with_resource_return_resource_dto(
        resource, updated_resource_dto):
    # Arrange
    resource_id = 1
    name = "Resource_1"
    link = "www.resource.com"
    description = "This is Resource 1"
    resource_pic = "www.resource/pic.com"
    resource_storage = ResourceStorageImplementation()

    # Act
    actual_resource_dto = resource_storage.update_resource_and_get_dto(
        name=name, link=link, description=description,
        resource_pic=resource_pic, resource_id=resource_id
    )

    # Assert
    assert updated_resource_dto == actual_resource_dto
