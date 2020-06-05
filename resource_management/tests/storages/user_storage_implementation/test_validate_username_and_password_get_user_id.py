import pytest

from unittest.mock import create_autospec

from resource_management.storages.user_implementation import \
    UserImplementation


@pytest.mark.django_db
def test_validate_username_and_password_get_user_id_with_user_return_user_id(user):
    # Arrange
    expected_user_id = 1
    username = "Durga"
    password = "Durga@870"
    storage = UserImplementation()

    # Act
    actual_user_id = storage.validate_username_and_password_get_user_id(
        username=username, password=password
    )

    # Assert
    assert expected_user_id == actual_user_id
