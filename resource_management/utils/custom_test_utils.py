from django_swagger_utils.utils.test import CustomAPITestCase

from resource_management.utils.fixture import (
    UserFactory, ResourceFactory, ResourceItemFactory,
    RequestFactory, ResourceItemAccessFactory
)


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
        self.create_users(size=3)
        self.create_resource_items(size=5)
        ResourceItemAccessFactory.create_batch(5)

    def create_requests(self, size):
        self.create_users(size=3)
        self.create_resource_items(size=3)
        RequestFactory.create_batch(3)
