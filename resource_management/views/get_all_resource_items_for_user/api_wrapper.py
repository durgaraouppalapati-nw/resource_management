import json

from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from resource_management.storages.user_implementation import \
    UserImplementation
from resource_management.storages.item_storage_implementation import \
    ItemStorageImplementation
from resource_management.presenters.presenter_implementation import \
    PresenterImplementation
from resource_management.interactors.get_resource_items_for_user_interactor \
    import GetAllResourceItemsForUserInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_id = kwargs['user_id']
    offset = kwargs['request_query_params'].offset
    limit = kwargs['request_query_params'].limit
    user = kwargs['user']
    requested_user_id = user.id
    
    user_storage = UserImplementation()
    item_storage = ItemStorageImplementation()
    presenter = PresenterImplementation()
    interactor = GetAllResourceItemsForUserInteractor(
        user_storage=user_storage,
        item_storage=item_storage,
        presenter=presenter
    )

    user_resource_items_dict = interactor.get_all_resource_items_for_user(
        user_id=user_id,
        offset=offset,
        limit=limit,
        requested_user_id=requested_user_id
    )
    data = json.dumps(user_resource_items_dict)

    return HttpResponse(data, status=200)
