import factory, factory.django, factory.fuzzy
from datetime import datetime, timedelta

from resource_management.models import (
    User, Resource, ResourceItem, Request, AccessLevel
)


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User

    username = factory.Sequence(lambda n: 'user%d' % n)
    name = factory.Sequence(lambda n: 'User %d' % n)
    job_role = 'Developer'
    department = 'Backend'
    gender = factory.fuzzy.FuzzyChoice(User.Gender_Choice, getter=lambda c: c[0])
    is_admin = False


class ResourceFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Resource

    name = factory.Sequence(lambda n: 'Resource %d' % n)
    resource_pic = factory.Sequence(lambda n: 'www.resource%d.pnj' % n)
    link = factory.Sequence(lambda n: 'www.resource%d.com' % n)
    description = factory.Sequence(lambda n: 'This is about Resource %d' % n)


class ResourceItemFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = ResourceItem

    resource = factory.Iterator(Resource.objects.all())
    title = factory.Sequence(lambda n: "ResourceItem %d" % n)
    link = factory.Sequence(lambda n: 'www.resource_item%d.com' % n)
    description = factory.Sequence(lambda n: 'This is about ResourceItem %d' % n)


class ResourceItemAccessFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = AccessLevel

    user = factory.Iterator(User.objects.filter(is_admin=False))
    resource_item = factory.Iterator(ResourceItem.objects.all())
    access_level = "READ"


def due_date_time():
    date_time = datetime.now() + timedelta(days=2)
    return date_time


class RequestFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Request

    user = factory.Iterator(User.objects.filter(is_admin=False))
    resource = factory.Iterator(Resource.objects.all())
    resource_item = factory.Iterator(ResourceItem.objects.all())
    access_level = 'READ'
    due_datetime = factory.LazyFunction(due_date_time)
    reason_for_access = "Wanted to do the project"
    request_status = "PENDING"
    reason_for_rejection = ""
