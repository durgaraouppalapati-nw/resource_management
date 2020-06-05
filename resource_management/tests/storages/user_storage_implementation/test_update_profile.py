import pytest

from resource_management.storages.user_implementation import \
    UserImplementation
from resource_management.models import User
from resource_management.interactors.storages.dtos import UserDetailsDto


@pytest.mark.django_db
def test_update_profile_with_details_updates_user_profile(user):
    # Arrange
    user_id = 1
    name = "User 1"
    profile_pic = ""
    job_role = "Frontend Developer"
    department = "Frontend"
    gender = "FEMALE"

    user_details_dto = UserDetailsDto(name=name,
                                      profile_pic=profile_pic,
                                      job_role=job_role,
                                      department=department,
                                      gender=gender
                                     )
    user_storage = UserImplementation()

    # Act
    user_storage.update_profile(
        user_id=user_id, user_details_dto=user_details_dto
    )

    # Act
    user = User.objects.get(id=user_id)
    assert user.name == name
    assert user.profile_pic == profile_pic
    assert user.job_role == job_role
    assert user.department == department
    assert user.gender == gender
