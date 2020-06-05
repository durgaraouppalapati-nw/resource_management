import pytest

from django_swagger_utils.drf_server.exceptions import \
    ExpectationFailed

from resource_management.presenters.presenter_implementation import \
    PresenterImplementation
from resource_management.constants.exception_messages import \
    USER_CAN_NOT_DELETE_REQUEST


def test_raise_user_can_not_delete_request_exception_raise_exception():
    # Arrange
    presenter = PresenterImplementation()
    exception_message = USER_CAN_NOT_DELETE_REQUEST[0]
    res_status = USER_CAN_NOT_DELETE_REQUEST[1]

    # Act
    with pytest.raises(ExpectationFailed) as exception:
        presenter.raise_user_can_not_delete_request_exception()

    # Assert
    assert exception.value.message == exception_message
    assert exception.value.res_status == res_status
