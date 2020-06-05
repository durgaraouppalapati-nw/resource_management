import json

from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from resource_management.storages.resource_storage_implementation import \
    ResourceStorageImplementation
from resource_management.presenters.presenter_implementation import \
    PresenterImplementation
from resource_management.interactors.update_resource_interactor import \
    UpdateResourceInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    user_id = user.id
    resource_id = kwargs['resource_id']
    request_data = kwargs['request_data']
    name = request_data['name']
    resource_pic = request_data['resource_pic']
    link = request_data['link']
    description = request_data['description']

    presenter = PresenterImplementation()
    resource_storage = ResourceStorageImplementation()
    interactor = UpdateResourceInteractor(
        resource_storage=resource_storage,
        presenter=presenter
    )

    updated_resorce = interactor.update_resource(
        user_id=user_id, name=name, resource_pic=resource_pic,
        link=link, description=description, resource_id=resource_id
    )
    data = json.dumps(updated_resorce)

    return HttpResponse(data, status=200)
