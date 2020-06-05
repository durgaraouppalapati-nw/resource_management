import pytest

from resource_management.models import User
from resource_management.storages.user_implementation import \
    UserImplementation


@pytest.mark.django_db
def test_get_user_details_with_user_id_return_user_details_dto(
        user, user_details_dto):
    # Arrange
    user_id = 1
    expected_user_details_dto = user_details_dto
    storage = UserImplementation()

    # Act
    actual_user_details_dto = storage.get_user_details(user_id=user_id)

    # Assert
    assert expected_user_details_dto == actual_user_details_dto
