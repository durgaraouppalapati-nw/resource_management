from resource_management.interactors.storages.user_interface import \
    UserInterface
from resource_management.interactors.storages.dtos import UserDetailsDto


class UpdateProfileInteractor:

    def __init__(self, user_storage: UserInterface):
        self.user_storage = user_storage

    def update_profile(self, user_id: int,
            user_details_dto: UserDetailsDto):
        self.user_storage.update_profile(
            user_id=user_id, user_details_dto=user_details_dto    
        )

        return
