import pytest
from unittest.mock import create_autospec

from django_swagger_utils.drf_server.exceptions import NotFound

from resource_management.interactors.search_resource_items_interactor \
    import SearchResourceItemsInteractor
from resource_management.interactors.storages.resource_interface import \
    ResourceInterface
from resource_management.interactors.storages.item_interface import \
    ItemInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface


def test_search_resource_items_interactor_return_items_details(
        items):
    # Arrange
    resource_id = 1
    search = "cloud"
    resource_storage = create_autospec(ResourceInterface)
    item_storage = create_autospec(ItemInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = SearchResourceItemsInteractor(
        resource_storage=resource_storage,
        item_storage=item_storage,
        presenter=presenter
    )
    resource_storage.check_is_resource_exists.return_value = True
    item_storage.search_resource_items.return_value = items

    # Act
    interactor.search_resource_items(resource_id=resource_id, search=search)

    # Assert
    resource_storage.check_is_resource_exists.assert_called_once_with(
        resource_id=resource_id
    )
    item_storage.search_resource_items.assert_called_once_with(
        resource_id=resource_id, search=search    
    )
    presenter.get_response_for_search_resource_items.assert_called_once_with(
        item_dtos=items
    )


def test_search_resource_items_interactor_without_resource_raise_exception(
        items):
    # Arrange
    resource_id = 1
    search = "cloud"
    resource_storage = create_autospec(ResourceInterface)
    item_storage = create_autospec(ItemInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = SearchResourceItemsInteractor(
        resource_storage=resource_storage,
        item_storage=item_storage,
        presenter=presenter
    )
    resource_storage.check_is_resource_exists.return_value = False
    presenter.raise_exception_for_resource_not_found.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.search_resource_items(
            resource_id=resource_id, search=search
        )

    # Assert
    resource_storage.check_is_resource_exists.assert_called_once_with(
        resource_id=resource_id
    )
    presenter.raise_exception_for_resource_not_found.assert_called_once()
