import pytest

from resource_management.storages.user_implementation import \
    UserImplementation
from resource_management.interactors.storages.dtos import \
    UsersDto, UsersCountDto


@pytest.mark.django_db
def test_get_all_users_with_users_return_users_dto(users, users_dto):
    # Arrange
    offset = 0
    limit = 10
    user_storage = UserImplementation()
    expected_output = users_dto

    # Act
    actual_output = user_storage.get_all_users(offset=offset, limit=limit)

    # Assert
    assert expected_output == actual_output


@pytest.mark.django_db
def test_get_all_users_without_users_return_users_dto_empty():
    # Arrange
    offset = 0
    limit = 10
    user_storage = UserImplementation()
    users_count_dto = UsersCountDto(users_count=0)
    expected_output = UsersDto(user_dtos=[],
                               users_count_dto=users_count_dto
                              )

    # Act
    actual_output = user_storage.get_all_users(offset=offset, limit=limit)

    # Assert
    assert expected_output == actual_output
