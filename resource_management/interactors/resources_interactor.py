from resource_management.interactors.storages.resource_interface import \
    ResourceInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface


class ResourceInteractor:

    def __init__(self, resource_storage: ResourceInterface,
                 presenter: PresenterInterface):
        self.resource_storage = resource_storage
        self.presenter = presenter

    def get_all_resources(self, offset: int, limit: int, user_id: int):
        
        if offset < 0:
            self.presenter.raise_exception_for_invalid_offset_length()
            return

        if limit < 0:
            self.presenter.raise_exception_for_invalid_limit_length()
            return

        is_user_not_admin = \
            not self.resource_storage.check_is_user_admin(user_id=user_id)
        if is_user_not_admin:
            self.presenter.raise_exception_for_unauthorized_user()
            return

        all_resources_dto = self.resource_storage.get_all_resources(
            offset=offset, limit=limit   
        )

        return self.presenter.get_response_for_get_all_resources(
            resources_details_dto=all_resources_dto
        )
