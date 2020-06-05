from django.http import HttpResponse

from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from resource_management.interactors.delete_request_interactor import \
    DeleteRequestIntercator
from resource_management.storages.request_storage_implementation import \
    RequestStorageImplementation
from resource_management.presenters.presenter_implementation import \
    PresenterImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    request_id = kwargs['request_id']
    user = kwargs['user']
    user_id = user.id

    request_storage = RequestStorageImplementation()
    presenter = PresenterImplementation()
    interactor = DeleteRequestIntercator(
        request_storage=request_storage,
        presenter=presenter
    )

    interactor.delete_request(user_id=user_id, request_id=request_id)
    return HttpResponse(status=200)
