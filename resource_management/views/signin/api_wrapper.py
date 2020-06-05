import json

from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from resource_management.interactors.signin_interactor import \
    SignInInteractor
from resource_management.storages.user_implementation import \
    UserImplementation
from resource_management.presenters.presenter_implementation import \
    PresenterImplementation
from common.oauth2_storage import OAuth2SQLStorage


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    request_data = kwargs['request_data']
    username = request_data['username']
    password = request_data['password']

    user_storage = UserImplementation()
    presenter = PresenterImplementation()
    oauth_storage = OAuth2SQLStorage()
    interactor = SignInInteractor(
        user_storage=user_storage,
        oauth_storage=oauth_storage,
        presenter=presenter
    )

    access_token_dict = interactor.login_with_credentials(
        username=username, password=password    
    )
    response = json.dumps(access_token_dict)
    return HttpResponse(response, status=200)
