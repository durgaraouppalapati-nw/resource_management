from typing import List

from resource_management.interactors.storages.item_interface import \
    ItemInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface


class GetResourceItemsInteractor:

    def __init__(self, item_storage: ItemInterface):
        self.item_storage = item_storage

    def get_resource_items_wrapper(self, presenter: PresenterInterface,
                                   item_ids: List[int]):
        try:
            item_dtos = self.get_resource_items(item_ids=item_ids)
        except:
            pass
            return

        return item_dtos

    def get_resource_items(self, item_ids: List[int]):
        unique_item_ids = self._get_unique_ids(ids=item_ids)
        item_dtos = self.item_storage.get_resource_items(
            item_ids=unique_item_ids    
        )
        return item_dtos

    def _get_unique_ids(self, ids: List[int]):
        return list(set(ids))
