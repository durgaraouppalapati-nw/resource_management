import pytest

from django_swagger_utils.drf_server.exceptions import BadRequest

from resource_management.presenters.presenter_implementation import \
    PresenterImplementation
from resource_management.constants.exception_messages import \
    INVALID_LIMIT_LENGTH


def test_raise_exception_for_invalid_limit_length_raise_invalid_limit_exception():
    # Arrange
    exception_message = INVALID_LIMIT_LENGTH[0]
    res_status = INVALID_LIMIT_LENGTH[1]
    presenter = PresenterImplementation()

    # Act
    with pytest.raises(BadRequest) as exception:
        presenter.raise_exception_for_invalid_limit_length()

    # Assert
    assert exception_message == exception.value.message
    assert res_status == exception.value.res_status
