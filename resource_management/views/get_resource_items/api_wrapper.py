import json

from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from resource_management.interactors.resource_items_interactor import \
    ResourceItemsInteractor
from resource_management.storages.item_storage_implementation import \
    ItemStorageImplementation
from resource_management.presenters.presenter_implementation import \
    PresenterImplementation
from resource_management.storages.resource_storage_implementation import \
    ResourceStorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    resource_id = kwargs['resource_id']
    offset = kwargs['request_query_params'].offset
    limit = kwargs['request_query_params'].limit
    user = kwargs['user']
    user_id = user.id

    item_storage = ItemStorageImplementation()
    resource_storage = ResourceStorageImplementation()
    presenter = PresenterImplementation()
    interactor = ResourceItemsInteractor(
        item_storage=item_storage,
        resource_storage=resource_storage,
        presenter=presenter
    )

    items_details = interactor.get_items_for_resource(
        resource_id=resource_id, offset=offset, limit=limit, user_id=user_id
    )
    data = json.dumps(items_details)

    return HttpResponse(data, status=200)
