from typing import List

from django.contrib.auth import authenticate
from django.db.models import Prefetch

from resource_management.interactors.storages.user_interface import \
    UserInterface
from resource_management.interactors.storages.dtos import (
    UserDetailsDto, UsersWithCountDetailsDto, UserWithAccessLevelDto,
    UsersCountDto, UsersDto, UserDto
)
from resource_management.models import User, ResourceItem, AccessLevel


class UserImplementation(UserInterface):

    def check_is_username_already_exists(self, username: str) -> bool:
        return User.objects.filter(username=username).exists()

    def create_user(self, username: str, password: str) -> str:
        user = User.objects.create(username=username)
        user.set_password(password)
        user.save()
        return

    def check_is_user_admin(self, user_id: int) -> bool:
        user = User.objects.get(id=user_id)
        return user.is_admin

    def get_user_details(self, user_id: int) -> UserDetailsDto:
        user = User.objects.get(id=user_id)

        user_details_dto = UserDetailsDto(
                                          name=user.name,
                                          profile_pic=user.profile_pic,
                                          job_role=user.job_role,
                                          department=user.department,
                                          gender=user.gender
                                        )
        return user_details_dto

    def validate_username_and_password_get_user_id(
            self, username: str, password: str) -> int:
        user_id = None
        user = authenticate(
            username=username, password=password
        )
        if user:
            user_id = user.id
        
        return user_id

    def get_users_for_item(self,
            item_id: int, offset: int,
            limit: int) -> UsersWithCountDetailsDto:
        queryset = AccessLevel.objects.filter(resource_item_id=item_id)
        users = User.objects.filter(resourceitem__id=item_id)\
                        .prefetch_related(
                            Prefetch(
                                'accesslevel_set',
                                queryset=queryset,
                                to_attr='access_level'
                            )
                        )
        users_count_dto = UsersCountDto(users_count=users.count())
        users = users[offset: offset+limit]

        users_access_level_dtos = [
            self._convert_user_obj_to_user_with_access_level_dto(user)
            for user in users
        ]
        users_with_count_dto = \
            self._prepare_users_with_count_dto(
                users_count_dto=users_count_dto,
                user_dtos = users_access_level_dtos
            )

        return users_with_count_dto

    def _convert_user_obj_to_user_with_access_level_dto(
            self, user) -> UserWithAccessLevelDto:
        resource_item = user.access_level[0]
        user_with_access_level_dto = UserWithAccessLevelDto(
            name=user.name,
            job_role=user.job_role,
            department=user.department,
            access_level=resource_item.access_level,
            item_id=resource_item.resource_item_id
        )
        return user_with_access_level_dto

    def _prepare_users_with_count_dto(
            self, users_count_dto, user_dtos) -> UsersWithCountDetailsDto:
        users_with_count_dto = UsersWithCountDetailsDto(
            users_count_dto=users_count_dto,
            user_dtos=user_dtos
        )
        return users_with_count_dto

    def get_all_users(self, offset: int, limit: int) -> UsersDto:
        users = User.objects.filter(is_admin=False)
        total_users = users.count()
        users = list(users)
        users = users[offset: offset+limit]

        users_count_dto = UsersCountDto(users_count=total_users)
        user_dtos = [
            self._convert_user_obj_to_user_dto(user)
            for user in users
        ]
        users_dto = self._prepare_users_dto_with_all_user_dtos(
            user_dtos=user_dtos,
            users_count_dto=users_count_dto
        )
        return users_dto

    def _convert_user_obj_to_user_dto(self, user) -> UserDto:
        user_dto = UserDto(name=user.name,
                           profile_pic=user.profile_pic,
                           job_role=user.job_role,
                           department=user.department,
                           user_id=user.id
                           )
        return user_dto

    def _prepare_users_dto_with_all_user_dtos(self,
            user_dtos: List[UserDto],
            users_count_dto: UsersCountDto) -> UsersDto:
        users_dto = UsersDto(
            user_dtos=user_dtos,
            users_count_dto=users_count_dto
        )
        return users_dto

    def check_is_user_exists(self, user_id: int) -> bool:
        return User.objects.filter(id=user_id).exists()

    def update_profile(self, user_id: int, user_details_dto: UserDetailsDto):
        User.objects.filter(id=user_id)\
            .update(
                name=user_details_dto.name,
                profile_pic=user_details_dto.profile_pic,
                job_role=user_details_dto.job_role,
                department=user_details_dto.department,
                gender=user_details_dto.gender
            )
        return

    def check_is_password_valid(self, user_id: int, password: str) -> bool:
        user = User.objects.get(id=user_id)
        return user.check_password(password)

    def update_password(self, user_id: int, new_password: str):
        user = User.objects.get(id=user_id)
        user.set_password(new_password)
        user.save()
