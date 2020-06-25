from django_swagger_utils.drf_server.exceptions import (
    BadRequest, NotFound, Forbidden, ExpectationFailed, Unauthorized
)

from typing import List

from common.dtos import UserAuthTokensDTO
from resource_management.interactors.presenters.presenter_interface \
    import PresenterInterface
from resource_management.interactors.storages.dtos import (
    UserDetailsDto, ResourcesDetailsDto, ItemsWithCountDetailsDto,
    UsersWithCountDetailsDto, ResourceDto, UsersDto,
    UserWithResourceItemsDto, ResourceItemDto, UserDto,
    RequestsDetailsDto, UserRequestDto, ItemsCountDto,
    UsersCountDto, UserResourceItemsDto, RequestStatusDto,
    RequestsCountDto
)
from resource_management.constants.exception_messages import (
    INVALID_CREDENTIALS, UNAUTHORIZED_USER, INVALID_RESOURCE_ID,
    INVALID_RESOURCE_ITEM_ID, INVALID_USER_ID, INVALID_OFFSET_LENGTH,
    INVALID_LIMIT_LENGTH, PASSWORD_MISMATCH, USERNAME_ALREADY_EXISTS,
    RESOURCE_NAME_ALREADY_EXISTS, INVALID_PASSWORD, INVALID_REQUEST_ID,
    USER_CAN_NOT_DELETE_REQUEST, ADMIN_ALREADY_RESPONDED,
    ITEM_DOES_NOT_BELONG_TO_RESOURCE
)
from resource_management.constants.constants import DEFAULT_DATE_TIME_FORMAT


class PresenterImplementation(PresenterInterface):

    def raise_password_mismatch_exception(self):
        raise ExpectationFailed(*PASSWORD_MISMATCH)

    def raise_username_already_exists_exception(self):
        raise ExpectationFailed(*USERNAME_ALREADY_EXISTS)

    def get_user_details_response(self, user_dto: UserDetailsDto):
        user_details_dict = {
            "name": user_dto.name,
            "profile_pic": user_dto.profile_pic,
            "job_role": user_dto.job_role,
            "department": user_dto.department,
            "gender": user_dto.gender
        }
        return user_details_dict

    def raise_exception_for_invalid_credentials(self):
        raise BadRequest(*INVALID_CREDENTIALS)

    def get_response_for_user_signin(self,
                                     oauth_tokens_dto: UserAuthTokensDTO):
        oauth_tokens_dict = {
            "access_token": oauth_tokens_dto.access_token,
        }
        return oauth_tokens_dict

    def get_response_for_get_all_resources(self,
                                           resources_details_dto: ResourcesDetailsDto):
        resource_dtos = resources_details_dto.resource_dtos
        resources_count_dto = resources_details_dto.resources_count_dto

        resources_dict_list = [
            self._convert_resource_dto_to_dict(resource_dto)
            for resource_dto in resource_dtos
        ]
        resources_deatils_with_count_dict = \
            self._prepare_resources_deatils_with_count_dict(
                resources_count_dto, resources_dict_list
            )
        return resources_deatils_with_count_dict

    def _convert_resource_dto_to_dict(self, resource_dto):
        resource_dict = {
            "name": resource_dto.name,
            "resource_pic": resource_dto.resource_pic,
            "link": resource_dto.link,
            "description": resource_dto.description,
            "resource_id": resource_dto.resource_id
        }
        return resource_dict

    def _prepare_resources_deatils_with_count_dict(self,
                                                   resources_count_dto, resources_dict_list):
        resources_with_count = {
            "total_resources": resources_count_dto.resources_count,
            "resources_details": resources_dict_list
        }
        return resources_with_count

    def get_response_for_get_items_for_resource(self,
                                                items_with_count_dto: ItemsWithCountDetailsDto):
        items_count_dto = items_with_count_dto.items_count_dto
        item_dtos = items_with_count_dto.item_dtos
        resource_dto = items_with_count_dto.resource_dto

        items_dict_list = [
            self._convert_item_dto_to_dict(item_dto)
            for item_dto in item_dtos
        ]
        resource_dict = self._convert_resource_dto_to_dict(resource_dto)
        items_with_count_dict = \
            self._prepare_items_with_count_dict(
                items_count_dto, items_dict_list, resource_dict
            )

        return items_with_count_dict

    def _convert_item_dto_to_dict(self, item_dto):
        item_dict = {
            "title": item_dto.title,
            "link": item_dto.link,
            "description": item_dto.description,
            "item_id": item_dto.item_id
        }
        return item_dict

    @staticmethod
    def _prepare_items_with_count_dict(items_count_dto,
                                       items_dict_list,
                                       resource_dict):
        items_with_count_dict = {
            "total_items": items_count_dto.items_count,
            "resource": resource_dict,
            "items": items_dict_list
        }
        return items_with_count_dict

    def get_response_for_get_users_for_item(self,
                                            users_with_count_dto: UsersWithCountDetailsDto):
        users_count_dto = users_with_count_dto.users_count_dto
        user_dtos = users_with_count_dto.user_dtos

        users_dict_list = [
            self._convert_user_with_access_level_dto_dict(user_dto)
            for user_dto in user_dtos
        ]
        users_with_count_dict = \
            self._prepare_users_with_count_dict(
                users_count_dto, users_dict_list
            )

        return users_with_count_dict

    @staticmethod
    def _convert_user_with_access_level_dto_dict(user_dto):
        user_dict = {
            "name": user_dto.name,
            "job_role": user_dto.job_role,
            "department": user_dto.department,
            "access_level": user_dto.access_level
        }
        return user_dict

    def _prepare_users_with_count_dict(
            self, users_count_dto, users_dict_list):
        users_with_count_dict = {
            "total_users": users_count_dto.users_count,
            "users": users_dict_list
        }
        return users_with_count_dict

    def raise_exception_for_unauthorized_user(self):
        raise Unauthorized(*UNAUTHORIZED_USER)

    def raise_exception_for_resource_not_found(self):
        raise NotFound(*INVALID_RESOURCE_ID)

    def raise_exception_for_invalid_offset_length(self):
        raise BadRequest(*INVALID_OFFSET_LENGTH)

    def raise_exception_for_invalid_limit_length(self):
        raise BadRequest(*INVALID_LIMIT_LENGTH)

    def raise_exception_for_resource_name_already_exists(self):
        raise ExpectationFailed(*RESOURCE_NAME_ALREADY_EXISTS)

    def get_response_for_update_resource(self, resource_dto: ResourceDto):
        resource_dict = self._convert_resource_dto_to_dict(resource_dto)
        return resource_dict

    def raise_exception_for_resource_item_not_found(self):
        raise NotFound(*INVALID_RESOURCE_ITEM_ID)

    def raise_exception_for_invalid_user(self):
        raise NotFound(*INVALID_USER_ID)

    def get_response_for_get_all_users(self, users_dto: UsersDto):
        user_dtos = users_dto.user_dtos
        users_count_dto = users_dto.users_count_dto

        users_dict = [
            self._prepare_user_details_dict(user)
            for user in user_dtos
        ]
        users_details_with_count = \
            self._prepare_users_details_with_count(
                users_details=users_dict, users_count_dto=users_count_dto
            )
        return users_details_with_count

    def _prepare_users_details_with_count(self,
                                          users_details,
                                          users_count_dto: UsersCountDto):
        users_details = {
            "total_users": users_count_dto.users_count,
            "users_details": users_details
        }
        return users_details

    def get_response_for_get_all_resource_items_for_user(self,
                                                         user_with_resource_items_dto: UserWithResourceItemsDto):
        items_count_dto = user_with_resource_items_dto.items_count_dto
        user_dto = user_with_resource_items_dto.user_dto
        resource_items = user_with_resource_items_dto.resource_items

        user_dict = self._prepare_user_dict_from_user_dto(user_dto)
        resource_items_list = [
            self._prepare_resource_item_dict_from_dto(resource_item)
            for resource_item in resource_items
        ]

        return self._prepare_user_with_resource_items_dict(
            items_count_dto, user_dict, resource_items_list
        )

    def get_response_for_get_requests(self,
                                      requests_details_dto: RequestsDetailsDto):
        request_dtos = requests_details_dto.request_dtos
        requests_count_dto = requests_details_dto.requests_count

        requests_dict = [
            self._prepeare_user_with_request_details_dict(request)
            for request in request_dtos
        ]
        return self._prepare_requests_dict_with_total_requests(
            requests_count_dto, requests_dict
        )

    def _prepeare_user_with_request_details_dict(self, request):
        request_dict = {
            'resource_name': request.resource_name,
            'request_id': request.request_id,
            'item_title': request.item_title,
            'access_level': request.access_level,
            'user_name': request.user_name,
            'profile_pic': request.profile_pic,
            'due_datetime': self._get_date_time_format(request.due_datetime)
        }
        return request_dict

    @staticmethod
    def _get_date_time_format(datetime):
        return datetime.strftime(DEFAULT_DATE_TIME_FORMAT)

    def _prepare_requests_dict_with_total_requests(
            self, requests_count_dto, requests_dict):
        return {
            "total_requests": requests_count_dto.requests_count,
            "requests_details": requests_dict
        }

    def _prepare_user_details_dict(self, user):
        user_dict = {
            'name': user.name,
            'profile_pic': user.profile_pic,
            'job_role': user.job_role,
            'department': user.department,
            'user_id': user.user_id
        }
        return user_dict

    def _prepare_resource_item_dict_from_dto(self,
                                             resource_item: ResourceItemDto):
        resource_item_dict = {
            'resource_name': resource_item.resource_name,
            'item_title': resource_item.item_title,
            'access_level': resource_item.access_level,
            'link': resource_item.link,
            'description': resource_item.description,
            'item_id': resource_item.item_id
        }
        return resource_item_dict

    def _prepare_user_dict_from_user_dto(self, user_dto: UserDto):
        user_dict = {
            "name": user_dto.name,
            "profile_pic": user_dto.profile_pic,
            "job_role": user_dto.job_role,
            "department": user_dto.department,
            "user_id": user_dto.user_id
        }
        return user_dict

    def _prepare_user_with_resource_items_dict(self,
                                               items_count_dto: ItemsCountDto,
                                               user_dict,
                                               resource_items_list):
        user_resource_items_dict = {
            'total_items': items_count_dto.items_count,
            'user_details': user_dict,
            'resource_items': resource_items_list
        }
        return user_resource_items_dict

    def raise_exception_for_invalid_password(self):
        raise ExpectationFailed(*INVALID_PASSWORD)

    def get_response_for_user_resource_items(self,
                                             user_resource_items_dto: UserResourceItemsDto):
        items_count_dto = user_resource_items_dto.items_count_dto
        resource_items = user_resource_items_dto.resource_items

        resource_items_list = [
            self._prepare_resource_item_dict(resource_item)
            for resource_item in resource_items
        ]

        return self._prepare_user_resource_items_dict(
            items_count_dto, resource_items_list
        )

    def _prepare_resource_item_dict(self,
                                    resource_item: ResourceItemDto):
        resource_item_dict = {
            'resource_name': resource_item.resource_name,
            'item_title': resource_item.item_title,
            'access_level': resource_item.access_level,
            'link': resource_item.link,
            'item_id': resource_item.item_id
        }
        return resource_item_dict

    def _prepare_user_resource_items_dict(self,
                                          items_count_dto: ItemsCountDto,
                                          resource_items_list):
        user_resource_items_dict = {
            'total_resource_items': items_count_dto.items_count,
            'resource_items': resource_items_list
        }
        return user_resource_items_dict

    def get_response_for_get_user_requests(self,
                                           requests_details_dto: List[RequestStatusDto],
                                           requests_count_dto: RequestsCountDto):
        requests_details = [
            self._prepare_request_status_dict(request_dto)
            for request_dto in requests_details_dto
        ]

        return {
            "total_requests": requests_count_dto.requests_count,
            "requests_details": requests_details
        }

    def _prepare_request_status_dict(self, request_dto):
        request_staus_dict = {
            "request_id": request_dto.request_id,
            "resource_name": request_dto.resource_name,
            "item_title": request_dto.item_title,
            "access_level": request_dto.access_level,
            "status": request_dto.status
        }
        return request_staus_dict

    def get_response_for_search_resources(self, resource_dtos):
        resources_details = [
            self._prepare_resource_minimal_details_dict(resource_dto)
            for resource_dto in resource_dtos
        ]
        return resources_details

    @staticmethod
    def _prepare_resource_minimal_details_dict(resource_dto):
        return {
            "resource_id": resource_dto.resource_id,
            "resource_name": resource_dto.name
        }

    def get_response_for_search_resource_items(self, item_dtos):
        items_details = [
            self._prepare_resource_item_minimal_details_dict(item_dto)
            for item_dto in item_dtos
        ]
        return items_details

    @staticmethod
    def _prepare_resource_item_minimal_details_dict(item_dto):
        return {
            "item_id": item_dto.item_id,
            "item_title": item_dto.title
        }

    def raise_exception_for_request_not_found(self):
        raise NotFound(*INVALID_REQUEST_ID)

    def raise_user_can_not_delete_request_exception(self):
        raise ExpectationFailed(*USER_CAN_NOT_DELETE_REQUEST)

    def raise_admin_already_responded_to_request_exception(self):
        raise ExpectationFailed(*ADMIN_ALREADY_RESPONDED)

    def raise_exception_for_item_not_belongs_to_resource(self):
        raise ExpectationFailed(*ITEM_DOES_NOT_BELONG_TO_RESOURCE)
