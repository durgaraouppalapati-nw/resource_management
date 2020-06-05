import pytest

from django_swagger_utils.drf_server.exceptions import Unauthorized

from resource_management.presenters.presenter_implementation import \
    PresenterImplementation
from resource_management.constants.exception_messages import UNAUTHORIZED_USER


def test_raise_exception_for_unauthorized_user_raise_exception():
    # Arrange
    exception_message = UNAUTHORIZED_USER[0]
    res_status = UNAUTHORIZED_USER[1]
    presenter = PresenterImplementation()

    # Act
    with pytest.raises(Unauthorized) as exception:
        presenter.raise_exception_for_unauthorized_user()

    # Assert
    assert exception.value.message == exception_message
    assert exception.value.res_status == res_status
