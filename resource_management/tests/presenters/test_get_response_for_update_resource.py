import pytest

from resource_management.presenters.presenter_implementation import \
    PresenterImplementation


def test_get_response_for_update_resource_return_resource_dict(
        resource_dto, resource_dict):
    # Arrange
    presenter = PresenterImplementation()
    expected_output = resource_dict

    # Act
    actual_output = presenter.get_response_for_update_resource(resource_dto)

    # Assert
    assert expected_output == actual_output
