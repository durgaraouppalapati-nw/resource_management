from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from resource_management.interactors.add_item_to_user_interactor import \
    AddResourceItemToUserInteractor
from resource_management.storages.item_storage_implementation import \
    ItemStorageImplementation
from resource_management.storages.user_implementation import \
    UserImplementation
from resource_management.presenters.presenter_implementation import \
    PresenterImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_id = kwargs['user_id']
    request_data = kwargs['request_data']
    item_id = request_data['item_id']
    access_level = request_data['access_level']
    user = kwargs['user']
    requested_user_id = user.id

    user_storage = UserImplementation()
    item_storage = ItemStorageImplementation()
    presenter = PresenterImplementation()
    interactor = AddResourceItemToUserInteractor(
        user_storage=user_storage,
        item_storage=item_storage,
        presenter=presenter
    )

    interactor.add_resource_item_to_user(
        user_id=user_id, item_id=item_id, access_level=access_level,
        requested_user_id=requested_user_id
    )
    return HttpResponse(status=201)
