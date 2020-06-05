import json

from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from resource_management.storages.resource_storage_implementation import \
    ResourceStorageImplementation
from resource_management.presenters.presenter_implementation import \
    PresenterImplementation
from resource_management.interactors.delete_resource_interactor import \
    DeleteResourceInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    user_id = user.id
    resource_id = kwargs['resource_id']

    presenter = PresenterImplementation()
    resource_storage = ResourceStorageImplementation()
    interactor = DeleteResourceInteractor(
        resource_storage=resource_storage,
        presenter=presenter
    )

    interactor.delete_resource(
        user_id=user_id, resource_id=resource_id
    )

    return HttpResponse(status=200)
