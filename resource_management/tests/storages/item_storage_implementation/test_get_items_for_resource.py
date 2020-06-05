import pytest

from resource_management.storages.item_storage_implementation import \
    ItemStorageImplementation
from resource_management.interactors.storages.dtos import \
    ItemsWithCountDetailsDto


@pytest.mark.django_db
def test_get_items_for_resource_with_items_return_items_with_count_dto(
        items, item_dtos, resource_dto, items_count_dto):
    # Arrange
    item_storage = ItemStorageImplementation()
    resource_id = 1
    offset = 0
    limit = 2

    expected_output = ItemsWithCountDetailsDto(
        items_count_dto=items_count_dto,
        item_dtos=item_dtos,
        resource_dto=resource_dto
    )

    # Act
    actual_output = item_storage.get_items_for_resource(
        resource_id=resource_id, offset=offset, limit=limit
    )

    # Assert
    assert expected_output == actual_output


@pytest.mark.django_db
def test_get_items_for_resource_with_no_items_return_empty(
        resource, resource_dto, items_zro_count_dto):
    # Arrange
    item_storage = ItemStorageImplementation()
    resource_id = 1
    offset = 0
    limit = 10

    expected_output = ItemsWithCountDetailsDto(
        items_count_dto=items_zro_count_dto,
        item_dtos=[],
        resource_dto=resource_dto
    )

    # Act
    actual_output = item_storage.get_items_for_resource(
        resource_id=resource_id, offset=offset, limit=limit
    )

    # Assert
    assert expected_output == actual_output
