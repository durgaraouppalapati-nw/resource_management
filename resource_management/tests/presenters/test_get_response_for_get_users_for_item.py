from resource_management.presenters.presenter_implementation import \
    PresenterImplementation


def test_get_response_for_get_users_for_item_retrun_users_dto_dict(
        users_with_count_dto, get_users_for_item_response):
    # Arrange
    presenter = PresenterImplementation()
    expected_output = get_users_for_item_response

    # Act
    actual_output = presenter.get_response_for_get_users_for_item(
        users_with_count_dto=users_with_count_dto    
    )

    # Assert
    assert expected_output == actual_output
