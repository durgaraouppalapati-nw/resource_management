import pytest

from resource_management.models import ResourceItem
from resource_management.storages.item_storage_implementation import \
    ItemStorageImplementation


@pytest.mark.django_db
def test_update_resource_item_creates_item(resources, items):
    # Arrange
    item_id = 1
    title = "item_1"
    link = "www.item_1.com"
    description = "This is about item_1"
    item_storage = ItemStorageImplementation()

    # Act
    item_storage.update_resource_item(
        title=title,
        link=link,
        description=description,
        item_id=item_id
    )

    # Assert
    item = ResourceItem.objects.get(id=item_id)
    assert item.link == link
    assert item.description == description
    assert item.title == title
