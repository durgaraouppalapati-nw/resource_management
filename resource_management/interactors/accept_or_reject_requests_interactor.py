from typing import List

from resource_management.interactors.storages.request_interface import \
    RequestInterface
from resource_management.interactors.storages.user_interface import \
    UserInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from resource_management.constants.enums import Confirmation


class AcceptOrRejectRequestsInteractor:

    def __init__(self, request_storage: RequestInterface,
                 user_storage: UserInterface,
                 presenter: PresenterInterface):
        self.request_storage = request_storage
        self.user_storage = user_storage
        self.presenter = presenter

    def accept_or_reject_requests(self, action: str,
            request_ids: List[int], reason_for_rejection: str, user_id: int):

        is_user_not_admin = \
            not self.user_storage.check_is_user_admin(user_id=user_id)
        if is_user_not_admin:
            self.presenter.raise_exception_for_unauthorized_user()
            return

        if action == Confirmation.ACCEPT.value:
            self.request_storage.accept_requests(request_ids)
        else:
            self.request_storage.reject_requests(
                request_ids, reason_for_rejection    
            )
        return
