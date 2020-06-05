from resource_management.presenters.presenter_implementation import \
    PresenterImplementation


def test_get_response_for_user_resource_items_return_items_dict(
        user_resource_items_dto, user_resource_items_response):
    # Arrange
    expected_output = user_resource_items_response
    presenter = PresenterImplementation()

    # Act
    actual_output = presenter.get_response_for_user_resource_items(
        user_resource_items_dto=user_resource_items_dto    
    )

    # Assert
    assert expected_output == actual_output
