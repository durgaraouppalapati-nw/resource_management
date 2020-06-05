from abc import abstractmethod, ABC

from resource_management.interactors.storages.dtos import (
    UserDetailsDto, UsersWithCountDetailsDto, UsersDto
)


class UserInterface(ABC):

    @abstractmethod
    def check_is_username_already_exists(self, username: str) -> bool:
        pass

    @abstractmethod
    def create_user(self, username: str, password: str) -> str:
        pass

    @abstractmethod
    def check_is_user_admin(self, user_id: int) -> bool:
        pass

    @abstractmethod
    def get_user_details(self, user_id: int) -> UserDetailsDto:
        pass

    @abstractmethod
    def validate_username_and_password_get_user_id(
            self, username: str, password: str) -> int:
        pass

    @abstractmethod
    def get_users_for_item(self,
            item_id: int, offset: int, limit: int) -> UsersWithCountDetailsDto:
        pass

    @abstractmethod
    def get_all_users(self, offset: int, limit: int) -> UsersDto:
        pass

    @abstractmethod
    def check_is_user_exists(self, user_id: int) -> bool:
        pass

    @abstractmethod
    def update_profile(self, user_id: int,
            user_details_dto: UserDetailsDto):
        pass

    @abstractmethod
    def check_is_password_valid(self, user_id: int, password: str) -> bool:
        pass

    @abstractmethod
    def update_password(self, user_id: int, new_password: str):
        pass
