from typing import List

from django.db.models import Q

from resource_management.models import Request, AccessLevel
from resource_management.interactors.storages.request_interface import \
    RequestInterface
from resource_management.interactors.storages.dtos import (
    RequestsCountDto, RequestsDetailsDto,
    GetRequestsParametersDto, UserRequestDto,
    RequestStatusDto, RequestDto
)
from resource_management.constants.enums import (
    Confirmation, SortRequests, FilterRequests
)


class RequestStorageImplementation(RequestInterface):

    def get_requests(self,
            get_requests_parameters_dto: GetRequestsParametersDto
            ) -> RequestsDetailsDto:
        filterby = get_requests_parameters_dto.filterby
        sortby = get_requests_parameters_dto.sortby
        filterby_value = get_requests_parameters_dto.filterby_value
        offset = get_requests_parameters_dto.offset
        limit = get_requests_parameters_dto.limit
        
        if filterby:
            requests = self._filter_requests_and_get_request_objs(
                filterby=filterby, filterby_value=filterby_value
            )
        else:
            requests = Request.objects.filter(
                request_status=Confirmation.PENDING.value
            )

        if not sortby:
            sortby = SortRequests.DUE_DATETIME.value
        requests = self._sort_the_requests(
            sortby=sortby, requests=requests
        )

        requests.prefetch_related('resource','user', 'item')
        total_requests_dto = RequestsCountDto(requests_count=requests.count())
        requests = requests[offset: offset+limit]
        
        user_request_dtos = [
            self._prepare_user_request_dto(request)
            for request in requests
        ]
        return total_requests_dto, user_request_dtos
        
            
    def _filter_requests_and_get_request_objs(self,
            filterby: str, filterby_value: str):

        if filterby == FilterRequests.NAME.value:
            filterby_value = int(filterby_value)
            requests = Request.objects.filter(
                Q(user_id=filterby_value) &
                Q(request_status=Confirmation.PENDING.value)
            )
        elif filterby == FilterRequests.RESOURCE.value:
            requests = Request.objects.filter(
                Q(resource__name=filterby_value) &
                Q(request_status=Confirmation.PENDING.value)
            )
        else:
            requests = Request.objects.filter(
                Q(access_level=filterby_value) &
                Q(request_status=Confirmation.PENDING.value)
            )

        return requests

    def _sort_the_requests(self, sortby: str, requests):

        if sortby == SortRequests.RESOURCE.value:
            requests = requests.order_by('resource__name')
        elif sortby == SortRequests.ITEM.value:
            requests = requests.order_by('resource_item__title')
        elif sortby == SortRequests.NAME.value:
            requests = requests.order_by('user__name')
        else:
            requests = requests.order_by('-due_datetime')

        return requests

    def _prepare_user_request_dto(self, request):
        request_dto = UserRequestDto(request_id=request.id,
                                     resource_name=request.resource.name,
                                     item_title=request.resource_item.title,
                                     access_level=request.access_level,
                                     user_name=request.user.name,
                                     profile_pic=request.user.profile_pic,
                                     due_datetime=request.due_datetime
                                    )
        return request_dto

    def accept_requests(self, request_ids: List[int]):
        requests = Request.objects.filter(id__in=request_ids)
        requests.update(request_status=Confirmation.ACCEPT.value)
        for request in requests:
            user_id = request.user_id
            item_id = request.resource_item_id
            access_level = request.access_level
            
            AccessLevel.objects.update_or_create(
                user_id=user_id,
                resource_item_id=item_id,
                access_level=access_level
            )
        return

    def reject_requests(self, request_ids: List[int],
            reason_for_rejection: str):
        Request.objects.filter(id__in=request_ids)\
                .update(
                    request_status=Confirmation.REJECT.value,
                    reason_for_rejection=reason_for_rejection
                )
        return

    def get_user_requests(self, user_id: int,
            requests_parameters_dto: GetRequestsParametersDto):
        filterby = requests_parameters_dto.filterby
        sortby = requests_parameters_dto.sortby
        filterby_value = requests_parameters_dto.filterby_value
        offset = requests_parameters_dto.offset
        limit = requests_parameters_dto.limit

        if filterby:
            requests = self._filter_user_requests_and_get_request_objs(
                filterby=filterby, filterby_value=filterby_value,
                user_id=user_id
            )
        else:
            requests = Request.objects.filter(user_id=user_id)
        
        if sortby:
            requests = self._sort_the_user_requests(
                sortby=sortby, requests=requests
            )

        requests.prefetch_related('resource', 'item')
        total_requests_dto = RequestsCountDto(requests_count=requests.count())
        requests = requests[offset: offset+limit]
        
        user_request_dtos = [
            self._prepare_user_request_status_dto(request)
            for request in requests
        ]
        return total_requests_dto, user_request_dtos

    def _filter_user_requests_and_get_request_objs(self,
            filterby: str, filterby_value: str, user_id: int):

        if filterby == FilterRequests.STATUS.value:
            requests = Request.objects.filter(
                Q(user_id=user_id) & Q(request_status=filterby_value)
            )
        elif filterby == FilterRequests.RESOURCE.value:
            requests = Request.objects.filter(
                Q(resource__name=filterby_value) & Q(user_id=user_id)
            )
        else:
            requests = Request.objects.filter(
                Q(access_level=filterby_value) & Q(user_id=user_id)
            )

        return requests

    def _sort_the_user_requests(self, sortby: str, requests):

        if sortby == SortRequests.RESOURCE.value:
            requests = requests.order_by('resource__name')
        elif sortby == SortRequests.STATUS.value:
            requests = requests.order_by('request_status')
        else:
            requests = requests.order_by('access_level')

        return requests

    def _prepare_user_request_status_dto(self, request):
        return RequestStatusDto(
            resource_name=request.resource.name,
            item_title=request.resource_item.title,
            status=request.request_status,
            access_level=request.access_level,
            request_id=request.id
        )

    def check_is_request_exists(self, request_id: int) -> bool:
        return Request.objects.filter(id=request_id).exists()

    def check_is_user_creator_of_request(self, user_id: int,
            request_id: int) -> bool:
        request = Request.objects.get(id=request_id)
        return request.user_id == user_id

    def check_is_admin_responded_to_request(self, request_id: int) -> bool:
        request = Request.objects.get(id=request_id)
        is_admin_responded = \
            request.request_status != Confirmation.PENDING.value
        return is_admin_responded

    def delete_request(self, request_id: int):
        Request.objects.filter(id=request_id).delete()

    def create_request(self, user_id: int, request_dto: RequestDto):
        Request.objects.create(resource_id=request_dto.resource_id,
                               resource_item_id=request_dto.item_id,
                               access_level=request_dto.access_level,
                               due_datetime=request_dto.due_datetime,
                               reason_for_access=request_dto.reason_for_access,
                               user_id=user_id
                              )
        return
