import json

from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from resource_management.interactors.search_resources_interactor import \
    SearchResourcesInteractor
from resource_management.storages.resource_storage_implementation import \
    ResourceStorageImplementation
from resource_management.presenters.presenter_implementation import \
    PresenterImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    search = kwargs['request_query_params'].search
    resource_storage = ResourceStorageImplementation()
    presenter = PresenterImplementation()
    interactor = SearchResourcesInteractor(
        resource_storage=resource_storage,
        presenter=presenter
    )

    resources_details = interactor.search_resources(search=search)
    data = json.dumps(resources_details)
    return HttpResponse(data, status=200)
