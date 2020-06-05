from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from resource_management.interactors.signup_interactor import \
    SignUpInteractor
from resource_management.storages.user_implementation import \
    UserImplementation
from resource_management.presenters.presenter_implementation import \
    PresenterImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    request_data = kwargs['request_data']
    username = request_data['username']
    password = request_data['password']
    confirm_password = request_data['confirm_password']

    user_storage = UserImplementation()
    presenter = PresenterImplementation()
    interactor = SignUpInteractor(
        user_storage=user_storage,
        presenter=presenter
    )

    interactor.create_user(
        username=username,
        password=password,
        confirm_password=confirm_password
    )

    return HttpResponse(status=201)
