from django.http import HttpResponse

from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from resource_management.storages.user_implementation import \
    UserImplementation
from resource_management.presenters.presenter_implementation import \
    PresenterImplementation
from resource_management.interactors.update_password_interactor import \
    UpdatePasswordInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    request_data = kwargs['request_data']
    old_password = request_data['old_password']
    new_password = request_data['new_password']
    confirm_password = request_data['confirm_password']
    user = kwargs['user']
    user_id = user.id

    user_storage = UserImplementation()
    presenter = PresenterImplementation()
    interactor = UpdatePasswordInteractor(
        user_storage=user_storage,
        presenter=presenter
    )

    interactor.update_password(
        user_id=user_id, old_password=old_password,
        new_password=new_password, confirm_password=confirm_password
    )
    return HttpResponse(status=200)
