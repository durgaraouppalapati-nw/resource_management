from resource_management.exceptions.exceptions import (
    InvalidOffsetValue, InvalidLimitValue
)


class LimitOffsetValidationMixin:

    def check_is_valid_offset_value(self, offset: int):
        if offset < 0:
            raise InvalidOffsetValue

    def check_is_valid_limit_value(self, limit: int):
        if limit < 0:
            raise InvalidLimitValue
