import pytest

from resource_management.models import ResourceItem
from resource_management.storages.item_storage_implementation import \
    ItemStorageImplementation


@pytest.mark.django_db
def test_delete_resource_items_creates_item(resources, items):
    # Arrange
    item_ids = [1, 2, 3]
    item_storage = ItemStorageImplementation()

    # Act
    item_storage.delete_resource_items(
        item_ids=item_ids
    )

    # Assert
    items = ResourceItem.objects.filter(id__in=item_ids)
    assert len(items) == 0
