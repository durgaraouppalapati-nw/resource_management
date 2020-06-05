from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from resource_management.interactors.delete_resource_items_interactor import \
    DeleteResourceItemsInteractor
from resource_management.storages.item_storage_implementation import \
    ItemStorageImplementation
from resource_management.storages.user_implementation import \
    UserImplementation
from resource_management.presenters.presenter_implementation import \
    PresenterImplementation



@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    user_id = user.id
    request_data = kwargs['request_data']
    item_ids = request_data['item_ids']

    item_storage = ItemStorageImplementation()
    user_storage = UserImplementation()
    presenter = PresenterImplementation()
    interactor = DeleteResourceItemsInteractor(
        item_storage=item_storage,
        user_storage=user_storage,
        presenter=presenter
    )

    interactor.delete_resource_items(
        user_id=user_id, item_ids=item_ids
    )
    return HttpResponse(status=200)
