from google.protobuf import wrappers_pb2 as _wrappers_pb2
import core_pb2 as _core_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ScheduleAdjustmentState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PENDING: _ClassVar[ScheduleAdjustmentState]
    IGNORED: _ClassVar[ScheduleAdjustmentState]
    APPLIED: _ClassVar[ScheduleAdjustmentState]
PENDING: ScheduleAdjustmentState
IGNORED: ScheduleAdjustmentState
APPLIED: ScheduleAdjustmentState

class ScheduleAdjustment(_message.Message):
    __slots__ = ("id", "schedule_id", "start_date", "end_date", "watering_time_multiplier", "state", "watering_cadence_adjustment", "temperature_monitoring_watering_adjustment_id")
    class WateringCadenceAdjustment(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_ADJUSTMENT: _ClassVar[ScheduleAdjustment.WateringCadenceAdjustment]
        WATER_EVERY_DAY: _ClassVar[ScheduleAdjustment.WateringCadenceAdjustment]
    NO_ADJUSTMENT: ScheduleAdjustment.WateringCadenceAdjustment
    WATER_EVERY_DAY: ScheduleAdjustment.WateringCadenceAdjustment
    ID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_ID_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    WATERING_TIME_MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    WATERING_CADENCE_ADJUSTMENT_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_MONITORING_WATERING_ADJUSTMENT_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    schedule_id: str
    start_date: _core_pb2.Date
    end_date: _core_pb2.Date
    watering_time_multiplier: _wrappers_pb2.DoubleValue
    state: ScheduleAdjustmentState
    watering_cadence_adjustment: ScheduleAdjustment.WateringCadenceAdjustment
    temperature_monitoring_watering_adjustment_id: _wrappers_pb2.StringValue
    def __init__(self, id: _Optional[str] = ..., schedule_id: _Optional[str] = ..., start_date: _Optional[_Union[_core_pb2.Date, _Mapping]] = ..., end_date: _Optional[_Union[_core_pb2.Date, _Mapping]] = ..., watering_time_multiplier: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., state: _Optional[_Union[ScheduleAdjustmentState, str]] = ..., watering_cadence_adjustment: _Optional[_Union[ScheduleAdjustment.WateringCadenceAdjustment, str]] = ..., temperature_monitoring_watering_adjustment_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class ScheduleAdjustmentStateWrapper(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: ScheduleAdjustmentState
    def __init__(self, value: _Optional[_Union[ScheduleAdjustmentState, str]] = ...) -> None: ...
