from abc import abstractmethod, ABC

from resource_management.interactors.storages.dtos import \
    ResourcesDetailsDto, ResourceMinimalDetailsDto


class ResourceInterface(ABC):

    @abstractmethod
    def get_all_resources(self, offset: int,
            limit: int) -> ResourcesDetailsDto:
        pass

    @abstractmethod
    def check_is_user_admin(self, user_id: int) -> bool:
        pass

    @abstractmethod
    def check_is_resource_exists(self, resource_id: int) -> bool:
        pass

    @abstractmethod
    def update_resource_and_get_dto(self, 
            resource_id, name: str, resource_pic: str, link: str,
            description: str):
        pass

    @abstractmethod
    def delete_resource(self, resource_id):
        pass

    @abstractmethod
    def create_resource(self, name: str,
            resource_pic: str, link: str, description: str):
        pass

    @abstractmethod
    def check_is_resource_name_already_exists(self, resource_name: str) ->bool:
        pass

    @abstractmethod
    def search_resources(self, search: str) -> ResourceMinimalDetailsDto:
        pass
