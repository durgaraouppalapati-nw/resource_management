from abc import abstractmethod, ABC
from typing import List

from resource_management.interactors.storages.dtos import (
    ItemsWithCountDetailsDto, UserWithResourceItemsDto,
    UserResourceItemsDto, ItemMinimalDetailsDto
)


class ItemInterface(ABC):

    @abstractmethod
    def get_items_for_resource(
            self, resource_id: int, offset: int, limit: int
            ) -> ItemsWithCountDetailsDto:
        pass

    @abstractmethod
    def create_resource_item(self, resource_id: int,
            title: str, link: str, description: str):
        pass

    @abstractmethod
    def check_is_resource_item_exists(self, item_id: int) -> bool:
        pass

    @abstractmethod
    def update_resource_item(self, item_id: int, title: str,
            link: str, description: str):
        pass

    @abstractmethod
    def delete_resource_items(self, item_ids: List[int]):
        pass

    @abstractmethod
    def get_all_resource_items_for_user(self,
            user_id: int, offset: int, limit: int) -> UserWithResourceItemsDto:
        pass

    @abstractmethod
    def add_resource_item_to_user(self, user_id: int,
            item_id: int, access_level: str):
        pass

    @abstractmethod
    def get_user_resource_items(self, user_id: int, offset: int,
            limit: int, search: str) -> UserResourceItemsDto:
        pass

    @abstractmethod
    def search_resource_items(self, resource_id: int,
            search: str) -> List[ItemMinimalDetailsDto]:
        pass

    @abstractmethod
    def check_is_resource_item_belongs_to_resource(self,
            item_id: int, resource_id: int) -> bool:
        pass
