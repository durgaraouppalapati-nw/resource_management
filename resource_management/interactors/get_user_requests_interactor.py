from resource_management.interactors.storages.user_interface import \
    UserInterface
from resource_management.interactors.storages.request_interface import \
    RequestInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from resource_management.interactors.storages.dtos import \
    GetRequestsParametersDto


class GetUserRequestsInteractor:

    def __init__(self, user_storage: UserInterface,
                 request_storage: RequestInterface,
                 presenter: PresenterInterface
                ):
        self.user_storage = user_storage
        self.request_storage = request_storage
        self.presenter = presenter

    def get_user_requests(self, user_id: int,
            requests_parameters_dto: GetRequestsParametersDto):
        offset = requests_parameters_dto.offset
        limit = requests_parameters_dto.limit

        if offset < 0:
            self.presenter.raise_exception_for_invalid_offset_length()
            return

        if limit < 0:
            self.presenter.raise_exception_for_invalid_limit_length()
            return

        is_user_not_exists = \
            not self.user_storage.check_is_user_exists(user_id=user_id)
        if is_user_not_exists:
            self.presenter.raise_exception_for_invalid_user()
            return

        total_requests_dto, requests_details_dto = \
            self.request_storage.get_user_requests(
                user_id, requests_parameters_dto
            )
        return self.presenter.get_response_for_get_user_requests(
            requests_details_dto=requests_details_dto,
            requests_count_dto=total_requests_dto
        )
