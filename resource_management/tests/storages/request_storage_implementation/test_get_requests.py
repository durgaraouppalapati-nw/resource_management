import pytest

from resource_management.storages.request_storage_implementation import \
    RequestStorageImplementation


@pytest.mark.django_db
def test_get_requests_with_requests_return_requests_count_and_request_details_dto(
        requests,
        requests_count_dto,
        user_request_dtos,
        get_requests_parameters_dto):
    # Arrange
    request_storage = RequestStorageImplementation()
    expected_output = requests_count_dto, user_request_dtos

    # Act
    actual_output = request_storage.get_requests(get_requests_parameters_dto)

    # Assert
    assert expected_output[0] == actual_output[0]
    assert expected_output[1] == actual_output[1]


@pytest.mark.django_db
def test_get_requests_with_filterby_name_return_requests_count_and_request_details_dto(
        requests,
        requests_count_filterby_name_dto,
        user_filterby_name_request_dtos,
        get_requests_filterby_name_dto):
    # Arrange
    request_storage = RequestStorageImplementation()
    expected_output = requests_count_filterby_name_dto, user_filterby_name_request_dtos

    # Act
    actual_output = request_storage.get_requests(
        get_requests_filterby_name_dto
    )

    # Assert
    assert expected_output[0] == actual_output[0]
    assert expected_output[1] == actual_output[1]


@pytest.mark.django_db
def test_get_requests_with_filterby_resource_return_requests_count_and_request_details_dto(
        requests,
        requests_count_dto,
        user_request_dtos,
        get_requests_filterby_resource_name_dto):
    # Arrange
    request_storage = RequestStorageImplementation()
    expected_output = requests_count_dto, user_request_dtos

    # Act
    actual_output = request_storage.get_requests(
        get_requests_filterby_resource_name_dto
    )

    # Assert
    assert expected_output[0] == actual_output[0]
    assert expected_output[1] == actual_output[1]


@pytest.mark.django_db
def test_get_requests_with_filterby_accesslevel_return_requests_count_and_request_details_dto(
        requests,
        requests_count_dto,
        user_request_dtos,
        get_requests_filterby_access_level_dto):
    # Arrange
    request_storage = RequestStorageImplementation()
    expected_output = requests_count_dto, user_request_dtos

    # Act
    actual_output = request_storage.get_requests(
        get_requests_filterby_access_level_dto
    )

    # Assert
    assert expected_output[0] == actual_output[0]
    assert expected_output[1] == actual_output[1]



@pytest.mark.django_db
def test_get_requests_with_sortby_resource_return_requests_count_and_request_details_dto(
        create_requests,
        requests_count_dto,
        users_requests_dtos,
        get_requests_sortby_resource_dto):
    # Arrange
    request_storage = RequestStorageImplementation()
    expected_output = requests_count_dto, users_requests_dtos

    # Act
    actual_output = request_storage.get_requests(
        get_requests_sortby_resource_dto
    )

    # Assert
    assert expected_output[0] == actual_output[0]
    assert expected_output[1] == actual_output[1]


@pytest.mark.django_db
def test_get_requests_with_sortby_item_return_requests_count_and_request_details_dto(
        create_requests,
        requests_count_dto,
        users_requests_dtos,
        get_requests_sortby_item_dto):
    # Arrange
    request_storage = RequestStorageImplementation()
    expected_output = requests_count_dto, users_requests_dtos

    # Act
    actual_output = request_storage.get_requests(
        get_requests_sortby_item_dto
    )

    # Assert
    assert expected_output[0] == actual_output[0]
    assert expected_output[1] == actual_output[1]


@pytest.mark.django_db
def test_get_requests_with_sortby_name_return_requests_count_and_request_details_dto(
        create_requests,
        requests_count_dto,
        users_requests_dtos,
        get_requests_sortby_name_dto):
    # Arrange
    request_storage = RequestStorageImplementation()
    expected_output = requests_count_dto, users_requests_dtos

    # Act
    actual_output = request_storage.get_requests(
        get_requests_sortby_name_dto
    )

    # Assert
    assert expected_output[0] == actual_output[0]
    assert expected_output[1] == actual_output[1]
