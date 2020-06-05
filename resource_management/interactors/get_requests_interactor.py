from typing import List

from resource_management.interactors.storages.request_interface import \
    RequestInterface
from resource_management.interactors.storages.user_interface import \
    UserInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from resource_management.interactors.storages.dtos import (
    GetRequestsParametersDto, RequestsCountDto, RequestsDetailsDto,
    UserRequestDto
)
from resource_management.constants.exception_messages import (
    INVALID_OFFSET_LENGTH, INVALID_LIMIT_LENGTH    
)


class GetRequestsInteractor:

    def __init__(self, request_storage: RequestInterface,
                 user_storage: UserInterface,
                 presenter: PresenterInterface):
        self.request_storage = request_storage
        self.user_storage = user_storage
        self.presenter = presenter

    def get_requests(self, offset: int, limit: int,
            sortby: str, filterby: str, value: str, user_id: int):
        get_requests_parameters_dto = \
            GetRequestsParametersDto(
                offset=offset,
                limit=limit,
                sortby=sortby,
                filterby=filterby,
                filterby_value=value
            )

        if offset < 0:
            self.presenter.raise_exception_for_invalid_offset_length()
            return

        if limit < 0:
            self.presenter.raise_exception_for_invalid_limit_length()
            return

        is_user_not_admin = \
            not self.user_storage.check_is_user_admin(user_id=user_id)
        if is_user_not_admin:
            self.presenter.raise_exception_for_unauthorized_user()
            return

        total_requests_dto, user_request_dtos = \
            self.request_storage.get_requests(
                get_requests_parameters_dto=get_requests_parameters_dto
            )
        requests_details_dto = self._prepare_requests_details_dto(
            total_requests_dto, user_request_dtos
        )
        return self.presenter.get_response_for_get_requests(
            requests_details_dto=requests_details_dto
        )

    def _prepare_requests_details_dto(self,
            total_requests_dto: RequestsCountDto,
            user_request_dtos: List[UserRequestDto]
            ) -> RequestsDetailsDto:
        request_details_dto = RequestsDetailsDto(
            request_dtos=user_request_dtos,
            requests_count=total_requests_dto
        )
        return request_details_dto
