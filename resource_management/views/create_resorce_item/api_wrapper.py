from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from resource_management.interactors.create_resource_item_interactor import \
    CreateResourceItemInteractor
from resource_management.storages.item_storage_implementation import \
    ItemStorageImplementation
from resource_management.storages.resource_storage_implementation import \
    ResourceStorageImplementation
from resource_management.presenters.presenter_implementation import \
    PresenterImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    user_id = user.id
    resource_id = kwargs['resource_id']
    request_data = kwargs['request_data']
    title = request_data['title']
    link = request_data['link']
    description = request_data['description']

    item_storage = ItemStorageImplementation()
    resource_storage = ResourceStorageImplementation()
    presenter = PresenterImplementation()
    interactor = CreateResourceItemInteractor(
        item_storage=item_storage,
        resource_storage=resource_storage,
        presenter=presenter
    )

    interactor.create_resource_item(
        resource_id=resource_id,
        user_id=user_id,
        title=title,
        link=link,
        description = description
    )
    return HttpResponse(status=201)
