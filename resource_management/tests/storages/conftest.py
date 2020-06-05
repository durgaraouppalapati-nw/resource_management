import pytest
import datetime

from resource_management.models import (
    User, Resource, ResourceItem, AccessLevel, Request
)
from resource_management.interactors.storages.dtos import (
    UserDetailsDto, ResourceDto, ResourcesDetailsDto,
    ItemDto, ItemsCountDto, UsersCountDto, UserWithAccessLevelDto,
    UsersWithCountDetailsDto, UserDto, UsersDto, ResourceItemDto,
    UserWithResourceItemsDto, RequestsCountDto, UserRequestDto,
    GetRequestsParametersDto, ResourcesCountDto, UserResourceItemsDto,
    RequestStatusDto, ResourceMinimalDetailsDto, ItemMinimalDetailsDto,
    RequestDto
)


@pytest.fixture()
def user():
    user = User.objects.create(
        username="Durga",
        name="Durga",
        profile_pic="www.durga.com",
        job_role="developer",
        department="Backend",
        gender="Male"
    )
    user.set_password("Durga@870")
    user.save()
    return user


@pytest.fixture()
def users():
    users = [
        {
            "username": "user1",
            "name": "User 1",
            "profile_pic": "https://image.shutterstock.com/image-vector/male-user-account-profile-circle-600w-467503055.jpg",
            "job_role": "Developer",
            "department": "Backend",
            "gender": "Male",
            "is_admin": "False"
        },
        {
            "username": "user2",
            "name": "User 2",
            "profile_pic": "https://image.shutterstock.com/image-vector/male-user-account-profile-circle-600w-467503055.jpg",
            "job_role": "Developer",
            "department": "Backend",
            "gender": "Male",
            "is_admin": "False"
        },
        {
            "username": "user3",
            "name": "User 3",
            "profile_pic": "https://image.shutterstock.com/image-vector/male-user-account-profile-circle-600w-467503055.jpg",
            "job_role": "Developer",
            "department": "Backend",
            "gender": "Male",
            "is_admin": "False"
        }
    ]

    users_list = []
    for user in users:
        users_list.append(
                            User(name=user['name'],
                                 username=user['username'],
                                 profile_pic=user['profile_pic'],
                                 job_role=user['job_role'],
                                 department=user['department'],
                                 gender=user['gender'],
                                 is_admin=user['is_admin']
                                 )
                        )
    User.objects.bulk_create(users_list)
    
    
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
def resources():
    resources = [
        {
            "name": "Resource 1",
            "resource_pic": "www.resource_pic1.com",
            "link": "www.resource1.com",
            "description": "This is about Resource 1"
        },
        {
            "name": "Resource 2",
            "resource_pic": "www.resource_pic2.com",
            "link": "www.resource2.com",
            "description": "This is about Resource 2"
        },
        {
            "name": "Resource 3",
            "resource_pic": "www.resource_pic3.com",
            "link": "www.resource3.com",
            "description": "This is about Resource 3"
        }
    ]

    resources_list = []
    for resource in resources:
        resources_list.append(
            Resource(name=resource['name'],
                     resource_pic=resource['resource_pic'],
                     link=resource['link'],
                     description=resource['description']
                     )
        )
    Resource.objects.bulk_create(resources_list)


@pytest.fixture()
def resource():
    Resource.objects.create(name="Resource 1",
                            resource_pic="www.resource_pic1.com",
                            link="www.resource1.com",
                            description="This is about Resource 1",
                            )

@pytest.fixture()
def updated_resource_dto():
    resource_dto = ResourceDto(name="Resource_1",
                               resource_pic="www.resource/pic.com",
                               link="www.resource.com",
                               description="This is Resource 1",
                               resource_id=1
                              )
    return resource_dto


@pytest.fixture()
def items(resources):
    items = [
        {
            "title": "Item 1",
            "link": "www.item1.com",
            "description": "This is about Item 1",
            "resource_id": 1
        },
        {
            "title": "Item 2",
            "link": "www.item2.com",
            "description": "This is about Item 2",
            "resource_id": 1
        },
        {
            "title": "Item 3",
            "link": "www.item3.com",
            "description": "This is about Item 3",
            "resource_id": 1
        },
    ]

    items_list = []
    for item in items:
        items_list.append(
            ResourceItem(title=item['title'],
                 link=item['link'],
                 description=item['description'],
                 resource_id=item['resource_id']
                )    
        )
    ResourceItem.objects.bulk_create(items_list)


@pytest.fixture()
def resource_items(users, items):
    resource_items = [
        {
            "user_id": 1,
            "resource_item_id": 1,
            "access_level": "read"
        },
        {
            "user_id": 2,
            "resource_item_id": 1,
            "access_level": "read"
        },
        {
            "user_id": 3,
            "resource_item_id": 1,
            "access_level": "read"
        }
    ]

    access_level_list = []
    for resource in resource_items:
        access_level_list.append(
            AccessLevel(user_id=resource['user_id'],
                        resource_item_id=resource['resource_item_id'],
                        access_level=resource['access_level']
                       )
        )
    AccessLevel.objects.bulk_create(access_level_list)


@pytest.fixture()
def resource_items_for_user(users, items):
    resource_items = [
        {
            "user_id": 1,
            "resource_item_id": 1,
            "access_level": "write"
        },
        {
            "user_id": 1,
            "resource_item_id": 2,
            "access_level": "read"
        },
        {
            "user_id": 1,
            "resource_item_id": 3,
            "access_level": "read"
        }
    ]

    access_level_list = []
    for resource in resource_items:
        access_level_list.append(
            AccessLevel(user_id=resource['user_id'],
                        resource_item_id=resource['resource_item_id'],
                        access_level=resource['access_level']
                       )
        )
    AccessLevel.objects.bulk_create(access_level_list)


@pytest.fixture()
def requests(users, resources, items, resource_items):
    requests = [
        {
            'user_id': 1,
            'resource_id': 1,
            'resource_item_id': 1,
            'access_level': 'read',
            'due_datetime': '2020-06-01 05:00:00',
            'reason_for_access': 'I want data to do something',
        },
        {
            'user_id': 2,
            'resource_id': 1,
            'resource_item_id': 2,
            'access_level': 'read',
            'due_datetime': '2020-06-01 05:00:00',
            'reason_for_access': 'I want data to do something',
        },
        {
            'user_id': 3,
            'resource_id': 1,
            'resource_item_id': 3,
            'access_level': 'read',
            'due_datetime': '2020-06-01 05:00:00',
            'reason_for_access': 'I want data to do something',
        },
    ]
    
    requests_list = []
    for request in requests:
        requests_list.append(
            Request(user_id=request['user_id'],
                    resource_id=request['resource_id'],
                    resource_item_id=request['resource_item_id'],
                    access_level=request['access_level'],
                    due_datetime=request['due_datetime'],
                    reason_for_access=request['reason_for_access']
                   )
        )
    Request.objects.bulk_create(requests_list)


@pytest.fixture()
def create_requests(users, resources, items, resource_items):
    requests = [
        {
            'user_id': 1,
            'resource_id': 1,
            'resource_item_id': 1,
            'access_level': 'read',
            'due_datetime': '2020-06-01 05:00:00',
            'reason_for_access': 'I want data to do something',
        },
        {
            'user_id': 2,
            'resource_id': 1,
            'resource_item_id': 2,
            'access_level': 'write',
            'due_datetime': '2020-06-01 06:00:00',
            'reason_for_access': 'I want data to do something',
        },
        {
            'user_id': 3,
            'resource_id': 1,
            'resource_item_id': 3,
            'access_level': 'read',
            'due_datetime': '2020-08-01 05:00:00',
            'reason_for_access': 'I want data to do something',
        },
    ]
    
    requests_list = []
    for request in requests:
        requests_list.append(
            Request(user_id=request['user_id'],
                    resource_id=request['resource_id'],
                    resource_item_id=request['resource_item_id'],
                    access_level=request['access_level'],
                    due_datetime=request['due_datetime'],
                    reason_for_access=request['reason_for_access']
                   )
        )
    Request.objects.bulk_create(requests_list)


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
def resources_details_dto(resource_dtos, resources_count_dto):
    resources_details_dto = ResourcesDetailsDto(resource_dtos=resource_dtos,
                                                resources_count_dto=resources_count_dto
                                               )
    return resources_details_dto


@pytest.fixture()
def resources_details_dto_with_empty(resource_dtos):
    resources_details_dto = ResourcesDetailsDto(resource_dtos=[],
                                                resources_count_dto=ResourcesCountDto(resources_count=0)
                                                )
    return resources_details_dto


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
    items_count_dto = ItemsCountDto(items_count=3)
    return items_count_dto


@pytest.fixture()
def items_zro_count_dto():
    items_count_dto = ItemsCountDto(items_count=0)
    return items_count_dto


@pytest.fixture()
def users_count_dto():
    users_count_dto = UsersCountDto(users_count=3)
    return users_count_dto


@pytest.fixture()
def requests_count_dto():
    requests_count = RequestsCountDto(requests_count=3)
    return requests_count


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
def user_requests_dtos():
    user_request_dtos = [
                        UserRequestDto(request_id=3,
                                      resource_name="Resource 1",
                                      item_title="Item 3",
                                      access_level="read",
                                      due_datetime=datetime.datetime(2020, 8, 1, 5, 0),
                                      user_name="User 3",
                                      profile_pic="www.user3/pic.com"
                                     ),
                        UserRequestDto(request_id=2,
                                      resource_name="Resource 1",
                                      item_title="Item 2",
                                      access_level="read",
                                      due_datetime=datetime.datetime(2020, 6, 1, 6, 0),
                                      user_name="User 2",
                                      profile_pic="www.user2/pic.com"
                                     ),
                        UserRequestDto(request_id=1,
                                      resource_name="Resource 1",
                                      item_title="Item 1",
                                      access_level="read",
                                      due_datetime=datetime.datetime(2020, 6, 1, 5, 0),
                                      user_name="User 1",
                                      profile_pic="www.user1/pic.com"
                                     )
                        ]
    return user_request_dtos


@pytest.fixture()
def users_requests_dtos():
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
                                      access_level="write",
                                      due_datetime=datetime.datetime(2020, 6, 1, 6, 0),
                                      user_name="User 2",
                                      profile_pic="www.user2/pic.com"
                                     ),
                        UserRequestDto(request_id=3,
                                      resource_name="Resource 1",
                                      item_title="Item 3",
                                      access_level="read",
                                      due_datetime=datetime.datetime(2020, 8, 1, 5, 0),
                                      user_name="User 3",
                                      profile_pic="www.user3/pic.com"
                                     ),
                        ]
    return user_request_dtos


@pytest.fixture()
def users_requests_with_sort_dtos():
    user_request_dtos = [
                        UserRequestDto(request_id=1,
                                      resource_name="Resource 1",
                                      item_title="Item 1",
                                      access_level="read",
                                      due_datetime=datetime.datetime(2020, 6, 1, 5, 0),
                                      user_name="User 1",
                                      profile_pic="www.user1/pic.com"
                                     ),
                        UserRequestDto(request_id=3,
                                      resource_name="Resource 1",
                                      item_title="Item 3",
                                      access_level="read",
                                      due_datetime=datetime.datetime(2020, 8, 1, 5, 0),
                                      user_name="User 3",
                                      profile_pic="www.user3/pic.com"
                                     ),
                        UserRequestDto(request_id=2,
                                      resource_name="Resource 1",
                                      item_title="Item 2",
                                      access_level="write",
                                      due_datetime=datetime.datetime(2020, 6, 1, 6, 0),
                                      user_name="User 2",
                                      profile_pic="www.user2/pic.com"
                                     )
                        ]
    return user_request_dtos


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
def get_requests_filterby_name_dto():
    get_requests_parameters_dto = GetRequestsParametersDto(
                                                            offset=0,
                                                            limit=5,
                                                            sortby="",
                                                            filterby="NAME",
                                                            filterby_value="1"
                                                           )
    return get_requests_parameters_dto


@pytest.fixture()
def get_requests_filterby_resource_name_dto():
    get_requests_parameters_dto = GetRequestsParametersDto(
                                                            offset=0,
                                                            limit=5,
                                                            sortby="",
                                                            filterby="RESOURCE",
                                                            filterby_value="Resource 1"
                                                           )
    return get_requests_parameters_dto


@pytest.fixture()
def get_requests_sortby_date_dto():
    get_requests_parameters_dto = GetRequestsParametersDto(
                                                            offset=0,
                                                            limit=5,
                                                            sortby="DUE_DATETIME",
                                                            filterby="",
                                                            filterby_value=""
                                                           )
    return get_requests_parameters_dto


@pytest.fixture()
def get_requests_sortby_resource_dto():
    get_requests_parameters_dto = GetRequestsParametersDto(
                                                            offset=0,
                                                            limit=5,
                                                            sortby="RESOURCE",
                                                            filterby="",
                                                            filterby_value=""
                                                           )
    return get_requests_parameters_dto


@pytest.fixture()
def get_requests_sortby_item_dto():
    get_requests_parameters_dto = GetRequestsParametersDto(
                                                            offset=0,
                                                            limit=5,
                                                            sortby="RESOURCE",
                                                            filterby="",
                                                            filterby_value=""
                                                           )
    return get_requests_parameters_dto


@pytest.fixture()
def get_requests_sortby_name_dto():
    get_requests_parameters_dto = GetRequestsParametersDto(
                                                            offset=0,
                                                            limit=5,
                                                            sortby="NAME",
                                                            filterby="",
                                                            filterby_value=""
                                                           )
    return get_requests_parameters_dto


@pytest.fixture()
def get_requests_filterby_access_level_dto():
    get_requests_parameters_dto = GetRequestsParametersDto(
                                                            offset=0,
                                                            limit=5,
                                                            sortby="",
                                                            filterby="ACCESSLEVEL",
                                                            filterby_value="read"
                                                           )
    return get_requests_parameters_dto


@pytest.fixture()
def requests_count_filterby_name_dto():
    requests_count = RequestsCountDto(requests_count=1)
    return requests_count


@pytest.fixture()
def user_filterby_name_request_dtos():
    user_request_dtos = [
                        UserRequestDto(request_id=1,
                                      resource_name="Resource 1",
                                      item_title="Item 1",
                                      access_level="read",
                                      due_datetime=datetime.datetime(2020, 6, 1, 5, 0),
                                      user_name="User 1",
                                      profile_pic="www.user1/pic.com"
                                     )
                        ]
    return user_request_dtos


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
def user_dto():
    user_dto = UserDto(name="User 1",
                       profile_pic="www.user1/pic.com",
                       job_role="Developer",
                       department="Backend",
                       user_id=1
                      )
    return user_dto


@pytest.fixture()
def resource_item_dtos():
    resource_item_dtos = [
        ResourceItemDto(resource_name="Resource 1",
                        item_title="Item 1",
                        link="www.item1.com",
                        description="This is about Item 1",
                        access_level="write",
                        item_id=1
                        ),
        ResourceItemDto(resource_name="Resource 1",
                        item_title="Item 2",
                        link="www.item2.com",
                        description="This is about Item 2",
                        access_level="read",
                        item_id=2
                        )
    ]
    return resource_item_dtos


@pytest.fixture()
def user_with_resource_items_dto(items_count_dto, user_dto, resource_item_dtos):
    dto = UserWithResourceItemsDto(items_count_dto=items_count_dto,
                                   user_dto=user_dto,
                                   resource_items=resource_item_dtos
                                  )
    return dto


@pytest.fixture()
def create_resources():
    resources = [
        {
            "name": "GitHub",
            "resource_pic": "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png",
            "link": "www.github.com",
            "description": "This is about Github. It is widely used by all the developers in the indrustry."
        },
        {
            "name": "BitBucket",
            "resource_pic": "https://poeditor.com/blog/wp-content/uploads/2014/06/bitbucket-logo.png",
            "link": "www.bitbucket.com",
            "description": "Bitbucket is a web-based version control repository hosting service owned by Atlassian, for source code and development projects that use either Mercurial (from launch until July 1, 2020)[2] or Git (since October 2011)[3] revision control systems."
        },
        {
            "name": "Zeplin",
            "resource_pic": "https://www.lennu.net/wp-content/uploads/2015/11/zeplin_logo-523x510.png",
            "link": "www.zeplin.com",
            "description": "A Zeppelin is a type of rigid airship named after the German Count Ferdinand von Zeppelin (German pronunciation: [ˈt͡sɛpəliːn]) who pioneered rigid airship development at the beginning of the 20th century. "
        },
        {
            "name": "Aws",
            "resource_pic": "https://logodix.com/logo/5867.png",
            "link": "www.aws.com",
            "description": "Amazon Web Services (AWS) is a subsidiary of Amazon that provides on-demand cloud computing platforms and APIs to individuals, companies, and governments, on a metered pay-as-you-go basis."
        },
        {
            "name": "DropBox",
            "resource_pic": "https://upload.wikimedia.org/wikipedia/commons/b/bb/Dropbox_logo.svg",
            "link": "www.dropbox.com",
            "description": "Dropbox is a file hosting service operated by the American company Dropbox, Inc., headquartered in San Francisco, California, that offers cloud storage, file synchronization, personal cloud, and client software. "
        }
    ]

    resources_list = []
    for resource in resources:
        resources_list.append(
            Resource(name=resource['name'],
                     resource_pic=resource['resource_pic'],
                     link=resource['link'],
                     description=resource['description']
                     )
        )
    Resource.objects.bulk_create(resources_list)


@pytest.fixture()
def create_resource_items(create_resources):
    items = [
        {
            "title": "Essential Kit",
            "link": "www.item1.com",
            "description": "This is about Item 1",
            "resource_id": 1
        },
        {
            "title": "Smart Food Management",
            "link": "www.item2.com",
            "description": "This is about Item 2",
            "resource_id": 1
        },
        {
            "title": "Reporting Portal",
            "link": "www.item3.com",
            "description": "This is about Item 3",
            "resource_id": 1
        },
        {
            "title": "Resource Management",
            "link": "www.item3.com",
            "description": "This is about Item 4",
            "resource_id": 2
        },
        {
            "title": "Forms",
            "link": "www.item3.com",
            "description": "This is about Item 5",
            "resource_id": 2
        },
        {
            "title": "Covid19",
            "link": "www.item3.com",
            "description": "This is about Item 6",
            "resource_id": 2
        },
        {
            "title": "Gyaan",
            "link": "www.item3.com",
            "description": "This is about Item 7",
            "resource_id": 3
        },
        {
            "title": "Slot Booking",
            "link": "www.item3.com",
            "description": "This is about Item 8",
            "resource_id": 3
        },
        {
            "title": "Let's Ride",
            "link": "www.item3.com",
            "description": "This is about Item 9",
            "resource_id": 3
        },
        {
            "title": "Project Management",
            "link": "www.item3.com",
            "description": "This is about Item 10",
            "resource_id": 4
        },
        {
            "title": "Files Bucket",
            "link": "www.item3.com",
            "description": "This is about Item 11",
            "resource_id": 4
        },
        {
            "title": "cloud9",
            "link": "www.item3.com",
            "description": "This is about Item 12",
            "resource_id": 4
        },
        {
            "title": "Project Maintanance",
            "link": "www.item3.com",
            "description": "This is about Item 13",
            "resource_id": 5
        },
        {
            "title": "Files Management",
            "link": "www.item3.com",
            "description": "This is about Item 14",
            "resource_id": 5
        }
    ]

    items_list = []
    for item in items:
        items_list.append(
            ResourceItem(title=item['title'],
                 link=item['link'],
                 description=item['description'],
                 resource_id=item['resource_id']
                )    
        )
    ResourceItem.objects.bulk_create(items_list)


@pytest.fixture()
def resource_items_access(users, create_resource_items):
    resource_items = [
        {
            "user_id": 1,
            "resource_item_id": 1,
            "access_level": "WRITE"
        },
        {
            "user_id": 1,
            "resource_item_id": 3,
            "access_level": "READ"
        },
        {
            "user_id": 1,
            "resource_item_id": 5,
            "access_level": "READ"
        },
        {
            "user_id": 1,
            "resource_item_id": 7,
            "access_level": "WRITE"
        },
        {
            "user_id": 1,
            "resource_item_id": 9,
            "access_level": "WRITE"
        },
        {
            "user_id": 1,
            "resource_item_id": 11,
            "access_level": "READ"
        }
    ]

    access_level_list = []
    for resource in resource_items:
        access_level_list.append(
            AccessLevel(user_id=resource['user_id'],
                        resource_item_id=resource['resource_item_id'],
                        access_level=resource['access_level']
                       )
        )
    AccessLevel.objects.bulk_create(access_level_list)


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
                        ),
        ResourceItemDto(resource_name="BitBucket",
                        item_title="Forms",
                        link="www.item3.com",
                        description="This is about Item 5",
                        access_level="READ",
                        item_id=5
                        ),
        ResourceItemDto(resource_name="Zeplin",
                        item_title="Gyaan",
                        link="www.item3.com",
                        description="This is about Item 7",
                        access_level="WRITE",
                        item_id=7
                        ),
        ResourceItemDto(resource_name="Zeplin",
                        item_title="Let's Ride",
                        link="www.item3.com",
                        description="This is about Item 9",
                        access_level="WRITE",
                        item_id=9
                        ),
        ResourceItemDto(resource_name="Aws",
                        item_title="Files Bucket",
                        link="www.item3.com",
                        description="This is about Item 11",
                        access_level="READ",
                        item_id=11
                        )
    ]
    return resource_item_dtos


@pytest.fixture()
def resource_items_count_dto():
    items_count = ItemsCountDto(items_count=6)
    return items_count


@pytest.fixture()
def user_resource_items_dto(resource_items_dtos, resource_items_count_dto):
    user_resource_items_dto = UserResourceItemsDto(
        items_count_dto=resource_items_count_dto,
        resource_items=resource_items_dtos
    )
    return user_resource_items_dto


@pytest.fixture()
def resource_items_dtos_searchby_resource_name():
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
def user_resource_items_dto_searchby_resource(
        resource_items_dtos_searchby_resource_name):
    user_resource_items_dto = UserResourceItemsDto(
        items_count_dto=ItemsCountDto(items_count=2),
        resource_items=resource_items_dtos_searchby_resource_name
    )
    return user_resource_items_dto

@pytest.fixture()
def resource_items_dtos_searchby_item_title():
    resource_item_dtos = [
        ResourceItemDto(resource_name="BitBucket",
                        item_title="Forms",
                        link="www.item3.com",
                        description="This is about Item 5",
                        access_level="READ",
                        item_id=5
                        )
    ]
    return resource_item_dtos

@pytest.fixture()
def user_resource_items_dto_searchby_item_title(
        resource_items_dtos_searchby_item_title):
    user_resource_items_dto = UserResourceItemsDto(
        items_count_dto=ItemsCountDto(items_count=1),
        resource_items=resource_items_dtos_searchby_item_title
    )
    return user_resource_items_dto


@pytest.fixture()
def resource_items_dtos_searchby_access_level():
    resource_item_dtos = [
        ResourceItemDto(resource_name="GitHub",
                        item_title="Essential Kit",
                        link="www.item1.com",
                        description="This is about Item 1",
                        access_level="WRITE",
                        item_id=1
                        ),
        ResourceItemDto(resource_name="Zeplin",
                        item_title="Gyaan",
                        link="www.item3.com",
                        description="This is about Item 7",
                        access_level="WRITE",
                        item_id=7
                        ),
        ResourceItemDto(resource_name="Zeplin",
                        item_title="Let's Ride",
                        link="www.item3.com",
                        description="This is about Item 9",
                        access_level="WRITE",
                        item_id=9
                        )
    ]
    return resource_item_dtos

@pytest.fixture()
def user_resource_items_dto_searchby_access_level(
        resource_items_dtos_searchby_access_level):
    user_resource_items_dto = UserResourceItemsDto(
        items_count_dto=ItemsCountDto(items_count=3),
        resource_items=resource_items_dtos_searchby_access_level
    )
    return user_resource_items_dto


@pytest.fixture()
def resource_items_dtos_searchby_common():
    resource_item_dtos = [
        ResourceItemDto(resource_name="BitBucket",
                        item_title="Forms",
                        link="www.item3.com",
                        description="This is about Item 5",
                        access_level="READ",
                        item_id=5
                        ),
        ResourceItemDto(resource_name="Aws",
                        item_title="Files Bucket",
                        link="www.item3.com",
                        description="This is about Item 11",
                        access_level="READ",
                        item_id=11
                        )
    ]
    return resource_item_dtos

@pytest.fixture()
def user_resource_items_dto_searchby_common(
        resource_items_dtos_searchby_common):
    user_resource_items_dto = UserResourceItemsDto(
        items_count_dto=ItemsCountDto(items_count=2),
        resource_items=resource_items_dtos_searchby_common
    )
    return user_resource_items_dto


@pytest.fixture()
def user_resource_items_dto_searchby_unknown(
        resource_items_dtos_searchby_common):
    user_resource_items_dto = UserResourceItemsDto(
        items_count_dto=ItemsCountDto(items_count=0),
        resource_items=[]
    )
    return user_resource_items_dto
 

@pytest.fixture()
def user_requests(users, create_resource_items):
    requests = [
        {
            'user_id': 1,
            'resource_id': 1,
            'resource_item_id': 2,
            'access_level': 'READ',
            'due_datetime': '2020-06-01 19:00:00',
            'reason_for_access': 'I want data to do something',
        },
        {
            'user_id': 1,
            'resource_id': 2,
            'resource_item_id': 4,
            'access_level': 'WRITE',
            'due_datetime': '2020-06-01 09:00:00',
            'reason_for_access': 'I want data to do something',
        },
        {
            'user_id': 1,
            'resource_id': 2,
            'resource_item_id': 6,
            'access_level': 'READ',
            'due_datetime': '2020-06-10 13:00:00',
            'reason_for_access': 'I want data to do something',
        },
        {
            'user_id': 1,
            'resource_id': 3,
            'resource_item_id': 8,
            'access_level': 'WRITE',
            'due_datetime': '2020-06-10 02:00:00',
            'reason_for_access': 'I want data to do something',
        },
        {
            'user_id': 1,
            'resource_id': 4,
            'resource_item_id': 10,
            'access_level': 'WRITE',
            'due_datetime': '2020-06-10 11:00:00',
            'reason_for_access': 'I want data to do something',
        },
    ]
    
    requests_list = []
    for request in requests:
        requests_list.append(
            Request(user_id=request['user_id'],
                    resource_id=request['resource_id'],
                    resource_item_id=request['resource_item_id'],
                    access_level=request['access_level'],
                    due_datetime=request['due_datetime'],
                    reason_for_access=request['reason_for_access']
                   )
        )
    Request.objects.bulk_create(requests_list)


@pytest.fixture()
def accept_requests(user_requests):
    resource_items = [
        {
            "user_id": 1,
            "resource_item_id": 4,
            "access_level": "WRITE"
        },
        {
            "user_id": 2,
            "resource_item_id": 6,
            "access_level": "READ"
        },
        {
            "user_id": 3,
            "resource_item_id": 10,
            "access_level": "WRITE"
        }
    ]

    access_level_list = []
    for resource in resource_items:
        access_level_list.append(
            AccessLevel(user_id=resource['user_id'],
                        resource_item_id=resource['resource_item_id'],
                        access_level=resource['access_level']
                       )
        )
    AccessLevel.objects.bulk_create(access_level_list)
    Request.objects.filter(id__in=[2, 3, 5])\
            .update(request_status="ACCEPTED")


@pytest.fixture()
def reject_requests(user_requests):
    Request.objects.filter(id=1)\
        .update(
            request_status="REJECTED",
            reason_for_rejection="Its Not useful"
        )


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
                         item_title="Resource Management",
                         access_level="WRITE",
                         request_id=2,
                         status="ACCEPTED"
                        ),
        RequestStatusDto(resource_name="BitBucket",
                         item_title="Covid19",
                         access_level="READ",
                         request_id=3,
                         status="ACCEPTED"
                        ),
        RequestStatusDto(resource_name="Zeplin",
                         item_title="Slot Booking",
                         access_level="WRITE",
                         request_id=4,
                         status="PENDING"
                        ),
        RequestStatusDto(resource_name="Aws",
                         item_title="Project Management",
                         access_level="WRITE",
                         request_id=5,
                         status="ACCEPTED"
                        )
    ]
    return request_dtos


@pytest.fixture()
def get_requests_filterby_request_status():
    get_requests_parameters_dto = GetRequestsParametersDto(
                                                            offset=0,
                                                            limit=5,
                                                            sortby="",
                                                            filterby="STATUS",
                                                            filterby_value="ACCEPTED"
                                                           )
    return get_requests_parameters_dto


@pytest.fixture()
def user_requests_status_dtos_filterby_status():
    request_dtos = [
        RequestStatusDto(resource_name="BitBucket",
                         item_title="Resource Management",
                         access_level="WRITE",
                         request_id=2,
                         status="ACCEPTED"
                        ),
        RequestStatusDto(resource_name="BitBucket",
                         item_title="Covid19",
                         access_level="READ",
                         request_id=3,
                         status="ACCEPTED"
                        ),
        RequestStatusDto(resource_name="Aws",
                         item_title="Project Management",
                         access_level="WRITE",
                         request_id=5,
                         status="ACCEPTED"
                        )
    ]
    return request_dtos


@pytest.fixture()
def get_requests_filterby_access_level():
    get_requests_parameters_dto = GetRequestsParametersDto(
                                                            offset=0,
                                                            limit=5,
                                                            sortby="",
                                                            filterby="ACCESSLEVEL",
                                                            filterby_value="READ"
                                                           )
    return get_requests_parameters_dto


@pytest.fixture()
def user_requests_status_dtos_filterby_accesslevel():
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
                        )
    ]
    return request_dtos


@pytest.fixture()
def get_requests_filterby_resource():
    get_requests_parameters_dto = GetRequestsParametersDto(
                                                            offset=0,
                                                            limit=5,
                                                            sortby="",
                                                            filterby="RESOURCE",
                                                            filterby_value="BitBucket"
                                                           )
    return get_requests_parameters_dto


@pytest.fixture()
def user_requests_status_dtos_filterby_resource():
    request_dtos = [
        RequestStatusDto(resource_name="BitBucket",
                         item_title="Resource Management",
                         access_level="WRITE",
                         request_id=2,
                         status="ACCEPTED"
                        ),
        RequestStatusDto(resource_name="BitBucket",
                         item_title="Covid19",
                         access_level="READ",
                         request_id=3,
                         status="ACCEPTED"
                        )
    ]
    return request_dtos


@pytest.fixture()
def get_requests_sortby_request_status():
    get_requests_parameters_dto = GetRequestsParametersDto(
                                                            offset=0,
                                                            limit=5,
                                                            sortby="STATUS",
                                                            filterby="",
                                                            filterby_value=""
                                                           )
    return get_requests_parameters_dto


@pytest.fixture()
def user_requests_status_dtos_sortby_status():
    request_dtos = [
        RequestStatusDto(resource_name="BitBucket",
                         item_title="Resource Management",
                         access_level="WRITE",
                         request_id=2,
                         status="ACCEPTED"
                        ),
        RequestStatusDto(resource_name="BitBucket",
                         item_title="Covid19",
                         access_level="READ",
                         request_id=3,
                         status="ACCEPTED"
                        ),
        RequestStatusDto(resource_name="Aws",
                         item_title="Project Management",
                         access_level="WRITE",
                         request_id=5,
                         status="ACCEPTED"
                        ),
        RequestStatusDto(resource_name="Zeplin",
                         item_title="Slot Booking",
                         access_level="WRITE",
                         request_id=4,
                         status="PENDING"
                        ),
        RequestStatusDto(resource_name="GitHub",
                         item_title="Smart Food Management",
                         access_level="READ",
                         request_id=1,
                         status="REJECTED"
                        )
    ]
    return request_dtos


@pytest.fixture()
def get_requests_sortby_resource():
    get_requests_parameters_dto = GetRequestsParametersDto(
                                                            offset=0,
                                                            limit=5,
                                                            sortby="RESOURCE",
                                                            filterby="",
                                                            filterby_value=""
                                                           )
    return get_requests_parameters_dto


@pytest.fixture()
def user_requests_status_dtos_sortby_resource():
    request_dtos = [
        RequestStatusDto(resource_name="Aws",
                         item_title="Project Management",
                         access_level="WRITE",
                         request_id=5,
                         status="ACCEPTED"
                        ),
        RequestStatusDto(resource_name="BitBucket",
                         item_title="Resource Management",
                         access_level="WRITE",
                         request_id=2,
                         status="ACCEPTED"
                        ),
        RequestStatusDto(resource_name="BitBucket",
                         item_title="Covid19",
                         access_level="READ",
                         request_id=3,
                         status="ACCEPTED"
                        ),
        RequestStatusDto(resource_name="GitHub",
                         item_title="Smart Food Management",
                         access_level="READ",
                         request_id=1,
                         status="REJECTED"
                        ),
        RequestStatusDto(resource_name="Zeplin",
                         item_title="Slot Booking",
                         access_level="WRITE",
                         request_id=4,
                         status="PENDING"
                        )
    ]
    return request_dtos


@pytest.fixture()
def get_requests_sortby_accesslevel():
    get_requests_parameters_dto = GetRequestsParametersDto(
                                                            offset=0,
                                                            limit=5,
                                                            sortby="ACCESSLEVEL",
                                                            filterby="",
                                                            filterby_value=""
                                                           )
    return get_requests_parameters_dto


@pytest.fixture()
def user_requests_status_dtos_sortby_accesslevel():
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
        RequestStatusDto(resource_name="BitBucket",
                         item_title="Resource Management",
                         access_level="WRITE",
                         request_id=2,
                         status="ACCEPTED"
                        ),
        RequestStatusDto(resource_name="Zeplin",
                         item_title="Slot Booking",
                         access_level="WRITE",
                         request_id=4,
                         status="PENDING"
                        ),
        RequestStatusDto(resource_name="Aws",
                         item_title="Project Management",
                         access_level="WRITE",
                         request_id=5,
                         status="ACCEPTED"
                        )
    ]
    return request_dtos


@pytest.fixture()
def search_resources_by_individual_name():
    return [ResourceMinimalDetailsDto(resource_id=4, name='Aws')]


@pytest.fixture()
def search_resources_by_common_name():
    return [
                ResourceMinimalDetailsDto(resource_id=1, name='GitHub'),
                ResourceMinimalDetailsDto(resource_id=2, name='BitBucket')
            ]

@pytest.fixture()
def search_resources_by_unknown_name():
    return []


@pytest.fixture()
def serach_resource_items_by_individual_name():
    resource_items = [
        ItemMinimalDetailsDto(item_id=12, title='cloud9')
    ]
    return resource_items


@pytest.fixture()
def search_resouce_items_by_common_name():
    return [
                ItemMinimalDetailsDto(item_id=10, title='Project Management'),
                ItemMinimalDetailsDto(item_id=12, title='cloud9')
            ]

@pytest.fixture()
def search_resouce_items_by_unknown_name():
    return []


@pytest.fixture()
def request_dto():
    request_dto = RequestDto(resource_id=1,
                             item_id=2,
                             access_level="READ",
                             due_datetime=datetime.datetime(2020, 6, 1, 10, 0),
                             reason_for_access="Wanted to do work"
                            )
    return request_dto


@pytest.fixture()
def requestsssss():
    requests = [
        {
            'user_id': 1,
            'resource_id': 1,
            'resource_item_id': 2,
            'access_level': 'READ',
            'due_datetime': '2020-06-01 19:00:00',
            'reason_for_access': 'I want data to do something',
        },
        {
            'user_id': 1,
            'resource_id': 2,
            'resource_item_id': 4,
            'access_level': 'WRITE',
            'due_datetime': '2020-06-01 09:00:00',
            'reason_for_access': 'I want data to do something',
        },
        {
            'user_id': 1,
            'resource_id': 2,
            'resource_item_id': 6,
            'access_level': 'READ',
            'due_datetime': '2020-06-10 13:00:00',
            'reason_for_access': 'I want data to do something',
        },
        {
            'user_id': 1,
            'resource_id': 3,
            'resource_item_id': 8,
            'access_level': 'WRITE',
            'due_datetime': '2020-06-10 02:00:00',
            'reason_for_access': 'I want data to do something',
        },
        {
            'user_id': 1,
            'resource_id': 4,
            'resource_item_id': 10,
            'access_level': 'WRITE',
            'due_datetime': '2020-06-10 11:00:00',
            'reason_for_access': 'I want data to do something',
        },
        {
            'user_id': 2,
            'resource_id': 1,
            'resource_item_id': 2,
            'access_level': 'READ',
            'due_datetime': '2020-06-01 19:00:00',
            'reason_for_access': 'I want data to do something',
        },
        {
            'user_id': 2,
            'resource_id': 2,
            'resource_item_id': 4,
            'access_level': 'WRITE',
            'due_datetime': '2020-06-01 09:00:00',
            'reason_for_access': 'I want data to do something',
        },
        {
            'user_id': 2,
            'resource_id': 2,
            'resource_item_id': 6,
            'access_level': 'READ',
            'due_datetime': '2020-06-10 13:00:00',
            'reason_for_access': 'I want data to do something',
        },
        {
            'user_id': 2,
            'resource_id': 3,
            'resource_item_id': 8,
            'access_level': 'WRITE',
            'due_datetime': '2020-06-10 02:00:00',
            'reason_for_access': 'I want data to do something',
        },
        {
            'user_id': 2,
            'resource_id': 4,
            'resource_item_id': 10,
            'access_level': 'WRITE',
            'due_datetime': '2020-06-10 11:00:00',
            'reason_for_access': 'I want data to do something',
        },
        {
            'user_id': 3,
            'resource_id': 1,
            'resource_item_id': 2,
            'access_level': 'READ',
            'due_datetime': '2020-06-01 19:00:00',
            'reason_for_access': 'I want data to do something',
        },
        {
            'user_id': 3,
            'resource_id': 2,
            'resource_item_id': 4,
            'access_level': 'WRITE',
            'due_datetime': '2020-06-01 09:00:00',
            'reason_for_access': 'I want data to do something',
        },
        {
            'user_id': 3,
            'resource_id': 2,
            'resource_item_id': 6,
            'access_level': 'READ',
            'due_datetime': '2020-06-10 13:00:00',
            'reason_for_access': 'I want data to do something',
        },
        {
            'user_id': 3,
            'resource_id': 3,
            'resource_item_id': 8,
            'access_level': 'WRITE',
            'due_datetime': '2020-06-10 02:00:00',
            'reason_for_access': 'I want data to do something',
        },
        {
            'user_id': 3,
            'resource_id': 4,
            'resource_item_id': 10,
            'access_level': 'WRITE',
            'due_datetime': '2020-06-10 11:00:00',
            'reason_for_access': 'I want data to do something',
        },
        {
            'user_id': 4,
            'resource_id': 1,
            'resource_item_id': 2,
            'access_level': 'READ',
            'due_datetime': '2020-06-01 19:00:00',
            'reason_for_access': 'I want data to do something',
        },
        {
            'user_id': 4,
            'resource_id': 2,
            'resource_item_id': 4,
            'access_level': 'WRITE',
            'due_datetime': '2020-06-01 09:00:00',
            'reason_for_access': 'I want data to do something',
        },
        {
            'user_id': 4,
            'resource_id': 2,
            'resource_item_id': 6,
            'access_level': 'READ',
            'due_datetime': '2020-06-10 13:00:00',
            'reason_for_access': 'I want data to do something',
        },
        {
            'user_id': 4,
            'resource_id': 3,
            'resource_item_id': 8,
            'access_level': 'WRITE',
            'due_datetime': '2020-06-10 02:00:00',
            'reason_for_access': 'I want data to do something',
        },
        {
            'user_id': 4,
            'resource_id': 4,
            'resource_item_id': 10,
            'access_level': 'WRITE',
            'due_datetime': '2020-06-10 11:00:00',
            'reason_for_access': 'I want data to do something',
        },
        {
            'user_id': 1,
            'resource_id': 1,
            'resource_item_id': 3,
            'access_level': 'READ',
            'due_datetime': '2020-06-01 19:00:00',
            'reason_for_access': 'I want data to do something',
        },
        {
            'user_id': 1,
            'resource_id': 2,
            'resource_item_id': 5,
            'access_level': 'WRITE',
            'due_datetime': '2020-06-01 09:00:00',
            'reason_for_access': 'I want data to do something',
        },
        {
            'user_id': 1,
            'resource_id': 5,
            'resource_item_id': 13,
            'access_level': 'READ',
            'due_datetime': '2020-06-10 13:00:00',
            'reason_for_access': 'I want data to do something',
        },
        {
            'user_id': 1,
            'resource_id': 3,
            'resource_item_id': 9,
            'access_level': 'WRITE',
            'due_datetime': '2020-06-10 02:00:00',
            'reason_for_access': 'I want data to do something',
        },
        {
            'user_id': 1,
            'resource_id': 4,
            'resource_item_id': 11,
            'access_level': 'WRITE',
            'due_datetime': '2020-06-10 11:00:00',
            'reason_for_access': 'I want data to do something',
        },
        {
            'user_id': 2,
            'resource_id': 1,
            'resource_item_id': 3,
            'access_level': 'READ',
            'due_datetime': '2020-06-01 19:00:00',
            'reason_for_access': 'I want data to do something',
        },
        {
            'user_id': 2,
            'resource_id': 2,
            'resource_item_id': 5,
            'access_level': 'WRITE',
            'due_datetime': '2020-06-01 09:00:00',
            'reason_for_access': 'I want data to do something',
        },
        {
            'user_id': 2,
            'resource_id': 5,
            'resource_item_id': 13,
            'access_level': 'READ',
            'due_datetime': '2020-06-10 13:00:00',
            'reason_for_access': 'I want data to do something',
        },
        {
            'user_id': 2,
            'resource_id': 3,
            'resource_item_id': 9,
            'access_level': 'WRITE',
            'due_datetime': '2020-06-10 02:00:00',
            'reason_for_access': 'I want data to do something',
        },
        {
            'user_id': 2,
            'resource_id': 4,
            'resource_item_id': 11,
            'access_level': 'WRITE',
            'due_datetime': '2020-06-10 11:00:00',
            'reason_for_access': 'I want data to do something',
        },
        {
            'user_id': 3,
            'resource_id': 1,
            'resource_item_id': 3,
            'access_level': 'READ',
            'due_datetime': '2020-06-01 19:00:00',
            'reason_for_access': 'I want data to do something',
        },
        {
            'user_id': 3,
            'resource_id': 2,
            'resource_item_id': 5,
            'access_level': 'WRITE',
            'due_datetime': '2020-06-01 09:00:00',
            'reason_for_access': 'I want data to do something',
        },
        {
            'user_id': 3,
            'resource_id': 5,
            'resource_item_id': 13,
            'access_level': 'READ',
            'due_datetime': '2020-06-10 13:00:00',
            'reason_for_access': 'I want data to do something',
        },
        {
            'user_id': 3,
            'resource_id': 3,
            'resource_item_id': 9,
            'access_level': 'WRITE',
            'due_datetime': '2020-06-10 02:00:00',
            'reason_for_access': 'I want data to do something',
        },
        {
            'user_id': 3,
            'resource_id': 4,
            'resource_item_id': 11,
            'access_level': 'WRITE',
            'due_datetime': '2020-06-10 11:00:00',
            'reason_for_access': 'I want data to do something',
        },
        {
            'user_id': 4,
            'resource_id': 1,
            'resource_item_id': 3,
            'access_level': 'READ',
            'due_datetime': '2020-06-01 19:00:00',
            'reason_for_access': 'I want data to do something',
        },
        {
            'user_id': 4,
            'resource_id': 2,
            'resource_item_id': 5,
            'access_level': 'WRITE',
            'due_datetime': '2020-06-01 09:00:00',
            'reason_for_access': 'I want data to do something',
        },
        {
            'user_id': 4,
            'resource_id': 5,
            'resource_item_id': 13,
            'access_level': 'READ',
            'due_datetime': '2020-06-10 13:00:00',
            'reason_for_access': 'I want data to do something',
        },
        {
            'user_id': 4,
            'resource_id': 3,
            'resource_item_id': 9,
            'access_level': 'WRITE',
            'due_datetime': '2020-06-10 02:00:00',
            'reason_for_access': 'I want data to do something',
        },
        {
            'user_id': 4,
            'resource_id': 4,
            'resource_item_id': 11,
            'access_level': 'WRITE',
            'due_datetime': '2020-06-10 11:00:00',
            'reason_for_access': 'I want data to do something',
        }
    ]
    
    requests_list = []
    for request in requests:
        requests_list.append(
            Request(user_id=request['user_id'],
                    resource_id=request['resource_id'],
                    resource_item_id=request['resource_item_id'],
                    access_level=request['access_level'],
                    due_datetime=request['due_datetime'],
                    reason_for_access=request['reason_for_access']
                   )
        )
    Request.objects.bulk_create(requests_list)
