from google.protobuf import timestamp_pb2 as _timestamp_pb2
import core_pb2 as _core_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ScheduleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FIXED: _ClassVar[ScheduleType]
    FLEX_MONTHLY: _ClassVar[ScheduleType]
    FLEX_DAILY: _ClassVar[ScheduleType]
FIXED: ScheduleType
FLEX_MONTHLY: ScheduleType
FLEX_DAILY: ScheduleType

class ScheduleCriteria(_message.Message):
    __slots__ = ("schedule_type", "start_date", "end_date", "annual_start_date", "annual_end_date", "rain_delay_enabled", "freeze_delay_enabled", "wind_delay_enabled", "climate_skip", "seasonal_shift", "smart_cycle", "cycle_soak", "soak_time", "cycle_time", "zone_delay_time", "start_time_set", "start_sun_time", "end_time_set", "end_sun_time", "start_time_with_end_time_boundary")
    SCHEDULE_TYPE_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    ANNUAL_START_DATE_FIELD_NUMBER: _ClassVar[int]
    ANNUAL_END_DATE_FIELD_NUMBER: _ClassVar[int]
    RAIN_DELAY_ENABLED_FIELD_NUMBER: _ClassVar[int]
    FREEZE_DELAY_ENABLED_FIELD_NUMBER: _ClassVar[int]
    WIND_DELAY_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CLIMATE_SKIP_FIELD_NUMBER: _ClassVar[int]
    SEASONAL_SHIFT_FIELD_NUMBER: _ClassVar[int]
    SMART_CYCLE_FIELD_NUMBER: _ClassVar[int]
    CYCLE_SOAK_FIELD_NUMBER: _ClassVar[int]
    SOAK_TIME_FIELD_NUMBER: _ClassVar[int]
    CYCLE_TIME_FIELD_NUMBER: _ClassVar[int]
    ZONE_DELAY_TIME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_SET_FIELD_NUMBER: _ClassVar[int]
    START_SUN_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_SET_FIELD_NUMBER: _ClassVar[int]
    END_SUN_TIME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_WITH_END_TIME_BOUNDARY_FIELD_NUMBER: _ClassVar[int]
    schedule_type: ScheduleType
    start_date: _core_pb2.Date
    end_date: _core_pb2.Date
    annual_start_date: _core_pb2.CalendarDate
    annual_end_date: _core_pb2.CalendarDate
    rain_delay_enabled: bool
    freeze_delay_enabled: bool
    wind_delay_enabled: bool
    climate_skip: bool
    seasonal_shift: bool
    smart_cycle: bool
    cycle_soak: bool
    soak_time: int
    cycle_time: int
    zone_delay_time: int
    start_time_set: _core_pb2.TimeList
    start_sun_time: str
    end_time_set: _core_pb2.TimeList
    end_sun_time: str
    start_time_with_end_time_boundary: _core_pb2.TimeInterval
    def __init__(self, schedule_type: _Optional[_Union[ScheduleType, str]] = ..., start_date: _Optional[_Union[_core_pb2.Date, _Mapping]] = ..., end_date: _Optional[_Union[_core_pb2.Date, _Mapping]] = ..., annual_start_date: _Optional[_Union[_core_pb2.CalendarDate, _Mapping]] = ..., annual_end_date: _Optional[_Union[_core_pb2.CalendarDate, _Mapping]] = ..., rain_delay_enabled: bool = ..., freeze_delay_enabled: bool = ..., wind_delay_enabled: bool = ..., climate_skip: bool = ..., seasonal_shift: bool = ..., smart_cycle: bool = ..., cycle_soak: bool = ..., soak_time: _Optional[int] = ..., cycle_time: _Optional[int] = ..., zone_delay_time: _Optional[int] = ..., start_time_set: _Optional[_Union[_core_pb2.TimeList, _Mapping]] = ..., start_sun_time: _Optional[str] = ..., end_time_set: _Optional[_Union[_core_pb2.TimeList, _Mapping]] = ..., end_sun_time: _Optional[str] = ..., start_time_with_end_time_boundary: _Optional[_Union[_core_pb2.TimeInterval, _Mapping]] = ...) -> None: ...
