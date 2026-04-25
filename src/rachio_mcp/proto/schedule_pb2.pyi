import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
import schedule_criteria_pb2 as _schedule_criteria_pb2
import schedule_restriction_criteria_pb2 as _schedule_restriction_criteria_pb2
import schedule_zone_info_pb2 as _schedule_zone_info_pb2
import schedule_adjustment_pb2 as _schedule_adjustment_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Schedule(_message.Message):
    __slots__ = ("id", "name", "schedule_criteria", "schedule_restriction_criteria", "zone_info", "enabled", "created", "updated", "summary", "color", "koppen_reduction_factor", "annual_start_on_notifications_enabled", "annual_end_on_notifications_enabled", "use_forecast_weather_for_precip_skip", "schedule_adjustments")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_CRITERIA_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_RESTRICTION_CRITERIA_FIELD_NUMBER: _ClassVar[int]
    ZONE_INFO_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    KOPPEN_REDUCTION_FACTOR_FIELD_NUMBER: _ClassVar[int]
    ANNUAL_START_ON_NOTIFICATIONS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ANNUAL_END_ON_NOTIFICATIONS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    USE_FORECAST_WEATHER_FOR_PRECIP_SKIP_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_ADJUSTMENTS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    schedule_criteria: _schedule_criteria_pb2.ScheduleCriteria
    schedule_restriction_criteria: _schedule_restriction_criteria_pb2.ScheduleRestrictionCriteria
    zone_info: _containers.RepeatedCompositeFieldContainer[_schedule_zone_info_pb2.ScheduleZoneInfo]
    enabled: bool
    created: _timestamp_pb2.Timestamp
    updated: _timestamp_pb2.Timestamp
    summary: str
    color: _wrappers_pb2.StringValue
    koppen_reduction_factor: _wrappers_pb2.DoubleValue
    annual_start_on_notifications_enabled: bool
    annual_end_on_notifications_enabled: bool
    use_forecast_weather_for_precip_skip: bool
    schedule_adjustments: _containers.RepeatedCompositeFieldContainer[_schedule_adjustment_pb2.ScheduleAdjustment]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., schedule_criteria: _Optional[_Union[_schedule_criteria_pb2.ScheduleCriteria, _Mapping]] = ..., schedule_restriction_criteria: _Optional[_Union[_schedule_restriction_criteria_pb2.ScheduleRestrictionCriteria, _Mapping]] = ..., zone_info: _Optional[_Iterable[_Union[_schedule_zone_info_pb2.ScheduleZoneInfo, _Mapping]]] = ..., enabled: bool = ..., created: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., summary: _Optional[str] = ..., color: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., koppen_reduction_factor: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., annual_start_on_notifications_enabled: bool = ..., annual_end_on_notifications_enabled: bool = ..., use_forecast_weather_for_precip_skip: bool = ..., schedule_adjustments: _Optional[_Iterable[_Union[_schedule_adjustment_pb2.ScheduleAdjustment, _Mapping]]] = ...) -> None: ...
