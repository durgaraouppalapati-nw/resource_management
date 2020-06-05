from resource_management.presenters.presenter_implementation import \
    PresenterImplementation


def test_get_response_for_search_resources_return_resources_details(
        search_resources, search_resources_response):
    # Arrange
    presenter = PresenterImplementation()
    expected_output = search_resources_response

    # Act
    actual_output = presenter.get_response_for_search_resources(
        resource_dtos=search_resources    
    )

    # Assert
    assert expected_output == actual_output
