import pytest

from resource_management.models import ResourceItem
from resource_management.storages.item_storage_implementation import \
    ItemStorageImplementation


@pytest.mark.django_db
def test_create_resource_item_creates_item(resource):
    # Arrange
    resource_id = 1
    title = "Item 1"
    link = "www.item1.com"
    description = "This is about item 1"
    item_storage = ItemStorageImplementation()

    # Act
    item_storage.create_resource_item(
        title=title,
        link=link,
        description=description,
        resource_id=resource_id
    )

    # Assert
    item = ResourceItem.objects.get(title=title)
    assert item.link == link
    assert item.description == description
    assert item.resource_id == resource_id
