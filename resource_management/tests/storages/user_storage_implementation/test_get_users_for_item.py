import pytest

from resource_management.storages.user_implementation import \
    UserImplementation


@pytest.mark.django_db
def test_get_users_for_item_with_users_return_users_dto(
        users, items, resource_items, users_with_count_dto):
    # Arrange
    user_storage = UserImplementation()
    expected_dto = users_with_count_dto
    item_id = 1
    offset = 0
    limit = 2

    # Act
    actual_dto = user_storage.get_users_for_item(
        item_id=item_id, offset=offset, limit=limit    
    )

    # Assert
    assert expected_dto == actual_dto
