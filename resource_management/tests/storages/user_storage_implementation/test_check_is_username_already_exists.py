import pytest

from resource_management.storages.user_implementation import \
    UserImplementation


@pytest.mark.django_db
def test_check_is_username_already_exists_with_user_return_true(user):
    # Arrange
    username = 'Durga'
    expected_output = True
    user_storage = UserImplementation()
    
    # Act
    actual_output = user_storage.check_is_username_already_exists(
        username=username    
    )

    # Assert
    assert expected_output == actual_output
