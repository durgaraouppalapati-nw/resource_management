from dataclasses import dataclass
from typing import List
from datetime import datetime


@dataclass
class UserDetailsDto:
    name: str
    profile_pic: str
    job_role: str
    department: str
    gender: str


@dataclass
class UserDto:
    name: str
    profile_pic: str
    job_role: str
    department: str
    user_id: int


@dataclass
class UserMinimalDetailsDto:
    name: str
    profile_pic: str
    user_id: int


@dataclass
class UserWithAccessLevelDto:
    name: str
    job_role: int
    department: int
    access_level: str
    item_id: int


@dataclass
class ResourceDto:
    name: str
    resource_pic: str
    link: str
    description: str
    resource_id: int


@dataclass
class ItemDto:
    title: str
    description: str
    link: str
    item_id: int
    resource_id: int


@dataclass
class ResourceItemDto:
    item_title: str
    resource_name: str
    access_level: str
    link: str
    description: str
    item_id: int


@dataclass
class ResourcesCountDto:
    resources_count: int

@dataclass
class ItemsCountDto:
    items_count: int


@dataclass
class UsersCountDto:
    users_count: int


@dataclass
class RequestsCountDto:
    requests_count: int


@dataclass
class ResourcesDetailsDto:
    resource_dtos: List[ResourceDto]
    resources_count_dto: ResourcesCountDto


@dataclass
class ItemsWithCountDetailsDto:
    items_count_dto: ItemsCountDto
    item_dtos: List[ItemDto]
    resource_dto: ResourceDto


@dataclass
class UsersWithCountDetailsDto:
    users_count_dto: UsersCountDto
    user_dtos: List[UserWithAccessLevelDto]


@dataclass
class UsersDto:
    user_dtos: List[UserDto]
    users_count_dto: UsersCountDto


@dataclass
class UserWithResourceItemsDto:
    items_count_dto: ItemsCountDto
    user_dto: UserDto
    resource_items: List[ResourceItemDto]


@dataclass
class UserResourceItemsDto:
    items_count_dto: ItemsCountDto
    resource_items: List[ResourceItemDto]


@dataclass
class UserRequestDto:
    request_id: int
    resource_name: str
    item_title: str
    access_level: str
    due_datetime: datetime
    user_name: str
    profile_pic: str


@dataclass
class RequestsDetailsDto:
    request_dtos: List[UserRequestDto]
    requests_count: RequestsCountDto


@dataclass
class GetRequestsParametersDto:
    offset: int
    limit: int
    sortby: str
    filterby: str
    filterby_value: str


@dataclass
class RequestStatusDto:
    resource_name: str
    item_title: str
    request_id: int
    access_level: str
    status: str


@dataclass
class RequestDto:
    resource_id: str
    item_id: str
    access_level: str
    due_datetime: datetime
    reason_for_access: str


@dataclass
class ResourceMinimalDetailsDto:
    resource_id: int
    name: str


@dataclass
class ItemMinimalDetailsDto:
    item_id: int
    title: str


