import pytest

from resource_management.storages.request_storage_implementation import \
    RequestStorageImplementation
from resource_management.interactors.storages.dtos import RequestsCountDto


@pytest.mark.django_db
def test_get_user_requests_with_requests_return_requests_count_and_request_details_dto(
        accept_requests,
        reject_requests,
        user_requests_status_dtos,
        get_requests_parameters_dto):
    # Arrange
    user_id = 1
    request_storage = RequestStorageImplementation()
    requests_count_dto = RequestsCountDto(requests_count=5)
    expected_output = requests_count_dto, user_requests_status_dtos

    # Act
    actual_output = request_storage.get_user_requests(
        user_id=user_id,
        requests_parameters_dto=get_requests_parameters_dto
    )

    # Assert
    assert expected_output[0] == actual_output[0]
    assert expected_output[1] == actual_output[1]


@pytest.mark.django_db
def test_get_user_requests_with_filterby_status_return_requests_count_and_request_details_dto(
        accept_requests,
        reject_requests,
        user_requests_status_dtos_filterby_status,
        get_requests_filterby_request_status):
    # Arrange
    user_id = 1
    request_storage = RequestStorageImplementation()
    requests_count_dto = RequestsCountDto(requests_count=3)
    expected_output = requests_count_dto, user_requests_status_dtos_filterby_status

    # Act
    actual_output = request_storage.get_user_requests(
        user_id=user_id,
        requests_parameters_dto=get_requests_filterby_request_status
    )

    # Assert
    assert expected_output[0] == actual_output[0]
    assert expected_output[1] == actual_output[1]


@pytest.mark.django_db
def test_get_user_requests_with_filterby_resource_return_requests_count_and_request_details_dto(
        accept_requests,
        reject_requests,
        user_requests_status_dtos_filterby_resource,
        get_requests_filterby_resource):
    # Arrange
    user_id = 1
    request_storage = RequestStorageImplementation()
    requests_count_dto = RequestsCountDto(requests_count=2)
    expected_output = requests_count_dto, user_requests_status_dtos_filterby_resource

    # Act
    actual_output = request_storage.get_user_requests(
        user_id=user_id,
        requests_parameters_dto=get_requests_filterby_resource
    )

    # Assert
    assert expected_output[0] == actual_output[0]
    assert expected_output[1] == actual_output[1]


@pytest.mark.django_db
def test_get_user_requests_with_filterby_accesslevel_return_requests_count_and_request_details_dto(
        accept_requests,
        reject_requests,
        user_requests_status_dtos_filterby_accesslevel,
        get_requests_filterby_access_level):
    # Arrange
    user_id = 1
    request_storage = RequestStorageImplementation()
    requests_count_dto = RequestsCountDto(requests_count=2)
    expected_output = requests_count_dto, user_requests_status_dtos_filterby_accesslevel

    # Act
    actual_output = request_storage.get_user_requests(
        user_id=user_id,
        requests_parameters_dto=get_requests_filterby_access_level
    )

    # Assert
    assert expected_output[0] == actual_output[0]
    assert expected_output[1] == actual_output[1]



@pytest.mark.django_db
def test_get_user_requests_with_sortby_resource_return_requests_count_and_request_details_dto(
        accept_requests,
        reject_requests,
        user_requests_status_dtos_sortby_resource,
        get_requests_sortby_resource):
    # Arrange
    user_id = 1
    request_storage = RequestStorageImplementation()
    requests_count_dto = RequestsCountDto(requests_count=5)
    expected_output = requests_count_dto, user_requests_status_dtos_sortby_resource

    # Act
    actual_output = request_storage.get_user_requests(
        user_id=user_id,
        requests_parameters_dto=get_requests_sortby_resource
    )

    # Assert
    assert expected_output[0] == actual_output[0]
    assert expected_output[1] == actual_output[1]


@pytest.mark.django_db
def test_get_user_requests_with_sortby_accesslevel_return_requests_count_and_request_details_dto(
        accept_requests,
        reject_requests,
        user_requests_status_dtos_sortby_accesslevel,
        get_requests_sortby_accesslevel):
    # Arrange
    user_id = 1
    request_storage = RequestStorageImplementation()
    requests_count_dto = RequestsCountDto(requests_count=5)
    expected_output = requests_count_dto, user_requests_status_dtos_sortby_accesslevel

    # Act
    actual_output = request_storage.get_user_requests(
        user_id=user_id,
        requests_parameters_dto=get_requests_sortby_accesslevel
    )

    # Assert
    assert expected_output[0] == actual_output[0]
    assert expected_output[1] == actual_output[1]


@pytest.mark.django_db
def test_get_user_requests_with_sortby_status_return_requests_count_and_request_details_dto(
        accept_requests,
        reject_requests,
        user_requests_status_dtos_sortby_status,
        get_requests_sortby_request_status):
    # Arrange
    user_id = 1
    request_storage = RequestStorageImplementation()
    requests_count_dto = RequestsCountDto(requests_count=5)
    expected_output = requests_count_dto, user_requests_status_dtos_sortby_status

    # Act
    actual_output = request_storage.get_user_requests(
        user_id=user_id,
        requests_parameters_dto=get_requests_sortby_request_status
    )

    # Assert
    assert expected_output[0] == actual_output[0]
    assert expected_output[1] == actual_output[1]
