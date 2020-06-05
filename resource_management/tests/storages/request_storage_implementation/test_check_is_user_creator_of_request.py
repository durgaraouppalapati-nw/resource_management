import pytest

from resource_management.storages.request_storage_implementation import \
    RequestStorageImplementation


@pytest.mark.django_db
def test_check_is_user_creator_of_request_with_request_return_true(user_requests):
    # Arrange
    request_id = 1
    user_id = 1
    expected_output = True
    request_storage = RequestStorageImplementation()

    # Act
    actual_output = request_storage.check_is_user_creator_of_request(
        request_id=request_id, user_id=user_id
    )

    # Assert
    assert expected_output == actual_output
