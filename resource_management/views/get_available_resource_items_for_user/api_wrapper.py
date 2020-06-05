import json
from django.http import HttpResponse

from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from resource_management.interactors.user_resource_items_interactor import \
    UserResourceItemsInteractor
from resource_management.storages.item_storage_implementation import \
    ItemStorageImplementation
from resource_management.storages.user_implementation import \
    UserImplementation
from resource_management.presenters.presenter_implementation import \
    PresenterImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    user_id = user.id
    offset = kwargs['request_query_params'].offset
    limit = kwargs['request_query_params'].limit
    search = kwargs['request_query_params'].search

    user_storage = UserImplementation()
    item_storage = ItemStorageImplementation()
    presenter = PresenterImplementation()
    interactor = UserResourceItemsInteractor(
        user_storage=user_storage,
        item_storage=item_storage,
        presenter=presenter
    )

    resource_items_dict = interactor.get_resource_items_for_user(
        user_id=user_id, offset=offset,
        limit=limit, search=search
    )
    data = json.dumps(resource_items_dict)
    return HttpResponse(data, status=200)
