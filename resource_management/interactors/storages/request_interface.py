from abc import abstractmethod
from typing import List

from resource_management.interactors.storages.dtos import (
    UserRequestDto, RequestsCountDto, GetRequestsParametersDto,
    RequestDto
)


class RequestInterface:

    @abstractmethod
    def get_requests(self,
        get_requests_parameters_dto: GetRequestsParametersDto):
        pass

    @abstractmethod
    def accept_requests(self, request_ids: List[int]):
        pass

    @abstractmethod
    def reject_requests(self, request_ids: List[int],
            reason_for_rejection: str):
        pass

    @abstractmethod
    def get_user_requests(self, user_id: int,
            requests_parameters_dto: GetRequestsParametersDto
            ):
        pass

    @abstractmethod
    def check_is_request_exists(self, request_id: int) -> bool:
        pass

    @abstractmethod
    def check_is_user_creator_of_request(self, user_id: int,
            request_id: int) -> bool:
        pass

    @abstractmethod
    def check_is_admin_responded_to_request(self, request_id: int) -> bool:
        pass

    @abstractmethod
    def delete_request(self, request_id: int):
        pass

    @abstractmethod
    def create_request(self, user_id: int, request_dto: RequestDto):
        pass
