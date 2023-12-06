import json

from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from resource_management.interactors.accept_or_reject_requests_interactor \
    import AcceptOrRejectRequestsInteractor
from resource_management.storages.request_storage_implementation import \
    RequestStorageImplementation
from resource_management.storages.user_implementation import \
    UserImplementation
from resource_management.presenters.presenter_implementation import \
    PresenterImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    
    request_data = kwargs['request_data']
    action = request_data['action']
    request_ids = request_data['request_ids']
    reason_for_rejection = request_data['reason_for_rejection']
    user = kwargs['user']
    user_id = user.id

    request_storage = RequestStorageImplementation()
    user_storage = UserImplementation()
    presenter = PresenterImplementation()
    interactor = AcceptOrRejectRequestsInteractor(
        request_storage=request_storage,
        user_storage=user_storage,
        presenter=presenter
    )

    response = interactor.accept_or_reject_requests(
        action=action, request_ids=request_ids,
        reason_for_rejection=reason_for_rejection,
        user_id=user_id
    )

    return response
