import pytest

from resource_management.storages.item_storage_implementation import \
    ItemStorageImplementation
from resource_management.models import AccessLevel


@pytest.mark.django_db
def test_add_item_to_user_adds_resource_item_to_user(resource_items):
    # Arrange
    user_id = 1
    item_id = 2
    access_level = "READ"
    expected_output = True

    item_storage = ItemStorageImplementation()

    # Act
    item_storage.add_resource_item_to_user(
        item_id=item_id, user_id=user_id, access_level=access_level    
    )

    # Assert
    actual_output = AccessLevel.objects.filter(user_id=user_id,
                                               resource_item_id=item_id,
                                               access_level=access_level
                                              )\
                                              .exists()
    assert expected_output == actual_output
  