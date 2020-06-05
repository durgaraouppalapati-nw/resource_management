import json

from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from resource_management.interactors.users_for_item_interactor import \
    UsersForItemInteractor
from resource_management.storages.user_implementation import \
    UserImplementation
from resource_management.storages.item_storage_implementation import \
    ItemStorageImplementation
from resource_management.presenters.presenter_implementation import \
    PresenterImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    item_id = kwargs['item_id']
    offset = kwargs['request_query_params'].offset
    limit = kwargs['request_query_params'].limit
    user = kwargs['user']
    user_id = user.id

    user_storage = UserImplementation()
    item_storage = ItemStorageImplementation()
    presenter = PresenterImplementation()
    interactor = UsersForItemInteractor(
        user_storage=user_storage,
        item_storage=item_storage,
        presenter=presenter
    )

    users_details = interactor.get_users_for_item(
        item_id=item_id, offset=offset, limit=limit, user_id=user_id 
    )
    data = json.dumps(users_details)

    return HttpResponse(data, status=200)
