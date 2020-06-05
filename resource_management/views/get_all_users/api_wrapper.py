import json

from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from resource_management.interactors.get_all_users_interactor import \
    GetAllUsersInteractor
from resource_management.storages.user_implementation import \
    UserImplementation
from resource_management.presenters.presenter_implementation import \
    PresenterImplementation

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    offset = kwargs['request_query_params'].offset
    limit = kwargs['request_query_params'].limit
    user = kwargs['user']
    user_id = user.id

    user_storage = UserImplementation()
    presenter = PresenterImplementation()
    interactor = GetAllUsersInteractor(
        user_storage=user_storage,
        presenter=presenter
    )

    users_dict = interactor.get_all_users(
        offset=offset, limit=limit,
        user_id=user_id
    )
    data = json.dumps(users_dict)

    return HttpResponse(data, status=200)
