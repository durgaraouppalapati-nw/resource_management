import enum

from ib_common.constants import BaseEnumClass


class Confirmation(BaseEnumClass, enum.Enum):
    ACCEPT = 'ACCEPTED'
    REJECT = 'REJECTED'
    PENDING = 'PENDING'


class SortRequests(BaseEnumClass, enum.Enum):
    RESOURCE = 'RESOURCE'
    ITEM = 'ITEM'
    NAME = 'NAME'
    DUE_DATETIME = 'DUE_DATETIME'
    ACCESSLEVEL = 'ACCESSLEVEL'
    STATUS = 'STATUS'


class FilterRequests(BaseEnumClass, enum.Enum):
    NAME = 'NAME'
    RESOURCE = 'RESOURCE'
    ACCESSLEVEL = 'ACCESSLEVEL'
    STATUS = 'STATUS'


class Gender(BaseEnumClass, enum.Enum):
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    OTHER = 'OTHER'


class SearchBy(BaseEnumClass, enum.Enum):
    RESOURCE = "RESOURCE"
    ITEM = "ITEM"
