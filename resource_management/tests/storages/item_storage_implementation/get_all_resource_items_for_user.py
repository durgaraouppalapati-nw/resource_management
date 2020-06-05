import pytest

from resource_management.storages.item_storage_implementation import \
    ItemStorageImplementation


@pytest.mark.django_db
def test_get_all_resource_items_for_user_with_resource_items_return_dto(
        resource_items, user_with_resource_items_dto):
    # Arrange
    item_storage = ItemStorageImplementation()
    user_id = 1
    offset = 0
    limit = 2
    expected_output = user_with_resource_items_dto

    # Act
    actual_output = item_storage.get_all_resource_items_for_user(
        user_id=user_id, offset=offset, limit=limit    
    )

    # Assert
    assert expected_output == actual_output
