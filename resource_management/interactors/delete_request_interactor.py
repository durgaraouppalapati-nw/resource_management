from resource_management.interactors.storages.request_interface import \
    RequestInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface


class DeleteRequestIntercator:

    def __init__(self, request_storage: RequestInterface,
                 presenter: PresenterInterface):
        self.request_storage = request_storage
        self.presenter = presenter

    def delete_request(self, request_id: int, user_id: int):
        is_request_not_exists = \
            not self.request_storage.check_is_request_exists(
                request_id=request_id
            )
        if is_request_not_exists:
            self.presenter.raise_exception_for_request_not_found()
            return

        is_creator_of_request_and_given_user_not_same = \
            not self.request_storage.check_is_user_creator_of_request(
                user_id=user_id, request_id=request_id    
            )
        if is_creator_of_request_and_given_user_not_same:
            self.presenter.raise_user_can_not_delete_request_exception()
            return

        is_admin_responded_to_request = \
            self.request_storage.check_is_admin_responded_to_request(
                request_id=request_id    
            )
        if is_admin_responded_to_request:
            self.presenter.raise_admin_already_responded_to_request_exception()
            return

        self.request_storage.delete_request(request_id=request_id)
        return
