import pytest

from django_swagger_utils.drf_server.exceptions import BadRequest

from resource_management.constants.exception_messages import \
    INVALID_CREDENTIALS
from resource_management.presenters.presenter_implementation import \
    PresenterImplementation


def test_raise_exception_for_invalid_credentials_raise_exception():
    # Arrange
    exception_messages = INVALID_CREDENTIALS[0]
    exception_res_status =  INVALID_CREDENTIALS[1]
    presenter = PresenterImplementation()

    # Act
    with pytest.raises(BadRequest) as exception:
        presenter.raise_exception_for_invalid_credentials()

    # Assert
    assert exception.value.message == exception_messages
    assert exception.value.res_status == exception_res_status
