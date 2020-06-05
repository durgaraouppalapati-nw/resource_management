import pytest
import datetime

from common.dtos import UserAuthTokensDTO
from resource_management.interactors.storages.dtos import (
    ResourceDto, ItemDto, ItemsCountDto, UserWithAccessLevelDto,
    UsersCountDto, UsersWithCountDetailsDto, RequestsCountDto,
    UserRequestDto, RequestsDetailsDto, ResourcesCountDto,
    UserDto, UsersDto, UsersCountDto, ResourceItemDto,
    UserResourceItemsDto, ItemsCountDto, RequestStatusDto, RequestsCountDto,
    ResourceMinimalDetailsDto, ItemMinimalDetailsDto
)

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
def resource_dtos():
    resource_dtos = [
        ResourceDto(name="Resource 1",
                    resource_pic="www.resource_pic1.com",
                    link="www.resource1.com",
                    description="This is about Resource 1",
                    resource_id=1
                   ),
        ResourceDto(name="Resource 2",
                    resource_pic="www.resource_pic2.com",
                    link="www.resource2.com",
                    description="This is about Resource 2",
                    resource_id=2
                   ),
        ResourceDto(name="Resource 3",
                    resource_pic="www.resource_pic3.com",
                    link="www.resource3.com",
                    description="This is about Resource 3",
                    resource_id=3
                   )
    ]
    return resource_dtos


@pytest.fixture()
def resources_count_dto():
    resources_count = ResourcesCountDto(resources_count=3)
    return resources_count


@pytest.fixture()
def item_dtos():
    item_dtos = [
        ItemDto(title="Item 1",
                link="www.item1.com",
                description="This is about Item 1",
                resource_id=1,
                item_id=1
                ),
        ItemDto(title="Item 2",
                link="www.item2.com",
                description="This is about Item 2",
                resource_id=1,
                item_id=2
                )
    ]
    return item_dtos


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
def items_count_dto():
    items_count_dto = ItemsCountDto(items_count=2)
    return items_count_dto


@pytest.fixture()
def users_count_dto():
    users_count_dto = UsersCountDto(users_count=3)
    return users_count_dto


@pytest.fixture()
def users_with_access_level_dto():
    users = [
        UserWithAccessLevelDto(name='User 1',
                               job_role="Developer",
                               department="Backend",
                               access_level="read",
                               item_id= 1
                               ),
        UserWithAccessLevelDto(name='User 2',
                               job_role="Developer",
                               department="Backend",
                               access_level="read",
                               item_id= 1
                               )
    ]
    return users


@pytest.fixture()
def users_with_count_dto(users_count_dto, users_with_access_level_dto):
    users_dto = UsersWithCountDetailsDto(users_count_dto=users_count_dto,
                                         user_dtos=users_with_access_level_dto)
    return users_dto


@pytest.fixture()
def user_request_dtos():
    user_request_dtos = [
                        UserRequestDto(request_id=1,
                                      resource_name="Resource 1",
                                      item_title="Item 1",
                                      access_level="read",
                                      due_datetime=datetime.datetime(2020, 6, 1, 5, 0),
                                      user_name="User 1",
                                      profile_pic="www.user1/pic.com"
                                     ),
                        UserRequestDto(request_id=2,
                                      resource_name="Resource 1",
                                      item_title="Item 2",
                                      access_level="read",
                                      due_datetime=datetime.datetime(2020, 6, 1, 5, 0),
                                      user_name="User 2",
                                      profile_pic="www.user2/pic.com"
                                     ),
                        UserRequestDto(request_id=3,
                                      resource_name="Resource 1",
                                      item_title="Item 3",
                                      access_level="read",
                                      due_datetime=datetime.datetime(2020, 6, 1, 5, 0),
                                      user_name="User 3",
                                      profile_pic="www.user3/pic.com"
                                     )
                        ]
    return user_request_dtos


@pytest.fixture()
def requests_count_dto():
    requests_count = RequestsCountDto(requests_count=3)
    return requests_count


@pytest.fixture()
def requests_details_dto(requests_count_dto, user_request_dtos):
    requests_details_dto = RequestsDetailsDto(
                                              requests_count=requests_count_dto,
                                              request_dtos=user_request_dtos
                                              )
    return requests_details_dto


@pytest.fixture()
def list_of_user_dtos():
    user_dtos = [
        UserDto(name="User 1",
                profile_pic="www.user1/pic.com",
                job_role="Developer",
                department="Backend",
                user_id=1
               ),
        UserDto(name="User 2",
                profile_pic="www.user2/pic.com",
                job_role="Developer",
                department="Backend",
                user_id=2
               ),
        UserDto(name="User 3",
                profile_pic="www.user3/pic.com",
                job_role="Developer",
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
def resource_items_dtos():
    resource_item_dtos = [
        ResourceItemDto(resource_name="GitHub",
                        item_title="Essential Kit",
                        link="www.item1.com",
                        description="This is about Item 1",
                        access_level="WRITE",
                        item_id=1
                        ),
        ResourceItemDto(resource_name="GitHub",
                        item_title="Reporting Portal",
                        link="www.item3.com",
                        description="This is about Item 3",
                        access_level="READ",
                        item_id=3
                        )
    ]
    return resource_item_dtos

@pytest.fixture()
def user_resource_items_dto(
        resource_items_dtos):
    user_resource_items_dto = UserResourceItemsDto(
        items_count_dto=ItemsCountDto(items_count=2),
        resource_items=resource_items_dtos
    )
    return user_resource_items_dto


@pytest.fixture()
def user_requests_status_dtos():
    request_dtos = [
        RequestStatusDto(resource_name="GitHub",
                         item_title="Smart Food Management",
                         access_level="READ",
                         request_id=1,
                         status="REJECTED"
                        ),
        RequestStatusDto(resource_name="BitBucket",
                         item_title="Covid19",
                         access_level="READ",
                         request_id=3,
                         status="ACCEPTED"
                        ),
        RequestStatusDto(resource_name="Aws",
                         item_title="Covid19",
                         access_level="READ",
                         request_id=5,
                         status="ACCEPTED"
                        )
    ]
    return request_dtos


@pytest.fixture()
def search_resources():
    return [
                ResourceMinimalDetailsDto(resource_id=1, name='GitHub'),
                ResourceMinimalDetailsDto(resource_id=2, name='BitBucket')
            ]


@pytest.fixture()
def search_resource_items():
    return [
                ItemMinimalDetailsDto(item_id=10, title='Project Management'),
                ItemMinimalDetailsDto(item_id=12, title='cloud9')
            ]


@pytest.fixture()
def search_resources_response():
    response = [
        {
            "resource_id": 1,
            "resource_name": "GitHub"
        },
        {
            "resource_id": 2,
            "resource_name": "BitBucket"
        }
    ]
    return response


@pytest.fixture()
def search_resource_items_response():
    response = [
        {
            "item_id": 10,
            "item_title": "Project Management"
        },
        {
            "item_id": 12,
            "item_title": "cloud9"
        }
    ]
    return response


@pytest.fixture()
def users_response():
    users_response = {
        "total_users": 3,
        "users_details": [
            {
                "name": "User 1",
                "profile_pic": "www.user1/pic.com",
                "job_role": "Developer",
                "department": "Backend",
                "user_id": 1
            },
            {
                "name": "User 2",
                "profile_pic": "www.user2/pic.com",
                "job_role": "Developer",
                "department": "Backend",
                "user_id": 2
            },
            {
                "name": "User 3",
                "profile_pic": "www.user3/pic.com",
                "job_role": "Developer",
                "department": "Backend",
                "user_id": 3
            }
        ]
    }
    return users_response


@pytest.fixture()
def resource_dtos_response():
    resource_dtos_response = {
        "total_resources": 3,
        "resources_details": [
            {
                "name": "Resource 1",
                "resource_pic": "www.resource_pic1.com",
                "link": "www.resource1.com",
                "description": "This is about Resource 1",
                "resource_id": 1
            },
            {
                "name": "Resource 2",
                "resource_pic": "www.resource_pic2.com",
                "link": "www.resource2.com",
                "description": "This is about Resource 2",
                "resource_id": 2
            },
            {
                "name": "Resource 3",
                "resource_pic": "www.resource_pic3.com",
                "link": "www.resource3.com",
                "description": "This is about Resource 3",
                "resource_id": 3
            }
        ]
    }
    return resource_dtos_response


@pytest.fixture()
def item_dtos_response():
    item_dtos_response = {
        "total_items": 2,
        "resource": {
            "name": "Resource 1",
            "resource_pic": "www.resource_pic1.com",
            "link": "www.resource1.com",
            "description": "This is about Resource 1",
            "resource_id": 1
        },
        "items": [
            {
                "title": "Item 1",
                "link": "www.item1.com",
                "description": "This is about Item 1",
                "item_id": 1
            },
            {
                "title": "Item 2",
                "link": "www.item2.com",
                "description": "This is about Item 2",
                "item_id": 2
            }
        ]
    }
    return item_dtos_response


@pytest.fixture()
def get_users_for_item_response():
    response = {
        "total_users": 3,
        "users": [
            {
                "name": "User 1",
                "job_role": "Developer",
                "department": "Backend",
                "access_level": "read"
            },
            {
                "name": "User 2",
                "job_role": "Developer",
                "department": "Backend",
                "access_level": "read"
            }
        ]
    }
    return response


@pytest.fixture()
def resource_dict():
    resource_dict = {
        "name": "Resource 1",
        "resource_pic": "www.resource_pic1.com",
        "link": "www.resource1.com",
        "description": "This is about Resource 1",
        "resource_id": 1
    }
    return resource_dict


@pytest.fixture()
def requests_details_response():
    requests_details_response = {
        'total_requests': 3,
        'requests_details': [
            {
                'request_id': 1,
                'resource_name': "Resource 1",
                'item_title': "Item 1",
                'access_level': "read",
                'due_datetime': "01/06/2020 05:00 AM",
                'user_name': "User 1",
                'profile_pic': "www.user1/pic.com"
            },
            {
                'request_id': 2,
                'resource_name': "Resource 1",
                'item_title': "Item 2",
                'access_level': "read",
                'due_datetime': "01/06/2020 05:00 AM",
                'user_name': "User 2",
                'profile_pic': "www.user2/pic.com"
            },
            {
                'request_id': 3,
                'resource_name': "Resource 1",
                'item_title': "Item 3",
                'access_level': "read",
                'due_datetime': "01/06/2020 05:00 AM",
                'user_name': "User 3",
                'profile_pic': "www.user3/pic.com"
            }
        ]
    }
    return requests_details_response


@pytest.fixture()
def user_resource_items_response():
    item_dtos_response = {
        "total_resource_items": 2,
        "resource_items": [
            {
                "resource_name": "GitHub",
                "item_title": "Essential Kit",
                "link": "www.item1.com",
                "access_level": "WRITE",
                "item_id": 1
            },
            {
                "resource_name": "GitHub",
                "item_title": "Reporting Portal",
                "link": "www.item3.com",
                "access_level": "READ",
                "item_id": 3
            }
        ]
    }
    return item_dtos_response


@pytest.fixture()
def requests_status_response():
    response = {
        "total_requests": 3,
        "requests_details": [
            {
                "resource_name": "GitHub",
                "item_title": "Smart Food Management",
                "access_level": "READ",
                "request_id": 1,
                "status": "REJECTED"
            },
            {
                "resource_name": "BitBucket",
                "item_title": "Covid19",
                "access_level": "READ",
                "request_id": 3,
                "status": "ACCEPTED"
            },
            {
                "resource_name": "Aws",
                "item_title": "Covid19",
                "access_level": "READ",
                "request_id": 5,
                "status": "ACCEPTED"
            }
        ]
    }
    return response
