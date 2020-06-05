import json

from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from resource_management.interactors.get_user_requests_interactor import \
    GetUserRequestsInteractor
from resource_management.storages.user_implementation import \
    UserImplementation
from resource_management.storages.request_storage_implementation import \
    RequestStorageImplementation
from resource_management.presenters.presenter_implementation import \
    PresenterImplementation
from resource_management.interactors.storages.dtos import \
    GetRequestsParametersDto


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    user_id = user.id
    sortby = kwargs['request_query_params'].sortby
    offset = kwargs['request_query_params'].offset
    limit = kwargs['request_query_params'].limit
    request_data = kwargs['request_data']
    filterby = request_data['filterby']
    value = request_data['value']
    
    requests_parameters_dto = GetRequestsParametersDto(
        offset=offset,
        limit=limit,
        sortby=sortby,
        filterby=filterby,
        filterby_value=value
    )

    user_storage = UserImplementation()
    request_storage = RequestStorageImplementation()
    presenter = PresenterImplementation()
    interactor = GetUserRequestsInteractor(
        user_storage=user_storage,
        request_storage=request_storage,
        presenter=presenter
    )

    requests_details = interactor.get_user_requests(
        user_id=user_id, requests_parameters_dto=requests_parameters_dto    
    )
    data = json.dumps(requests_details)
    return HttpResponse(data, status=200)
