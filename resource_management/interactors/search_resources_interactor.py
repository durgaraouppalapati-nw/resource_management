from resource_management.interactors.storages.resource_interface import \
    ResourceInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface
from resource_management.constants.enums import SearchBy


class SearchResourcesInteractor:

    def __init__(self, resource_storage: ResourceInterface,
                 presenter: PresenterInterface):
        self.resource_storage = resource_storage
        self.presenter = presenter

    def search_resources(self, search: str):
        resources_dtos = \
            self.resource_storage.search_resources(search=search)

        return self.presenter.get_response_for_search_resources(
            resource_dtos=resources_dtos,    
        )
