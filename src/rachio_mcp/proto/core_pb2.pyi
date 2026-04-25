import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DisplayUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    METRIC: _ClassVar[DisplayUnit]
    IMPERIAL: _ClassVar[DisplayUnit]

class DayOfWeek(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MONDAY: _ClassVar[DayOfWeek]
    TUESDAY: _ClassVar[DayOfWeek]
    WEDNESDAY: _ClassVar[DayOfWeek]
    THURSDAY: _ClassVar[DayOfWeek]
    FRIDAY: _ClassVar[DayOfWeek]
    SATURDAY: _ClassVar[DayOfWeek]
    SUNDAY: _ClassVar[DayOfWeek]

class OddDay(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ODD_DAY_DISABLED: _ClassVar[OddDay]
    ODD: _ClassVar[OddDay]
    EVEN: _ClassVar[OddDay]
METRIC: DisplayUnit
IMPERIAL: DisplayUnit
MONDAY: DayOfWeek
TUESDAY: DayOfWeek
WEDNESDAY: DayOfWeek
THURSDAY: DayOfWeek
FRIDAY: DayOfWeek
SATURDAY: DayOfWeek
SUNDAY: DayOfWeek
ODD_DAY_DISABLED: OddDay
ODD: OddDay
EVEN: OddDay

class GeoPoint(_message.Message):
    __slots__ = ("latitude", "longitude")
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    latitude: float
    longitude: float
    def __init__(self, latitude: _Optional[float] = ..., longitude: _Optional[float] = ...) -> None: ...

class Address(_message.Message):
    __slots__ = ("address_line_1", "address_line_2", "city", "county", "region", "postal_code", "country")
    ADDRESS_LINE_1_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_LINE_2_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    COUNTY_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    POSTAL_CODE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    address_line_1: str
    address_line_2: str
    city: str
    county: str
    region: Region
    postal_code: str
    country: Country
    def __init__(self, address_line_1: _Optional[str] = ..., address_line_2: _Optional[str] = ..., city: _Optional[str] = ..., county: _Optional[str] = ..., region: _Optional[_Union[Region, _Mapping]] = ..., postal_code: _Optional[str] = ..., country: _Optional[_Union[Country, _Mapping]] = ...) -> None: ...

class Region(_message.Message):
    __slots__ = ("name", "code")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    name: str
    code: str
    def __init__(self, name: _Optional[str] = ..., code: _Optional[str] = ...) -> None: ...

class Country(_message.Message):
    __slots__ = ("name", "code")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    name: str
    code: str
    def __init__(self, name: _Optional[str] = ..., code: _Optional[str] = ...) -> None: ...

class TimeList(_message.Message):
    __slots__ = ("time",)
    TIME_FIELD_NUMBER: _ClassVar[int]
    time: _containers.RepeatedCompositeFieldContainer[Time]
    def __init__(self, time: _Optional[_Iterable[_Union[Time, _Mapping]]] = ...) -> None: ...

class StringList(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[_Iterable[str]] = ...) -> None: ...

class TimeInterval(_message.Message):
    __slots__ = ("start", "end")
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    start: Time
    end: Time
    def __init__(self, start: _Optional[_Union[Time, _Mapping]] = ..., end: _Optional[_Union[Time, _Mapping]] = ...) -> None: ...

class DateInterval(_message.Message):
    __slots__ = ("start", "end")
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    start: Date
    end: Date
    def __init__(self, start: _Optional[_Union[Date, _Mapping]] = ..., end: _Optional[_Union[Date, _Mapping]] = ...) -> None: ...

class TimestampInterval(_message.Message):
    __slots__ = ("start", "end")
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    start: _timestamp_pb2.Timestamp
    end: _timestamp_pb2.Timestamp
    def __init__(self, start: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Date(_message.Message):
    __slots__ = ("year", "month", "day")
    YEAR_FIELD_NUMBER: _ClassVar[int]
    MONTH_FIELD_NUMBER: _ClassVar[int]
    DAY_FIELD_NUMBER: _ClassVar[int]
    year: int
    month: int
    day: int
    def __init__(self, year: _Optional[int] = ..., month: _Optional[int] = ..., day: _Optional[int] = ...) -> None: ...

class CalendarDate(_message.Message):
    __slots__ = ("month", "day")
    MONTH_FIELD_NUMBER: _ClassVar[int]
    DAY_FIELD_NUMBER: _ClassVar[int]
    month: int
    day: int
    def __init__(self, month: _Optional[int] = ..., day: _Optional[int] = ...) -> None: ...

class Time(_message.Message):
    __slots__ = ("hour", "minute", "second", "millis")
    HOUR_FIELD_NUMBER: _ClassVar[int]
    MINUTE_FIELD_NUMBER: _ClassVar[int]
    SECOND_FIELD_NUMBER: _ClassVar[int]
    MILLIS_FIELD_NUMBER: _ClassVar[int]
    hour: int
    minute: int
    second: int
    millis: int
    def __init__(self, hour: _Optional[int] = ..., minute: _Optional[int] = ..., second: _Optional[int] = ..., millis: _Optional[int] = ...) -> None: ...

class NullableString(_message.Message):
    __slots__ = ("null", "data")
    NULL_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    null: _struct_pb2.NullValue
    data: str
    def __init__(self, null: _Optional[_Union[_struct_pb2.NullValue, str]] = ..., data: _Optional[str] = ...) -> None: ...
