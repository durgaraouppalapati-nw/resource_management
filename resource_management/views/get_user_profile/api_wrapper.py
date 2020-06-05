import json

from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']

    data = {
        "username": user.name,
        "is_admin": user.is_superuser
    }
    response = json.dumps(data)
    return HttpResponse(response, status=200)
