from django.http import HttpResponse

from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from resource_management.interactors.create_request_interactor import \
    CreateRequestInteractor
from resource_management.storages.resource_storage_implementation import \
    ResourceStorageImplementation
from resource_management.storages.request_storage_implementation import \
    RequestStorageImplementation
from resource_management.storages.item_storage_implementation import \
    ItemStorageImplementation
from resource_management.presenters.presenter_implementation import \
    PresenterImplementation
from resource_management.interactors.storages.dtos import RequestDto


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    user_id= user.id
    request_data = kwargs['request_data']
    resource_id = request_data['resource_id']
    item_id = request_data['item_id']
    access_level = request_data['access_level']
    due_datetime = request_data['due_datetime']
    reason_for_access = request_data['reason_for_access']

    request_dto = RequestDto(resource_id=resource_id,
                             item_id=item_id,
                             access_level=access_level,
                             due_datetime=due_datetime,
                             reason_for_access=reason_for_access
                            )

    request_storage = RequestStorageImplementation()
    resource_storage = ResourceStorageImplementation()
    item_storage = ItemStorageImplementation()
    presenter = PresenterImplementation()
    interactor = CreateRequestInteractor(
        request_storage=request_storage,
        resource_storage=resource_storage,
        item_storage=item_storage,
        presenter=presenter
    )

    interactor.create_request(user_id=user_id, request_dto=request_dto)
    return HttpResponse(status=201)
