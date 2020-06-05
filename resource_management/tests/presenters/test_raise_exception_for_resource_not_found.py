import pytest

from django_swagger_utils.drf_server.exceptions import NotFound

from resource_management.presenters.presenter_implementation import \
    PresenterImplementation
from resource_management.constants.exception_messages import \
    INVALID_RESOURCE_ID


def test_raise_exception_for_invalid_resource_raise_exception():
    # Arrange
    exception_message = INVALID_RESOURCE_ID[0]
    res_status = INVALID_RESOURCE_ID[1]
    presenter = PresenterImplementation()

    # Act
    with pytest.raises(NotFound) as exception:
        presenter.raise_exception_for_resource_not_found()

    # Assert
    assert exception.value.message == exception_message
    assert exception.value.res_status == res_status
