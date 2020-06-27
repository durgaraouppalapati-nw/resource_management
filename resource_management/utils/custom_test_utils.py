from datetime import datetime
from freezegun import freeze_time
from django_swagger_utils.utils.test import CustomAPITestCase

from resource_management.utils.fixture import (
    UserFactory, ResourceFactory, ResourceItemFactory,
    RequestFactory, ResourceItemAccessFactory
)
from resource_management.models import ResourceItem, User


class CustomTestUtils(CustomAPITestCase):

    def set_up_user(self, username, password):
        super(CustomTestUtils, self).setupUser(
            username=username, password=password
        )
        UserFactory.reset_sequence()
        ResourceFactory.reset_sequence()
        ResourceItemFactory.reset_sequence()
        RequestFactory.reset_sequence()
        ResourceItemAccessFactory.reset_sequence()

    def set_foo_user_as_admin(self, user):
        user.is_admin = True
        user.save()

    def create_users(self, size):
        users = UserFactory.create_batch(size=size)
        return users

    def create_resources(self, size):
        resources = ResourceFactory.create_batch(size=size)
        return resources

    def create_resource_items(self, size):
        resource = self.create_resources(1)
        resource_items = ResourceItemFactory.create_batch(size=size, resource=resource[0])
        return resource_items

    def create_resource_item_access(self):
        users = self.create_users(size=5)
        resource_items = self.create_resource_items(size=3)
        ResourceItemAccessFactory.create(resource_item=resource_items[0],
                                         user=users[1]
                                         )
        ResourceItemAccessFactory.create(resource_item=resource_items[0],
                                         user=users[2]
                                         )
        ResourceItemAccessFactory.create(resource_item=resource_items[0],
                                         user=users[3]
                                         )

    def create_requests(self, size):
        self.create_users(size=3)
        self.create_resource_items(size=3)
        requests = RequestFactory.create_batch(size=size)
        return requests

    def create_resource_items_for_user(self):
        self.create_users(size=2)
        self.create_resource_items(size=3)
        ResourceItemAccessFactory.create_batch(3, user=User.objects.get(id=2))

    def create_resource_items_for_default_user(self):
        self.create_resource_items(size=3)
        ResourceItemAccessFactory.create_batch(3)

    def user_requests(self):
        self.create_resource_items(size=3)
        requests = RequestFactory.create_batch(size=3)
        requests[1].request_status = 'ACCEPTED'
        requests[2].request_status = 'REJECTED'
        requests[2].reason_for_rejection = "At this time u don't need it"
        requests[1].save()
        requests[2].save()
