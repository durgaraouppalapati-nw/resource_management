from resource_management.presenters.presenter_implementation import \
    PresenterImplementation
from resource_management.interactors.storages.dtos import \
    ResourcesDetailsDto, ResourcesCountDto


def test_get_response_for_get_all_resources_return_resoures_dict(
        resource_dtos, resources_count_dto, resource_dtos_response):
    # Arrange
    expected_output = resource_dtos_response
    presenter = PresenterImplementation()

    resource_details_dto = ResourcesDetailsDto(
        resource_dtos=resource_dtos,
        resources_count_dto=resources_count_dto
    )

    # Act
    actual_output = presenter.get_response_for_get_all_resources(
        resources_details_dto=resource_details_dto
    )

    # Assert
    assert expected_output == actual_output


def test_get_response_for_get_all_resources_without_resources_return_empty():
    # Arrange
    expected_output = {
        "total_resources": 0,
        "resources_details": []
    }
    presenter = PresenterImplementation()

    resource_details_dto = ResourcesDetailsDto(
        resource_dtos=[],
        resources_count_dto=ResourcesCountDto(resources_count=0)
    )

    # Act
    actual_output = presenter.get_response_for_get_all_resources(
        resources_details_dto=resource_details_dto
    )

    # Assert
    assert expected_output == actual_output
