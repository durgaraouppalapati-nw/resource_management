from typing import List

from resource_management.interactors.storages.resource_interface \
    import ResourceInterface
from resource_management.interactors.storages.dtos import (
    ResourcesDetailsDto, ResourceDto, ResourcesCountDto,
    ResourceMinimalDetailsDto
)
from resource_management.models import Resource, User


class ResourceStorageImplementation(ResourceInterface):

    def get_all_resources(self,
            offset: int, limit: int) -> ResourcesDetailsDto:
        resources = Resource.objects.all()
        total_resources = resources.count()
        resources = resources[offset: offset+limit]

        resource_dtos = [
            self._convert_resource_obj_to_dto(resource)
            for resource in resources
        ]
        resources_count_dto = ResourcesCountDto(
            resources_count=total_resources
        )
        resources_details_dto = self._prepare_resources_details_dto(
            resource_dtos=resource_dtos,
            resources_count_dto=resources_count_dto
        )
        return resources_details_dto

    def _convert_resource_obj_to_dto(self, resource) -> ResourceDto:
        resource_dto = ResourceDto(name=resource.name,
                                   resource_pic=resource.resource_pic,
                                   link=resource.link,
                                   description=resource.description,
                                   resource_id=resource.id
                                   )
        return resource_dto

    def _prepare_resources_details_dto(
            self, resource_dtos: List[ResourceDto],
            resources_count_dto: ResourcesCountDto
            ) -> ResourcesDetailsDto:
        resources_details_dto = ResourcesDetailsDto(
            resource_dtos=resource_dtos,
            resources_count_dto=resources_count_dto
        )
        return resources_details_dto
    
    def check_is_user_admin(self, user_id: int) -> bool:
        user = User.objects.get(id=user_id)
        is_admin = user.is_admin
        return is_admin
    
    def check_is_resource_exists(self,
            resource_id: int):
        return Resource.objects.filter(id=resource_id).exists()
    
    def update_resource_and_get_dto(self, 
            resource_id: int, name: str, resource_pic: str, link: str,
            description: str):
        resource = Resource.objects.get(id=resource_id)
        resource.name = name
        resource.resource_pic = resource_pic
        resource.link = link
        resource.description = description
        resource.save()
        resource_dto = self._convert_resource_obj_to_dto(resource)
        return resource_dto
    
    def delete_resource(self, resource_id: int):
        Resource.objects.filter(id=resource_id).delete()

    def check_is_resource_name_already_exists(self, resource_name: str) ->bool:
        return Resource.objects.filter(name=resource_name).exists()

    def create_resource(self, name: str,
            resource_pic: str, link: str, description: str):
        Resource.objects.create(
                                name=name,
                                resource_pic=resource_pic,
                                link=link,
                                description=description
                                )
        return

    def search_resources(self, search: str) -> List[ResourceMinimalDetailsDto]:
        resources = Resource.objects.filter(name__icontains=search)
        resource_dtos = [
            self._prepare_resource_minimal_details_dto(resource)
            for resource in resources
        ]
        return resource_dtos

    def _prepare_resource_minimal_details_dto(self,
            resource) -> ResourceMinimalDetailsDto:
        return ResourceMinimalDetailsDto(resource_id=resource.id,
                                         name=resource.name
                                        )
