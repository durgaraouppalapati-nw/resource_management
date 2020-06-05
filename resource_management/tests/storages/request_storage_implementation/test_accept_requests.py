import pytest

from resource_management.storages.request_storage_implementation import \
    RequestStorageImplementation
from resource_management.models import AccessLevel, Request


@pytest.mark.django_db
def test_accept_request_creates_access_to_user(requests):
    # Arrange
    request_ids = [1, 2, 3]
    request_storage = RequestStorageImplementation()

    # Act
    request_storage.accept_requests(request_ids)

    # Assert
    user_access_items = AccessLevel.objects.filter(id__in=request_ids)
    assert len(user_access_items) == len(request_ids)
