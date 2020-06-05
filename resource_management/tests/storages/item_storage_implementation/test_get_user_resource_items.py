import pytest

from resource_management.storages.item_storage_implementation import \
    ItemStorageImplementation


@pytest.mark.django_db
def test_get_user_resource_items_without_search_return_resource_items(
        resource_items_access, user_resource_items_dto):
    # Arrange
    user_id = 1
    offset = 0
    limit = 10
    search = ""
    expected_output = user_resource_items_dto
    item_storage = ItemStorageImplementation()

    # Act
    actual_output = item_storage.get_user_resource_items(
        user_id=user_id, offset=offset, limit=limit, search=search
    )

    # Assert
    assert expected_output == actual_output


@pytest.mark.django_db
def test_get_user_resource_items_with_searchby_resource_name_return_resource_items(
        resource_items_access, user_resource_items_dto_searchby_resource):
    # Arrange
    user_id = 1
    offset = 0
    limit = 10
    search = "github"
    expected_output = user_resource_items_dto_searchby_resource
    item_storage = ItemStorageImplementation()

    # Act
    actual_output = item_storage.get_user_resource_items(
        user_id=user_id, offset=offset, limit=limit, search=search
    )

    # Assert
    assert expected_output == actual_output


@pytest.mark.django_db
def test_get_user_resource_items_with_searchby_item_title_return_resource_items(
        resource_items_access, user_resource_items_dto_searchby_item_title):
    # Arrange
    user_id = 1
    offset = 0
    limit = 10
    search = "forms"
    expected_output = user_resource_items_dto_searchby_item_title
    item_storage = ItemStorageImplementation()

    # Act
    actual_output = item_storage.get_user_resource_items(
        user_id=user_id, offset=offset, limit=limit, search=search
    )

    # Assert
    assert expected_output == actual_output


@pytest.mark.django_db
def test_get_user_resource_items_with_searchby_access_level_return_resource_items(
        resource_items_access, user_resource_items_dto_searchby_access_level):
    # Arrange
    user_id = 1
    offset = 0
    limit = 10
    search = "WRITE"
    expected_output = user_resource_items_dto_searchby_access_level
    item_storage = ItemStorageImplementation()

    # Act
    actual_output = item_storage.get_user_resource_items(
        user_id=user_id, offset=offset, limit=limit, search=search
    )

    # Assert
    assert expected_output == actual_output


@pytest.mark.django_db
def test_get_user_resource_items_with_searchby_resource_and_item_return_resource_items(
        resource_items_access, user_resource_items_dto_searchby_common):
    # Arrange
    user_id = 1
    offset = 0
    limit = 10
    search = "bucket"
    expected_output = user_resource_items_dto_searchby_common
    item_storage = ItemStorageImplementation()

    # Act
    actual_output = item_storage.get_user_resource_items(
        user_id=user_id, offset=offset, limit=limit, search=search
    )

    # Assert
    assert expected_output == actual_output


@pytest.mark.django_db
def test_get_user_resource_items_with_searchby_unknown_return_empty(
        resource_items_access, user_resource_items_dto_searchby_unknown):
    # Arrange
    user_id = 1
    offset = 0
    limit = 10
    search = "superuser"
    expected_output = user_resource_items_dto_searchby_unknown
    item_storage = ItemStorageImplementation()

    # Act
    actual_output = item_storage.get_user_resource_items(
        user_id=user_id, offset=offset, limit=limit, search=search
    )

    # Assert
    assert expected_output == actual_output
