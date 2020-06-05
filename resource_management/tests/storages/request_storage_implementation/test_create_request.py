import pytest

from resource_management.storages.request_storage_implementation import \
    RequestStorageImplementation
from resource_management.models import Request


@pytest.mark.django_db
def test_create_request_creates_new_request(
        users, create_resource_items, request_dto):
    # Arrange
    user_id = 1
    request_storage = RequestStorageImplementation()

    # Act
    request_storage.create_request(user_id=user_id, request_dto=request_dto)

    # Assert
    assert Request.objects.filter(user_id=user_id).exists() == True
