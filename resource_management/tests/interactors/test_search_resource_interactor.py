from unittest.mock import create_autospec

from resource_management.interactors.search_resources_interactor \
    import SearchResourcesInteractor
from resource_management.interactors.storages.resource_interface import \
    ResourceInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface


def test_search_resources_interactor_return_details(
        resources):
    # Arrange
    search = "AWS"
    resource_storage = create_autospec(ResourceInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = SearchResourcesInteractor(
        resource_storage=resource_storage,
        presenter=presenter
    )
    resource_storage.search_resources.return_value = resources

    # Act
    interactor.search_resources(search=search)

    # Assert
    resource_storage.search_resources.assert_called_once_with(search=search)
    presenter.get_response_for_search_resources.assert_called_once_with(
        resource_dtos=resources
    )
