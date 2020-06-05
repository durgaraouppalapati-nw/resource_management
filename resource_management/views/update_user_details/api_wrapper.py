from django.http import HttpResponse

from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from resource_management.storages.user_implementation import \
    UserImplementation
from resource_management.interactors.update_profile_interactor import \
    UpdateProfileInteractor
from resource_management.interactors.storages.dtos import UserDetailsDto


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    request_data = kwargs['request_data']
    name = request_data['name']
    profile_pic = request_data['profile_pic']
    job_role = request_data['job_role']
    department = request_data['department']
    gender = request_data['gender']
    user = kwargs['user']
    user_id = user.id
    
    user_storage = UserImplementation()
    interactor = UpdateProfileInteractor(
        user_storage=user_storage    
    )
    user_details_dto = UserDetailsDto(name=name,
                                      profile_pic=profile_pic,
                                      job_role=job_role,
                                      department=department,
                                      gender=gender
                                     )

    interactor.update_profile(
        user_id=user_id, user_details_dto=user_details_dto
    )
    return HttpResponse(status=200)
