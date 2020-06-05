import json

from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from resource_management.interactors.get_requests_interactor import \
    GetRequestsInteractor
from resource_management.storages.request_storage_implementation import \
    RequestStorageImplementation
from resource_management.storages.user_implementation import \
    UserImplementation
from resource_management.presenters.presenter_implementation import \
    PresenterImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    sortby = kwargs['request_query_params'].sortby
    offset = kwargs['request_query_params'].offset
    limit = kwargs['request_query_params'].limit
    request_data = kwargs['request_data']
    filterby = request_data['filterby']
    value = request_data['value']
    user = kwargs['user']
    user_id = user.id

    request_storage = RequestStorageImplementation()
    user_storage = UserImplementation()
    presenter = PresenterImplementation()
    interactor = GetRequestsInteractor(
        request_storage=request_storage,
        user_storage=user_storage,
        presenter=presenter
    )

    requests_dict = interactor.get_requests(
        offset=offset, limit=limit, sortby=sortby,
        filterby=filterby, value=value, user_id=user_id
    )
    data = json.dumps(requests_dict)

    return HttpResponse(data, status=200)
