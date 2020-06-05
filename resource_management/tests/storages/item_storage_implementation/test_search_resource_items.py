import pytest

from resource_management.storages.item_storage_implementation import \
    ItemStorageImplementation


@pytest.mark.django_db
def test_search_resource_items_with_individual_name_return_resource_item(
        create_resource_items, serach_resource_items_by_individual_name):
    # Arrange
    resource_id = 4
    search = "cloud9"
    item_storage = ItemStorageImplementation()
    expected_output = serach_resource_items_by_individual_name

    # Act
    actual_output = item_storage.search_resource_items(
        resource_id=resource_id, search=search
    )

    # Assert
    assert expected_output == actual_output


@pytest.mark.django_db
def test_search_resource_items_with_common_name_return_resource_items(
        create_resource_items, search_resouce_items_by_common_name):
    # Arrange
    resource_id = 4
    search = "o"
    item_storage = ItemStorageImplementation()
    expected_output = search_resouce_items_by_common_name

    # Act
    actual_output = item_storage.search_resource_items(
        resource_id=resource_id, search=search
    )

    # Assert
    assert expected_output == actual_output


@pytest.mark.django_db
def test_search_resource_items_with_unknown_name_return_empty(
        create_resource_items, search_resouce_items_by_unknown_name):
    # Arrange
    resource_id = 4
    search = "Covid19"
    item_storage = ItemStorageImplementation()
    expected_output = search_resouce_items_by_unknown_name

    # Act
    actual_output = item_storage.search_resource_items(
        resource_id=resource_id, search=search
    )

    # Assert
    assert expected_output == actual_output
