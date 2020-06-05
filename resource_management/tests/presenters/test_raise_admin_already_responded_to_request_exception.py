import pytest

from django_swagger_utils.drf_server.exceptions import \
    ExpectationFailed

from resource_management.presenters.presenter_implementation import \
    PresenterImplementation
from resource_management.constants.exception_messages import \
    ADMIN_ALREADY_RESPONDED


def test_raise_admin_already_responded_to_request_exception_raises_exception():
    # Arrange
    presenter = PresenterImplementation()
    exception_message = ADMIN_ALREADY_RESPONDED[0]
    res_status = ADMIN_ALREADY_RESPONDED[1]

    # Act
    with pytest.raises(ExpectationFailed) as exception:
        presenter.raise_admin_already_responded_to_request_exception()

    # Assert
    assert exception.value.message == exception_message
    assert exception.value.res_status == res_status
