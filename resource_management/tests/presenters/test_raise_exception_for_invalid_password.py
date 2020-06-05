import pytest

from django_swagger_utils.drf_server.exceptions import ExpectationFailed

from resource_management.presenters.presenter_implementation import \
    PresenterImplementation
from resource_management.constants.exception_messages import INVALID_PASSWORD


def test_raise_exception_for_invalid_password_raises_exception():
    # Arrange
    presenter = PresenterImplementation()
    exception_message = INVALID_PASSWORD[0]
    res_status = INVALID_PASSWORD[1]

    # Act
    with pytest.raises(ExpectationFailed) as exception:
        presenter.raise_exception_for_invalid_password()

    # Assert
    assert exception_message == exception.value.message
    assert res_status == exception.value.res_status
