import pytest

from django_swagger_utils.drf_server.exceptions import \
    NotFound, ExpectationFailed

from resource_management.presenters.presenter_implementation import \
    PresenterImplementation
from resource_management.constants.exception_messages import \
    INVALID_REQUEST_ID


def test_raise_exception_for_request_not_found_raise_invalid_request_id_exception():
    # Arrange
    presenter = PresenterImplementation()
    exception_message = INVALID_REQUEST_ID[0]
    res_status = INVALID_REQUEST_ID[1]

    # Act
    with pytest.raises(NotFound) as exception:
        presenter.raise_exception_for_request_not_found()

    # Assert
    assert exception.value.message == exception_message
    assert exception.value.res_status == res_status
