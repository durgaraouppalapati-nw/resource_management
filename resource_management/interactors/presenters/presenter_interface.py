from abc import ABC
from abc import abstractmethod

from typing import List

from common.dtos import UserAuthTokensDTO
from resource_management.interactors.storages.dtos import (
    UserDetailsDto, ResourcesDetailsDto, ItemsWithCountDetailsDto,
    UsersWithCountDetailsDto, ResourceDto, UserWithResourceItemsDto,
    UsersDto, RequestsDetailsDto, UserResourceItemsDto,
    RequestsCountDto, RequestStatusDto
)


class PresenterInterface(ABC):

    @abstractmethod
    def raise_password_mismatch_exception(self):
        pass

    @abstractmethod
    def raise_username_already_exists_exception(self):
        pass

    @abstractmethod
    def get_user_details_response(self, user_dto: UserDetailsDto):
        pass

    @abstractmethod
    def raise_exception_for_invalid_credentials(self):
        pass

    @abstractmethod
    def get_response_for_user_signin(self,
            oauth_tokens_dto: UserAuthTokensDTO):
        pass

    @abstractmethod
    def get_response_for_get_all_resources(self,
            resources_details_dto: ResourcesDetailsDto):
        pass

    @abstractmethod
    def get_response_for_get_items_for_resource(self,
            items_with_count_dto: ItemsWithCountDetailsDto):
        pass

    @abstractmethod
    def get_response_for_get_users_for_item(self,
            users_with_count_dto: UsersWithCountDetailsDto):
        pass

    @abstractmethod
    def raise_exception_for_unauthorized_user(self):
        pass

    @abstractmethod
    def raise_exception_for_resource_not_found(self):
        pass

    @abstractmethod
    def get_response_for_update_resource(self, resource_dto: ResourceDto):
        pass

    @abstractmethod
    def raise_exception_for_resource_item_not_found(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_user(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_offset_length(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_limit_length(self):
        pass

    @abstractmethod
    def raise_exception_for_resource_name_already_exists(self):
        pass

    @abstractmethod
    def get_response_for_get_all_users(self, users_dto: UsersDto):
        pass

    @abstractmethod
    def get_response_for_get_all_resource_items_for_user(self,
            user_with_resource_items_dto: UserWithResourceItemsDto):
        pass

    @abstractmethod
    def get_response_for_get_requests(self, 
            requests_details_dto: RequestsDetailsDto):
        pass

    @abstractmethod
    def raise_exception_for_invalid_password(self):
        pass

    @abstractmethod
    def get_response_for_user_resource_items(self,
            user_resource_items_dto: UserResourceItemsDto):
        pass

    @abstractmethod
    def get_response_for_get_user_requests(self,
            requests_details_dto: List[RequestStatusDto],
            requests_count_dto: RequestsCountDto):
        pass

    @abstractmethod
    def get_response_for_search_resources(self, resource_dtos):
        pass

    @abstractmethod
    def get_response_for_search_resource_items(self, item_dtos):
        pass

    @abstractmethod
    def raise_exception_for_request_not_found(self):
        pass

    @abstractmethod
    def raise_user_can_not_delete_request_exception(self):
        pass

    @abstractmethod
    def raise_admin_already_responded_to_request_exception(self):
        pass

    @abstractmethod
    def raise_exception_for_item_not_belongs_to_resource(self):
        pass