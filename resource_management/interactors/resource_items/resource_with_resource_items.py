from resource_management.interactors.storages.resource_interface import \
    ResourceInterface
from resource_management.interactors.storages.item_interface import \
    ItemInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from resource_management.exceptions.exceptions import (
    InvalidOffsetValue, InvalidLimitValue, InvalidResourceId
)
from resource_management.interactors.mixins.pagination_mixin import \
    LimitOffsetValidationMixin
from resource_management.interactors.storages.dtos import \
    ResourceWithResourceItemsDTO


class ResourceWithResourceItemsInteractor(LimitOffsetValidationMixin):

    def __init__(self, resource_storage: ResourceInterface,
                 item_storage: ItemInterface):
        self.resource_storage = resource_storage
        self.item_storage = item_storage

    def get_resource_with_resource_items_wrapper(self,
            resource_id: int, offset: int, limit: int,
            presenter: PresenterInterface):

        try:
            resource_with_items = self.get_resource_with_resource_items(
                resource_id=resource_id, offset=offset, limit=limit    
            )
        except InvalidOffsetValue:
            presenter.raise_exception_for_invalid_offset_length()
        except InvalidLimitValue:
            presenter.raise_exception_for_invalid_limit_length()
        except InvalidResourceId:
            presenter.raise_exception_for_resource_not_found()

        return presenter.get_resource_with_resource_items_response(
            resource_with_items=resource_with_items    
        )

    def get_resource_with_resource_items(self,
            resource_id: int, offset: int, limit: int):
        self.check_is_valid_offset_value(offset)
        self.check_is_valid_limit_value(limit)

        is_resource_not_exists = \
            not self.resource_storage.check_is_resource_exists(resource_id)
        if is_resource_not_exists:
            raise InvalidResourceId

        resource_item_ids = \
            self.resource_storage.get_resource_item_ids(resource_id)
        resource_item_ids = resource_item_ids[offset: offset+limit]

        from resource_management.interactors.resource_items.resource_details \
            import GetResourceDetailsInteractor
        from resource_management.interactors.resource_items.resource_items \
            import GetResourceItemsInteractor

        resource_interactor = GetResourceDetailsInteractor(
            resource_storage=self.resource_storage    
        )
        resource_items_interactor = GetResourceItemsInteractor(
            item_storage=self.item_storage    
        )

        resource_details = resource_interactor.get_resource_details(
            resource_id=resource_id    
        )
        resource_items_details = resource_items_interactor.get_resource_items(
            item_ids=resource_item_ids    
        )

        return ResourceWithResourceItemsDTO(
            resource=resource_details,
            resource_items=resource_items_details
        )
