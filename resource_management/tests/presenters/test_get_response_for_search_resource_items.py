from resource_management.presenters.presenter_implementation import \
    PresenterImplementation


def test_get_response_for_search_resource_items_return_items_details(
        search_resource_items, search_resource_items_response):
    # Arrange
    presenter = PresenterImplementation()
    expected_output = search_resource_items_response

    # Act
    actual_output = presenter.get_response_for_search_resource_items(
        item_dtos=search_resource_items    
    )

    # Assert
    assert expected_output == actual_output
