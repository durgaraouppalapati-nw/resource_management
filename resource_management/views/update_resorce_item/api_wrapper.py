from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from resource_management.interactors.update_resource_item_interactor import \
    UpdateResourceItemInteractor
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
    item_id = kwargs['item_id']
    request_data = kwargs['request_data']
    title = request_data['title']
    link = request_data['link']
    description = request_data['description']

    item_storage = ItemStorageImplementation()
    user_storage = UserImplementation()
    presenter = PresenterImplementation()
    interactor = UpdateResourceItemInteractor(
        item_storage=item_storage,
        user_storage=user_storage,
        presenter=presenter
    )

    interactor.update_resource_item(
        user_id=user_id,
        title=title,
        link=link,
        description = description,
        item_id=item_id
    )
    return HttpResponse(status=200)
