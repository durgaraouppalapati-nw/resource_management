import pytest

from resource_management.models import ResourceItem
from resource_management.storages.item_storage_implementation import \
    ItemStorageImplementation


@pytest.mark.django_db
def test_check_resource_item_exists_with_items_return_true(resources, items):
    # Arrange
    item_id = 1
    expected_output = True
    item_storage = ItemStorageImplementation()

    # Act
    actual_output = item_storage.check_is_resource_item_exists(
        item_id=item_id
    )

    # Assert
    assert expected_output == actual_output
