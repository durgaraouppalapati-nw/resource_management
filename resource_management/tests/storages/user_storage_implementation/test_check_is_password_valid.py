import pytest

from resource_management.storages.user_implementation import \
    UserImplementation


@pytest.mark.django_db
def test_check_is_password_valid_with_correct_password_return_true(user):
    # Arrange
    user_id = 1
    password = "Durga@870"
    expected_output = True
    user_storage = UserImplementation()

    # Act
    actual_output = user_storage.check_is_password_valid(
        user_id=user_id, password=password    
    )

    # Assert
    assert expected_output == actual_output
