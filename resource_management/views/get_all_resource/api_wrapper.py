import json

from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from resource_management.interactors.resources_interactor import \
    ResourceInteractor
from resource_management.storages.resource_storage_implementation import \
    ResourceStorageImplementation
from resource_management.presenters.presenter_implementation import \
    PresenterImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    offset = kwargs['request_query_params'].offset
    limit = kwargs['request_query_params'].limit
    user = kwargs['user']
    user_id = user.id

    resource_storage = ResourceStorageImplementation()
    presenter = PresenterImplementation()
    interactor = ResourceInteractor(
        resource_storage=resource_storage,
        presenter=presenter
    )

    resources_details = interactor.get_all_resources(
        offset=offset, limit=limit, user_id=user_id
    )
    data = json.dumps(resources_details)

    return HttpResponse(data, status=200)
