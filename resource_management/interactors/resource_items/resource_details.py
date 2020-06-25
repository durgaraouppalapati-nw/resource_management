from resource_management.interactors.storages.resource_interface import \
    ResourceInterface
from resource_management.interactors.presenter.presenter_interface import \
    PresenterInterface
from resource_management.exceptions.exceptions import InvalidResourceId


class GetResourceDetailsInteractor:

    def __init__(self, resource_storage: ResourceInterface):
        self.resource_storage = resource_storage

    def get_resource_details_wrapper(self, resource_id: int,
                                     presenter: PresenterInterface):
        try:
            resource_dto = self.get_resource_details(resource_id=resource_id)
        except InvalidResourceId:
            presenter.raise_exception_for_resource_not_found()
            return

        return resource_dto

    def get_resource_details(self, resource_id: int):
        self.resource_storage.check_is_resource_exists(resource_id)
        resource_dto = self.resource_storage.get_resource_details(
            resource_id=resource_id    
        )
        return resource_dto
