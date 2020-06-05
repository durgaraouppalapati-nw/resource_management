from typing import List

from django.db.models import Prefetch, Q
from django.db import connection

from resource_management.interactors.storages.item_interface import \
    ItemInterface
from resource_management.interactors.storages.dtos import \
    ItemsWithCountDetailsDto
from resource_management.models import (
    ResourceItem, Resource, User, AccessLevel
)
from resource_management.interactors.storages.dtos import (
    ItemDto, ItemsCountDto, ItemsWithCountDetailsDto,
    ResourceDto, UserWithResourceItemsDto, UserDto, ResourceItemDto,
    UserResourceItemsDto, ResourceMinimalDetailsDto, ItemMinimalDetailsDto
)
from resource_management.constants.enums import SearchBy


class ItemStorageImplementation(ItemInterface):

    def get_items_for_resource(
            self, resource_id: int, offset: int, limit: int
            ) -> ItemsWithCountDetailsDto:
        items = ResourceItem.objects.filter(resource_id=resource_id)
        resource = Resource.objects.get(id=resource_id)
        total_items = items.count()
        required_items = items[offset:offset+limit]
        
        items_count_dto = self._prepare_items_count_dto(total_items)
        item_dtos = [
            self._convert_item_obj_to_dto(item)
            for item in required_items
        ]
        resource_dto = self._convert_resource_obj_to_dto(resource)
        items_with_count_dto = self._prepare_items_with_count_details_dto(
            items_count_dto, item_dtos, resource_dto
        )

        return items_with_count_dto

    def _prepare_items_count_dto(self, total_items: int) -> ItemsCountDto:
        items_count_dto = ItemsCountDto(items_count=total_items)
        return items_count_dto

    def _convert_item_obj_to_dto(self, item) -> ItemDto:
        item_dto = ItemDto(title=item.title,
                           description=item.description,
                           link=item.link,
                           item_id=item.id,
                           resource_id=item.resource_id
                          )
        return item_dto

    def _convert_resource_obj_to_dto(self, resource):
        resource_dto = ResourceDto(name=resource.name,
                                   resource_pic=resource.resource_pic,
                                   link=resource.link,
                                   description=resource.description,
                                   resource_id=resource.id
                                   )
        return resource_dto

    def _prepare_items_with_count_details_dto(
            self, items_count_dto, item_dtos, resource_dto
            ) -> ItemsWithCountDetailsDto:
        items_with_count_dto = ItemsWithCountDetailsDto(
                items_count_dto=items_count_dto,
                item_dtos=item_dtos,
                resource_dto=resource_dto
            )
        return items_with_count_dto

    def create_resource_item(self, resource_id: int,
            title: str, link: str, description: str):
        ResourceItem.objects.create(resource_id=resource_id,
                                    title=title,
                                    link=link,
                                    description=description
                                   )

    def check_is_resource_item_exists(self, item_id: int) -> bool:
        return ResourceItem.objects.filter(id=item_id).exists()

    def update_resource_item(self, item_id: int, title: str,
            link: str, description: str):
        item = ResourceItem.objects.get(id=item_id)
        item.title = title
        item.link = link
        item.description = description
        item.save()

    def delete_resource_items(self, item_ids: List[int]):
        ResourceItem.objects.filter(id__in=item_ids).delete()

    def get_all_resource_items_for_user(self, user_id: int,
            offset: int, limit: int) -> UserWithResourceItemsDto:
        user = User.objects.get(id=user_id)
        user_access_level = AccessLevel.objects.filter(user_id=user_id)
        resource_items = ResourceItem.objects.filter(users=user)\
                                    .prefetch_related(
                                        Prefetch(
                                            'accesslevel_set',
                                            queryset=user_access_level,
                                            to_attr='user_access_level'
                                        ),
                                        'resource'
                                    )
        total_items = resource_items.count()
        resource_items = resource_items[offset: offset+limit]
        
        
        user_with_resource_items_dto = \
            self._get_user_with_resource_items_dto(
                total_items=total_items, user=user,
                resource_items=resource_items
            )
        return user_with_resource_items_dto

    def _get_user_with_resource_items_dto(self,
            total_items: int, user, resource_items):
        items_count_dto = self._prepare_items_count_dto(total_items)
        user_dto = self._convert_user_obj_to_dto(user)
        resource_item_dtos = [
            self._convert_resource_item_obj_to_resource_item_dto(
                resource_item
            )
            for resource_item in resource_items
        ]

        user_with_resource_items_dto = \
            self._prepare_user_with_resource_items_dto(
                items_count_dto, user_dto, resource_item_dtos    
            )
        return user_with_resource_items_dto

    def _convert_user_obj_to_dto(self, user) -> UserDto:
        user_dto = UserDto(name=user.name,
                           profile_pic=user.profile_pic,
                           user_id=user.id,
                           job_role=user.job_role,
                           department=user.department
                           )
        return user_dto

    def _convert_resource_item_obj_to_resource_item_dto(self,
            resource_item) -> ResourceItemDto:
        resource_item_dto = ResourceItemDto(
            resource_name=resource_item.resource.name,
            item_title=resource_item.title,
            link=resource_item.link,
            description=resource_item.description,
            item_id=resource_item.id,
            access_level=resource_item.user_access_level[0].access_level
            )
        return resource_item_dto

    def _prepare_user_with_resource_items_dto(self,
            items_count_dto: ItemsCountDto, user_dto: UserDto,
            resource_items: List[ResourceItemDto]
            ) -> UserWithResourceItemsDto:

        user_with_resource_items_dto = UserWithResourceItemsDto(
            items_count_dto=items_count_dto,    
            user_dto=user_dto,
            resource_items=resource_items
        )
        return user_with_resource_items_dto

    def add_resource_item_to_user(self, user_id: int,
            item_id: int, access_level: str):
        AccessLevel.objects.create(
            user_id=user_id,
            resource_item_id=item_id,
            access_level=access_level
        )
        return

    def get_user_resource_items(self, user_id: int, offset: int,
            limit: int, search: str) -> UserResourceItemsDto:
        user_access_level = AccessLevel.objects.filter(user_id=user_id)
        resource_items = ResourceItem.objects\
                .filter(accesslevel__user_id=user_id)\
                .prefetch_related(
                    Prefetch(
                        'accesslevel_set',
                        queryset=user_access_level,
                        to_attr='user_access_level'
                    ),
                    'resource'
                )
        if search:
            resource_items = resource_items\
                    .filter(
                        Q(resource__name__icontains=search) |
                        Q(title__icontains=search) |
                        Q(accesslevel__access_level__icontains=search)    
                    )
        
        total_items = resource_items.count()
        resource_items = resource_items[offset: offset+limit]

        user_resource_items_dto = \
            self._get_user_resource_items_dto(
                total_items=total_items,
                resource_items=resource_items
            )
        return user_resource_items_dto

    def _get_user_resource_items_dto(self,
            total_items: int, resource_items):
        items_count_dto = self._prepare_items_count_dto(total_items)
        resource_item_dtos = [
            self._convert_resource_item_obj_to_resource_item_dto(
                resource_item
            )
            for resource_item in resource_items
        ]

        user_resource_items_dto = UserResourceItemsDto(
            items_count_dto=items_count_dto,
            resource_items=resource_item_dtos    
        )
        return user_resource_items_dto

    def search_resource_items(self, resource_id: int,
            search: str) -> List[ItemMinimalDetailsDto]:
        resource_items = ResourceItem.objects.filter(
                                Q(resource_id=resource_id) &
                                Q(title__icontains=search)
                            )
        item_dtos = [
            self._prepare_item_minimal_details_dto(resource_item)
            for resource_item in resource_items
        ]
        return item_dtos

    def _prepare_item_minimal_details_dto(self,
            resource_item) -> ItemMinimalDetailsDto:
        return ItemMinimalDetailsDto(item_id=resource_item.id,
                                     title=resource_item.title
                                    )

    def check_is_resource_item_belongs_to_resource(self,
            item_id: int, resource_id: int) -> bool:
        item = ResourceItem.objects.get(id=item_id)
        return item.resource_id == resource_id
