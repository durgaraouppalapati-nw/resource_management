import pytest

from resource_management.storages.user_implementation import \
    UserImplementation
from resource_management.models import User


@pytest.mark.django_db
def test_update_password_updates_with_new_password(user):
    # Arrange
    user_id = 1
    new_password = "Durga@123"
    user_storage = UserImplementation()

    # Act
    user_storage.update_password(
        user_id=user_id, new_password=new_password    
    )

    # Assert
    user = User.objects.get(id=user_id)
    assert user.check_password(new_password) == True
