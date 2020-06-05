import pytest

from resource_management.storages.user_implementation import \
    UserImplementation
from resource_management.models import User


@pytest.mark.django_db
def test_create_user_with_details_creates_user_in_db():
    # Arrange
    username = "durga"
    password = "durga@123"
    expected_output = True
    user_storage = UserImplementation()

    # Act
    user_storage.create_user(username=username, password=password)

    # Assert
    actual_output = \
        User.objects.filter(username=username).exists()

    assert expected_output == actual_output
