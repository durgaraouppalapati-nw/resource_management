import pytest

from datetime import datetime

from common.dtos import (
    UserAuthTokensDTO, AccessTokenDTO, RefreshTokenDTO,
    Application
)
from resource_management.interactors.storages.dtos import (
    UserDetailsDto, ResourcesDetailsDto, ResourceDto, ItemDto,
    ItemsCountDto, UserWithAccessLevelDto, UsersCountDto,
    UserDto, UsersDto, UserWithResourceItemsDto, ResourceItemDto,
    RequestsDetailsDto, RequestsCountDto, UserRequestDto,
    ResourcesCountDto, UserResourceItemsDto, RequestStatusDto,
    GetRequestsParametersDto, ResourceMinimalDetailsDto,
    ItemMinimalDetailsDto
)
from resource_management.interactors.storages.dtos import RequestDto


@pytest.fixture()
def user_details_dto():
    user_details_dto = UserDetailsDto(name="Durga",
                                      profile_pic="www.durga.com",
                                      job_role="developer",
                                      department="Backend",
                                      gender="Male"
                                     )
    return user_details_dto


@pytest.fixture()
def user_dto():
    user_dto = UserDto(name="Durga",
                       profile_pic="www.durga.com",
                       job_role="developer",
                       department="Backend",
                       user_id=1
                    )
    return user_dto


@pytest.fixture()
def list_of_user_dtos():
    user_dtos = [
        UserDto(name="User 1",
                profile_pic="www.user1.com",
                job_role="developer",
                department="Backend",
                user_id=1
               ),
        UserDto(name="User 2",
                profile_pic="www.user2.com",
                job_role="developer",
                department="Backend",
                user_id=2
               ),
        UserDto(name="User 3",
                profile_pic="www.user3.com",
                job_role="developer",
                department="Backend",
                user_id=3
               )
    ]
    return user_dtos


@pytest.fixture()
def users_dto(list_of_user_dtos):
    users_dto = UsersDto(user_dtos=list_of_user_dtos,
                         users_count_dto=UsersCountDto(users_count=3)
                        )
    return users_dto


@pytest.fixture()
def oauth_tokens_dto():
    oauth_token_dto = UserAuthTokensDTO(
                                        user_id=1,
                                        access_token="access_token",
                                        refresh_token="refresh_token",
                                        expires_in="01-06-2020"
                                       )
    return oauth_token_dto


@pytest.fixture()
def access_token_dto():
    access_token_dto = AccessTokenDTO(
                                    access_token_id=1,
                                    token="access_token",
                                    expires="01-06-2020"
        )
    return access_token_dto


@pytest.fixture()
def application_dto():
    application = Application(application_id=1)
    return application


@pytest.fixture()
def refresh_token_dto():
    refresh_token_dto = RefreshTokenDTO(
                                        user_id=1,
                                        token="refresh_token",
                                        access_token=1,
                                        revoked="01-06-2020"
                                       )
    return refresh_token_dto


@pytest.fixture()
def resource_dtos():
    resource_dtos = [
        ResourceDto(name="Resource 1",
                    resource_pic="www.resource1/pic.com",
                    link="www.resource1.com",
                    description="This is about Resource 1",
                    resource_id=1
                    ),
        ResourceDto(name="Resource 2",
                    resource_pic="www.resource2/pic.com",
                    link="www.resource2.com",
                    description="This is about Resource 2",
                    resource_id=2
                    )
    ]
    return resource_dtos


@pytest.fixture()
def resources_count_dto():
    resources_count = ResourcesCountDto(resources_count=2)
    return resources_count


@pytest.fixture()
def resource_dto():
    resource = ResourceDto(name="Resource 1",
                            resource_pic="www.resource_pic1.com",
                            link="www.resource1.com",
                            description="This is about Resource 1",
                            resource_id=1
                           )
    return resource


@pytest.fixture()
def item_dtos(resource_dtos):
    item_dtos = [
            ItemDto(title="Item 1",
                    description="This is about Item 1",
                    link="www.item1.com",
                    item_id=1,
                    resource_id=1
                    ),
            ItemDto(title="Item 2",
                    description="This is about Item 2",
                    link="www.item1.com",
                    item_id=2,
                    resource_id=1
                    )        
    ]
    return item_dtos


@pytest.fixture()
def items_count_dto():
    items_count = ItemsCountDto(items_count=2)
    return items_count


@pytest.fixture()
def users_with_access_level_dtos():
    user_dtos = [
        UserWithAccessLevelDto(name="User 1",
                               job_role="Developer",
                               department="Backend",
                               access_level="write",
                               item_id=1
                              ),
        UserWithAccessLevelDto(name="User 2",
                               job_role="Developer",
                               department="Backend",
                               access_level="write",
                               item_id=1
                              )                
    ]
    return user_dtos


@pytest.fixture()
def users_count_dto():
    users_count = UsersCountDto(users_count=2)
    return users_count


@pytest.fixture()
def resource_items():
    resource_items = [
        ResourceItemDto(resource_name="Resource 1",
                        item_title="Item 1",
                        link="www.item1.com",
                        description="This is about item 1",
                        item_id=1,
                        access_level="write"
                        ),
        ResourceItemDto(resource_name="Resource 2",
                        item_title="Item 2",
                        link="www.item2.com",
                        description="This is about item 2",
                        item_id=2,
                        access_level="write"
                        )
    ]
    return resource_items


@pytest.fixture()
def users_with_resource_items_dto(items_count_dto, resource_items, user_dto):
    dto = UserWithResourceItemsDto(
        items_count_dto=items_count_dto,
        user_dto=user_dto,
        resource_items=resource_items
    )
    return dto


@pytest.fixture()
def users_resource_items_dto(items_count_dto, resource_items):
    dto = UserResourceItemsDto(
        items_count_dto=items_count_dto,
        resource_items=resource_items
    )
    return dto



@pytest.fixture()
def request_dtos():
    request_dtos = [
        UserRequestDto(resource_name="Resource 1",
                   item_title="Item 1",
                   access_level="read",
                   request_id=1,
                   due_datetime="2020-06-01 05:00:00",
                   user_name="User 1",
                   profile_pic="www.user1/pic.com"
                  ),
        UserRequestDto(resource_name="Resource 2",
                   item_title="Item 2",
                   access_level="read",
                   request_id=2,
                   due_datetime="2020-06-01 05:00:00",
                   user_name="User 2",
                   profile_pic="www.user2/pic.com"
                  ),
        UserRequestDto(resource_name="Resource 3",
                   item_title="Item 3",
                   access_level="read",
                   request_id=3,
                   due_datetime="2020-06-01 05:00:00",
                   user_name="User 2",
                   profile_pic="www.user2/pic.com"
                  )
    ]
    return request_dtos


@pytest.fixture()
def requests_status_dtos():
    requests_status_dtos = [
        RequestStatusDto(resource_name="Resource 1",
                         item_title="Item 1",
                         access_level="READ",
                         status="PENDING",
                         request_id=1
                        ),
        RequestStatusDto(resource_name="Resource 2",
                         item_title="Item 2",
                         access_level="READ",
                         status="ACCEPTED",
                         request_id=1
                        )
    ]
    return requests_status_dtos


@pytest.fixture()
def get_requests_parameters_dto():
    get_requests_parameters_dto = GetRequestsParametersDto(
                                                            offset=0,
                                                            limit=5,
                                                            sortby="",
                                                            filterby="",
                                                            filterby_value=""
                                                           )
    return get_requests_parameters_dto
    

@pytest.fixture()
def get_requests_parameters_dto_with_invalid_offset():
    get_requests_parameters_dto = GetRequestsParametersDto(
                                                            offset=-1,
                                                            limit=5,
                                                            sortby="",
                                                            filterby="",
                                                            filterby_value=""
                                                           )
    return get_requests_parameters_dto

@pytest.fixture()
def get_requests_parameters_dto_with_invalid_limit():
    get_requests_parameters_dto = GetRequestsParametersDto(
                                                            offset=1,
                                                            limit=-5,
                                                            sortby="",
                                                            filterby="",
                                                            filterby_value=""
                                                           )
    return get_requests_parameters_dto


@pytest.fixture()
def requests_count_dto():
    requests_count = RequestsCountDto(requests_count=5)
    return requests_count


@pytest.fixture()
def requests_details_dto(user_dto, request_dtos, requests_count_dto):
    requests_dto = RequestsDetailsDto(
                                      request_dtos=request_dtos,
                                      requests_count=requests_count_dto
                                     )
    return requests_dto


@pytest.fixture()
def resources():
    resources = [ResourceMinimalDetailsDto(resource_id=1,name="AWS")]
    return resources


@pytest.fixture()
def items():
    items = [ItemMinimalDetailsDto(item_id=1, title="Project Management")]
    return items


@pytest.fixture()
def resources_dtos_response():
    resources_dtos_response = [
        {
            "name": "Resource 1",
            "resource_pic": "www.resource1/pic.com",
            "link": "www.resource1.com",
            "description": "This is about Resource 1",
            "resource_id": 1
        },    
        {
            "name": "Resource 2",
            "resource_pic": "www.resource2/pic.com",
            "link": "www.resource2.com",
            "description": "This is about Resource 2",
            "resource_id": 2
        }
    ]
    return resources_dtos_response


@pytest.fixture()
def items_with_count_dtos_response():
    response = {
        "total_items": 2,
        "items": [
            {
                "title": "Item 1",
                "description": "This is about Item 1",
                "link": "www.item1.com",
                "item_id": 1,
            },
            {
                "title": "Item 2",
                "description": "This is about Item 2",
                "link": "www.item2.com",
                "item_id": 2,
            }
        ]
    }
    return response


@pytest.fixture()
def users_with_access_level_response():
    response = {
        "total_users": 2,
        "users": [
            {
                "name": "User 1",
                "job_role": "Developer",
                "department": "Backend",
                "access_level": "write",
                "item_id": 1  
            },
            {
                "name": "User 2",
                "job_role": "Developer",
                "department": "Backend",
                "access_level": "write",
                "item_id": 1
            }
        ]
    }
    return response


@pytest.fixture()
def list_of_users_response():
    users = [
        {
            "name": "User 1",
            "profile_pic": "www.user1.com",
            "job_role": "developer",
            "department": "Backend",
            "user_id": 1
        },
        {
            "name": "User 2",
            "profile_pic": "www.user2.com",
            "job_role": "developer",
            "department": "Backend",
            "user_id": 2
        },
        {
            "name": "User 3",
            "profile_pic": "www.user3.com",
            "job_role": "developer",
            "department": "Backend",
            "user_id": 3
        },
    ]
    return users


@pytest.fixture()
def request_dto():
    request_dto = RequestDto(resource_id=1,
                             item_id=2,
                             access_level="READ",
                             due_datetime=datetime(2020, 6, 1, 10, 0),
                             reason_for_access="Wanted to do work"
                            )
    return request_dto
