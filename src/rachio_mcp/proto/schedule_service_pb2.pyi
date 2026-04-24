import datetime

from google.protobuf import wrappers_pb2 as _wrappers_pb2
import schedule_pb2 as _schedule_pb2
import schedule_restriction_criteria_pb2 as _schedule_restriction_criteria_pb2
import schedule_criteria_pb2 as _schedule_criteria_pb2
import schedule_zone_info_pb2 as _schedule_zone_info_pb2
import core_pb2 as _core_pb2
import skip_sequence_pb2 as _skip_sequence_pb2
import schedule_run_pb2 as _schedule_run_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
import schedule_adjustment_pb2 as _schedule_adjustment_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetLocationsAndDevicesForScheduleRequest(_message.Message):
    __slots__ = ("schedule_id",)
    SCHEDULE_ID_FIELD_NUMBER: _ClassVar[int]
    schedule_id: str
    def __init__(self, schedule_id: _Optional[str] = ...) -> None: ...

class GetLocationsAndDevicesForScheduleResponse(_message.Message):
    __slots__ = ("schedule_location_info",)
    SCHEDULE_LOCATION_INFO_FIELD_NUMBER: _ClassVar[int]
    schedule_location_info: _containers.RepeatedCompositeFieldContainer[
        ScheduleLocationInfo
    ]
    def __init__(
        self,
        schedule_location_info: _Optional[
            _Iterable[_Union[ScheduleLocationInfo, _Mapping]]
        ] = ...,
    ) -> None: ...

class ScheduleLocationInfo(_message.Message):
    __slots__ = ("location_id", "device_id")
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    location_id: str
    device_id: _containers.RepeatedScalarFieldContainer[str]
    def __init__(
        self,
        location_id: _Optional[str] = ...,
        device_id: _Optional[_Iterable[str]] = ...,
    ) -> None: ...

class CreateScheduleRequest(_message.Message):
    __slots__ = (
        "name",
        "schedule_criteria",
        "schedule_restriction_criteria",
        "zone_info",
        "enabled",
        "color",
        "koppen_reduction_factor",
        "annual_start_on_notifications_enabled",
        "annual_end_on_notifications_enabled",
    )
    NAME_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_CRITERIA_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_RESTRICTION_CRITERIA_FIELD_NUMBER: _ClassVar[int]
    ZONE_INFO_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    KOPPEN_REDUCTION_FACTOR_FIELD_NUMBER: _ClassVar[int]
    ANNUAL_START_ON_NOTIFICATIONS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ANNUAL_END_ON_NOTIFICATIONS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    name: str
    schedule_criteria: _schedule_criteria_pb2.ScheduleCriteria
    schedule_restriction_criteria: (
        _schedule_restriction_criteria_pb2.ScheduleRestrictionCriteria
    )
    zone_info: _containers.RepeatedCompositeFieldContainer[
        _schedule_zone_info_pb2.ScheduleZoneInfo
    ]
    enabled: _wrappers_pb2.BoolValue
    color: _wrappers_pb2.StringValue
    koppen_reduction_factor: _wrappers_pb2.DoubleValue
    annual_start_on_notifications_enabled: bool
    annual_end_on_notifications_enabled: bool
    def __init__(
        self,
        name: _Optional[str] = ...,
        schedule_criteria: _Optional[
            _Union[_schedule_criteria_pb2.ScheduleCriteria, _Mapping]
        ] = ...,
        schedule_restriction_criteria: _Optional[
            _Union[
                _schedule_restriction_criteria_pb2.ScheduleRestrictionCriteria, _Mapping
            ]
        ] = ...,
        zone_info: _Optional[
            _Iterable[_Union[_schedule_zone_info_pb2.ScheduleZoneInfo, _Mapping]]
        ] = ...,
        enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        color: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...,
        koppen_reduction_factor: _Optional[
            _Union[_wrappers_pb2.DoubleValue, _Mapping]
        ] = ...,
        annual_start_on_notifications_enabled: bool = ...,
        annual_end_on_notifications_enabled: bool = ...,
    ) -> None: ...

class CreateScheduleResponse(_message.Message):
    __slots__ = ("schedule",)
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    schedule: _schedule_pb2.Schedule
    def __init__(
        self, schedule: _Optional[_Union[_schedule_pb2.Schedule, _Mapping]] = ...
    ) -> None: ...

class GetSchedulesRequest(_message.Message):
    __slots__ = ("schedule_id", "zone_id", "device_id", "location_id")
    SCHEDULE_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    schedule_id: _core_pb2.StringList
    zone_id: _core_pb2.StringList
    device_id: _core_pb2.StringList
    location_id: _core_pb2.StringList
    def __init__(
        self,
        schedule_id: _Optional[_Union[_core_pb2.StringList, _Mapping]] = ...,
        zone_id: _Optional[_Union[_core_pb2.StringList, _Mapping]] = ...,
        device_id: _Optional[_Union[_core_pb2.StringList, _Mapping]] = ...,
        location_id: _Optional[_Union[_core_pb2.StringList, _Mapping]] = ...,
    ) -> None: ...

class GetSchedulesResponse(_message.Message):
    __slots__ = ("schedule",)
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    schedule: _containers.RepeatedCompositeFieldContainer[_schedule_pb2.Schedule]
    def __init__(
        self,
        schedule: _Optional[_Iterable[_Union[_schedule_pb2.Schedule, _Mapping]]] = ...,
    ) -> None: ...

class UpdateScheduleRequest(_message.Message):
    __slots__ = (
        "schedule_id",
        "name",
        "schedule_criteria",
        "schedule_restriction_criteria",
        "zone_info_to_add_or_update",
        "zone_ids_to_remove",
        "enabled",
        "color",
        "koppen_reduction_factor",
        "annual_start_on_notifications_enabled",
        "annual_end_on_notifications_enabled",
        "use_forecast_weather_for_precip_skip",
    )
    SCHEDULE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_CRITERIA_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_RESTRICTION_CRITERIA_FIELD_NUMBER: _ClassVar[int]
    ZONE_INFO_TO_ADD_OR_UPDATE_FIELD_NUMBER: _ClassVar[int]
    ZONE_IDS_TO_REMOVE_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    KOPPEN_REDUCTION_FACTOR_FIELD_NUMBER: _ClassVar[int]
    ANNUAL_START_ON_NOTIFICATIONS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ANNUAL_END_ON_NOTIFICATIONS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    USE_FORECAST_WEATHER_FOR_PRECIP_SKIP_FIELD_NUMBER: _ClassVar[int]
    schedule_id: str
    name: _wrappers_pb2.StringValue
    schedule_criteria: _schedule_criteria_pb2.ScheduleCriteria
    schedule_restriction_criteria: (
        _schedule_restriction_criteria_pb2.ScheduleRestrictionCriteria
    )
    zone_info_to_add_or_update: _containers.RepeatedCompositeFieldContainer[
        _schedule_zone_info_pb2.ScheduleZoneInfo
    ]
    zone_ids_to_remove: _containers.RepeatedScalarFieldContainer[str]
    enabled: _wrappers_pb2.BoolValue
    color: _wrappers_pb2.StringValue
    koppen_reduction_factor: _wrappers_pb2.DoubleValue
    annual_start_on_notifications_enabled: _wrappers_pb2.BoolValue
    annual_end_on_notifications_enabled: _wrappers_pb2.BoolValue
    use_forecast_weather_for_precip_skip: _wrappers_pb2.BoolValue
    def __init__(
        self,
        schedule_id: _Optional[str] = ...,
        name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...,
        schedule_criteria: _Optional[
            _Union[_schedule_criteria_pb2.ScheduleCriteria, _Mapping]
        ] = ...,
        schedule_restriction_criteria: _Optional[
            _Union[
                _schedule_restriction_criteria_pb2.ScheduleRestrictionCriteria, _Mapping
            ]
        ] = ...,
        zone_info_to_add_or_update: _Optional[
            _Iterable[_Union[_schedule_zone_info_pb2.ScheduleZoneInfo, _Mapping]]
        ] = ...,
        zone_ids_to_remove: _Optional[_Iterable[str]] = ...,
        enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        color: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...,
        koppen_reduction_factor: _Optional[
            _Union[_wrappers_pb2.DoubleValue, _Mapping]
        ] = ...,
        annual_start_on_notifications_enabled: _Optional[
            _Union[_wrappers_pb2.BoolValue, _Mapping]
        ] = ...,
        annual_end_on_notifications_enabled: _Optional[
            _Union[_wrappers_pb2.BoolValue, _Mapping]
        ] = ...,
        use_forecast_weather_for_precip_skip: _Optional[
            _Union[_wrappers_pb2.BoolValue, _Mapping]
        ] = ...,
    ) -> None: ...

class UpdateScheduleResponse(_message.Message):
    __slots__ = ("schedule",)
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    schedule: _schedule_pb2.Schedule
    def __init__(
        self, schedule: _Optional[_Union[_schedule_pb2.Schedule, _Mapping]] = ...
    ) -> None: ...

class DeleteScheduleRequest(_message.Message):
    __slots__ = ("schedule_id",)
    SCHEDULE_ID_FIELD_NUMBER: _ClassVar[int]
    schedule_id: str
    def __init__(self, schedule_id: _Optional[str] = ...) -> None: ...

class DeleteScheduleResponse(_message.Message):
    __slots__ = ("deleted",)
    DELETED_FIELD_NUMBER: _ClassVar[int]
    deleted: bool
    def __init__(self, deleted: bool = ...) -> None: ...

class RunScheduleRequest(_message.Message):
    __slots__ = ("schedule_id",)
    SCHEDULE_ID_FIELD_NUMBER: _ClassVar[int]
    schedule_id: str
    def __init__(self, schedule_id: _Optional[str] = ...) -> None: ...

class RunScheduleResponse(_message.Message):
    __slots__ = ("device_id",)
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    device_id: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, device_id: _Optional[_Iterable[str]] = ...) -> None: ...

class CopyScheduleRequest(_message.Message):
    __slots__ = ("schedule_id",)
    SCHEDULE_ID_FIELD_NUMBER: _ClassVar[int]
    schedule_id: str
    def __init__(self, schedule_id: _Optional[str] = ...) -> None: ...

class CopyScheduleResponse(_message.Message):
    __slots__ = ("schedule",)
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    schedule: _schedule_pb2.Schedule
    def __init__(
        self, schedule: _Optional[_Union[_schedule_pb2.Schedule, _Mapping]] = ...
    ) -> None: ...

class SetSkipRequest(_message.Message):
    __slots__ = ("schedule_id", "disabled")
    SCHEDULE_ID_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    schedule_id: str
    disabled: bool
    def __init__(
        self, schedule_id: _Optional[str] = ..., disabled: bool = ...
    ) -> None: ...

class SetSkipResponse(_message.Message):
    __slots__ = ("skip",)
    SKIP_FIELD_NUMBER: _ClassVar[int]
    skip: _skip_sequence_pb2.SkipSequence
    def __init__(
        self, skip: _Optional[_Union[_skip_sequence_pb2.SkipSequence, _Mapping]] = ...
    ) -> None: ...

class GetScheduleRunsRequest(_message.Message):
    __slots__ = ("schedule_id", "start_time", "end_time")
    SCHEDULE_ID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    schedule_id: str
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    def __init__(
        self,
        schedule_id: _Optional[str] = ...,
        start_time: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        end_time: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
    ) -> None: ...

class GetScheduleRunsResponse(_message.Message):
    __slots__ = ("runs", "skips")
    RUNS_FIELD_NUMBER: _ClassVar[int]
    SKIPS_FIELD_NUMBER: _ClassVar[int]
    runs: _containers.RepeatedCompositeFieldContainer[_schedule_run_pb2.ScheduleRun]
    skips: _containers.RepeatedCompositeFieldContainer[_skip_sequence_pb2.SkipSequence]
    def __init__(
        self,
        runs: _Optional[
            _Iterable[_Union[_schedule_run_pb2.ScheduleRun, _Mapping]]
        ] = ...,
        skips: _Optional[
            _Iterable[_Union[_skip_sequence_pb2.SkipSequence, _Mapping]]
        ] = ...,
    ) -> None: ...

class PreviewScheduleRequest(_message.Message):
    __slots__ = (
        "name",
        "schedule_criteria",
        "schedule_restriction_criteria",
        "zone_info",
    )
    NAME_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_CRITERIA_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_RESTRICTION_CRITERIA_FIELD_NUMBER: _ClassVar[int]
    ZONE_INFO_FIELD_NUMBER: _ClassVar[int]
    name: str
    schedule_criteria: _schedule_criteria_pb2.ScheduleCriteria
    schedule_restriction_criteria: (
        _schedule_restriction_criteria_pb2.ScheduleRestrictionCriteria
    )
    zone_info: _containers.RepeatedCompositeFieldContainer[
        _schedule_zone_info_pb2.ScheduleZoneInfo
    ]
    def __init__(
        self,
        name: _Optional[str] = ...,
        schedule_criteria: _Optional[
            _Union[_schedule_criteria_pb2.ScheduleCriteria, _Mapping]
        ] = ...,
        schedule_restriction_criteria: _Optional[
            _Union[
                _schedule_restriction_criteria_pb2.ScheduleRestrictionCriteria, _Mapping
            ]
        ] = ...,
        zone_info: _Optional[
            _Iterable[_Union[_schedule_zone_info_pb2.ScheduleZoneInfo, _Mapping]]
        ] = ...,
    ) -> None: ...

class PreviewScheduleResponse(_message.Message):
    __slots__ = ("schedule",)
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    schedule: _schedule_pb2.Schedule
    def __init__(
        self, schedule: _Optional[_Union[_schedule_pb2.Schedule, _Mapping]] = ...
    ) -> None: ...

class GetScheduleAdjustmentRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetScheduleAdjustmentResponse(_message.Message):
    __slots__ = ("schedule_adjustment",)
    SCHEDULE_ADJUSTMENT_FIELD_NUMBER: _ClassVar[int]
    schedule_adjustment: _schedule_adjustment_pb2.ScheduleAdjustment
    def __init__(
        self,
        schedule_adjustment: _Optional[
            _Union[_schedule_adjustment_pb2.ScheduleAdjustment, _Mapping]
        ] = ...,
    ) -> None: ...

class ListScheduleAdjustmentsByDeviceIdRequest(_message.Message):
    __slots__ = ("device_id",)
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    def __init__(self, device_id: _Optional[str] = ...) -> None: ...

class ListScheduleAdjustmentsByDeviceIdResponse(_message.Message):
    __slots__ = ("schedule_adjustments",)
    SCHEDULE_ADJUSTMENTS_FIELD_NUMBER: _ClassVar[int]
    schedule_adjustments: _containers.RepeatedCompositeFieldContainer[
        _schedule_adjustment_pb2.ScheduleAdjustment
    ]
    def __init__(
        self,
        schedule_adjustments: _Optional[
            _Iterable[_Union[_schedule_adjustment_pb2.ScheduleAdjustment, _Mapping]]
        ] = ...,
    ) -> None: ...

class UpdateScheduleAdjustmentRequest(_message.Message):
    __slots__ = ("id", "state")
    ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    id: str
    state: _schedule_adjustment_pb2.ScheduleAdjustmentStateWrapper
    def __init__(
        self,
        id: _Optional[str] = ...,
        state: _Optional[
            _Union[_schedule_adjustment_pb2.ScheduleAdjustmentStateWrapper, _Mapping]
        ] = ...,
    ) -> None: ...

class UpdateScheduleAdjustmentResponse(_message.Message):
    __slots__ = ("schedule_adjustment",)
    SCHEDULE_ADJUSTMENT_FIELD_NUMBER: _ClassVar[int]
    schedule_adjustment: _schedule_adjustment_pb2.ScheduleAdjustment
    def __init__(
        self,
        schedule_adjustment: _Optional[
            _Union[_schedule_adjustment_pb2.ScheduleAdjustment, _Mapping]
        ] = ...,
    ) -> None: ...
