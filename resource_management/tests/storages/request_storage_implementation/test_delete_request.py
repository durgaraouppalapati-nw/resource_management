import pytest

from resource_management.storages.request_storage_implementation import \
    RequestStorageImplementation
from resource_management.models import Request


@pytest.mark.django_db
def test_delete_request_with_request_deltes_request(user_requests):
    # Arrange
    request_id = 1
    expected_output = False
    request_storage = RequestStorageImplementation()

    # Act
    actual_output = request_storage.delete_request(
        request_id=request_id
    )

    # Assert
    actual_output = Request.objects.filter(id=request_id).exists()
    assert expected_output == actual_output
