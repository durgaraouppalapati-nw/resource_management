from resource_management.presenters.presenter_implementation import \
    PresenterImplementation


def test_get_response_for_get_users_return_users_details_dict(
        users_response, users_dto):
    # Arrange
    presenter = PresenterImplementation()
    expected_output = users_response

    # Act
    actual_output = presenter.get_response_for_get_all_users(
        users_dto=users_dto    
    )

    # Assert
    assert expected_output == actual_output
