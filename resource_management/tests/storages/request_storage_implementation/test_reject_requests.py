import pytest

from resource_management.storages.request_storage_implementation import \
    RequestStorageImplementation
from resource_management.models import Request


@pytest.mark.django_db
def test_reject_requests_updates_request_status(requests):
    # Arrange
    request_storage = RequestStorageImplementation()
    request_ids = [1, 2, 3]
    reason_for_rejection = "For now it is not accesseble for u"

    # Act
    request_storage.reject_requests(
        request_ids=request_ids, reason_for_rejection=reason_for_rejection
    )

    # Assert
    request_objs = Request.objects.filter(id__in=request_ids)
    for request in request_objs:
        assert request.request_status == "REJECTED"
        assert request.reason_for_rejection == reason_for_rejection
