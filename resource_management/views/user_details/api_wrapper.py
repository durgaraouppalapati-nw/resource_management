import json

from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from resource_management.interactors.user_profile_interactor import \
    UserProfileInteractor
from resource_management.storages.user_implementation import \
    UserImplementation
from resource_management.presenters.presenter_implementation import \
    PresenterImplementation
from common.oauth2_storage import OAuth2SQLStorage


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    user_id = user.id

    user_storage = UserImplementation()
    presenter = PresenterImplementation()
    interactor = UserProfileInteractor(
        user_storage=user_storage,
        presenter=presenter
    )

    user_details = interactor.get_user_details(user_id=user_id)

    response = json.dumps(user_details)
    return HttpResponse(response, status=200)
