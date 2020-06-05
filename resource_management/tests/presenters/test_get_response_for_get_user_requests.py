from resource_management.presenters.presenter_implementation import \
    PresenterImplementation


def test_get_response_for_get_user_requests_return_requests_dict(
        user_requests_status_dtos,
        requests_count_dto,
        requests_status_response):
    # Arrange
    presenter = PresenterImplementation()
    expected_output = requests_status_response

    # Act
    actual_output = presenter.get_response_for_get_user_requests(
        requests_count_dto=requests_count_dto,
        requests_details_dto=user_requests_status_dtos
    )

    # Assert
    assert expected_output == actual_output
