from resource_management.interactors.storages.request_interface import \
    RequestInterface
from resource_management.interactors.storages.resource_interface import \
    ResourceInterface
from resource_management.interactors.storages.item_interface import \
    ItemInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from resource_management.interactors.storages.dtos import RequestDto


class CreateRequestInteractor:

    def __init__(self, request_storage: RequestInterface,
                 resource_storage: ResourceInterface,
                 item_storage: ItemInterface,
                 presenter: PresenterInterface):
        self.request_storage = request_storage
        self.resource_storage = resource_storage
        self.item_storage = item_storage
        self.presenter = presenter

    def create_request(self, user_id: int, request_dto: RequestDto):
        resource_id = request_dto.resource_id
        item_id = request_dto.item_id

        is_resource_not_exists = \
            not self.resource_storage.check_is_resource_exists(
                resource_id=resource_id
            )
        if is_resource_not_exists:
            self.presenter.raise_exception_for_resource_not_found()

        is_resource_item_not_exists = \
            not self.item_storage.check_is_resource_item_exists(
                item_id=item_id    
            )
        if is_resource_item_not_exists:
            self.presenter.raise_exception_for_resource_item_not_found()

        is_resource_item_not_belongs_to_resource = \
            not self.item_storage.check_is_resource_item_belongs_to_resource(
                resource_id=resource_id, item_id=item_id    
            )
        if is_resource_item_not_belongs_to_resource:
            self.presenter.raise_exception_for_item_not_belongs_to_resource()

        self.request_storage.create_request(
            user_id=user_id, request_dto=request_dto
        )
        return
