import pytest

from resource_management.storages.user_implementation import \
    UserImplementation


@pytest.mark.django_db
def test_check_is_user_exists_with_users_return_true(users):
    # Arrange
    user_id = 1
    user_storage = UserImplementation()
    expected_output = True

    # Act
    actual_output = user_storage.check_is_user_exists(user_id=user_id)

    # Assert
    assert expected_output == actual_output
