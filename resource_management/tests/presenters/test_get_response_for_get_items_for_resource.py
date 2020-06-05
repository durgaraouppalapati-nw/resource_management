from resource_management.presenters.presenter_implementation import \
    PresenterImplementation
from resource_management.interactors.storages.dtos import (
    ResourcesDetailsDto, ItemsWithCountDetailsDto
)


def test_get_response_for_get_items_for_resource_return_items(
        item_dtos, resource_dto, items_count_dto, item_dtos_response):
    # Arrange
    presenter = PresenterImplementation()
    items_with_count_dto = ItemsWithCountDetailsDto(
        item_dtos=item_dtos,
        items_count_dto=items_count_dto,
        resource_dto=resource_dto
    )
    expected_output = item_dtos_response

    # Act
    actual_output = presenter.get_response_for_get_items_for_resource(
        items_with_count_dto=items_with_count_dto    
    )

    # Assert
    assert expected_output == actual_output
