import json

from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from resource_management.storages.resource_storage_implementation import \
    ResourceStorageImplementation
from resource_management.presenters.presenter_implementation import \
    PresenterImplementation
from resource_management.storages.item_storage_implementation import \
    ItemStorageImplementation
from resource_management.interactors.search_resource_items_interactor import \
    SearchResourceItemsInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    search = kwargs['request_query_params'].search
    resource_id = kwargs['resource_id']

    resource_storage = ResourceStorageImplementation()
    item_storage = ItemStorageImplementation()
    presenter = PresenterImplementation()
    interactor = SearchResourceItemsInteractor(
        resource_storage=resource_storage,
        item_storage=item_storage,
        presenter=presenter
    )

    items_details = interactor.search_resource_items(
        resource_id=resource_id, search=search    
    )
    data = json.dumps(items_details)
    return HttpResponse(data, status=200)
