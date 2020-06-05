from resource_management.interactors.storages.item_interface import \
    ItemInterface
from resource_management.interactors.storages.resource_interface import \
    ResourceInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface


class SearchResourceItemsInteractor:

    def __init__(self, item_storage: ItemInterface,
                 resource_storage: ResourceInterface,
                 presenter: PresenterInterface):
        self.item_storage = item_storage
        self.resource_storage = resource_storage
        self.presenter = presenter

    def search_resource_items(self, resource_id: int,
            search: str):
        is_resource_not_exists = \
            not self.resource_storage.check_is_resource_exists(resource_id)
        if is_resource_not_exists:
            self.presenter.raise_exception_for_resource_not_found()

        item_dtos = \
            self.item_storage.search_resource_items(
                resource_id=resource_id, search=search
            )
        return self.presenter.get_response_for_search_resource_items(
            item_dtos=item_dtos
        )
