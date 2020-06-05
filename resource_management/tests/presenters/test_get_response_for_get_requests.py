import pytest

from resource_management.presenters.presenter_implementation import \
    PresenterImplementation


def test_get_response_for_get_requests_return_requests_details_response(
        requests_details_dto, requests_details_response):
    # Arrange
    presenter = PresenterImplementation()
    expected_output = requests_details_response

    # Act
    actual_output = presenter.get_response_for_get_requests(
        requests_details_dto=requests_details_dto    
    )

    # Assert
    assert expected_output == actual_output
