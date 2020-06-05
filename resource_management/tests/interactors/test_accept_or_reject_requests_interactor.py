import pytest
from unittest.mock import create_autospec

from django_swagger_utils.drf_server.exceptions import BadRequest

from resource_management.interactors.accept_or_reject_requests_interactor \
    import AcceptOrRejectRequestsInteractor
from resource_management.interactors.storages.request_interface import \
    RequestInterface
from resource_management.interactors.storages.user_interface import \
    UserInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface


def test_accept_or_reject_requests_interactor_with_accept_action():
    # Arrange
    action = "ACCEPTED"
    request_ids = [1, 2, 3],
    reason_for_rejection = ""
    user_id = 1

    request_storage = create_autospec(RequestInterface)
    user_storage = create_autospec(UserInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = AcceptOrRejectRequestsInteractor(
        request_storage=request_storage,
        user_storage=user_storage,
        presenter=presenter
    )
    user_storage.check_is_user_admin.return_value = True

    # Act
    interactor.accept_or_reject_requests(
        action=action, request_ids=request_ids,
        reason_for_rejection=reason_for_rejection,
        user_id=user_id
    )

    # Assert
    user_storage.check_is_user_admin.assert_called_once_with(user_id=user_id)
    request_storage.accept_requests.assert_called_once_with(
        request_ids=request_ids    
    )


def test_accept_or_reject_requests_interactor_with_reject_action():
    # Arrange
    action = "REJECTED"
    request_ids = [1, 2, 3],
    reason_for_rejection = "This is not prefarable for u now"
    user_id = 1

    request_storage = create_autospec(RequestInterface)
    user_storage = create_autospec(UserInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = AcceptOrRejectRequestsInteractor(
        request_storage=request_storage,
        user_storage=user_storage,
        presenter=presenter
    )
    user_storage.check_is_user_admin.return_value = True

    # Act
    interactor.accept_or_reject_requests(
        action=action, request_ids=request_ids,
        reason_for_rejection=reason_for_rejection,
        user_id=user_id
    )

    # Assert
    user_storage.check_is_user_admin.assert_called_once_with(user_id=user_id)
    request_storage.reject_requests.assert_called_once_with(
        request_ids=request_ids, reason_for_rejection=reason_for_rejection
    )


def test_accept_or_reject_requests_interactor_with_user_raise_exception():
    # Arrange
    action = "REJECTED"
    request_ids = [1, 2, 3],
    reason_for_rejection = "This is not prefarable for u now"
    user_id = 1

    request_storage = create_autospec(RequestInterface)
    user_storage = create_autospec(UserInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = AcceptOrRejectRequestsInteractor(
        request_storage=request_storage,
        user_storage=user_storage,
        presenter=presenter
    )
    user_storage.check_is_user_admin.return_value = False
    presenter.raise_exception_for_unauthorized_user.side_effect = BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.accept_or_reject_requests(
            action=action, request_ids=request_ids,
            reason_for_rejection=reason_for_rejection,
            user_id=user_id
        )

    # Assert
    user_storage.check_is_user_admin.assert_called_once_with(user_id=user_id)
    presenter.raise_exception_for_unauthorized_user.assert_called_once()
