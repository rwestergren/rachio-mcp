import datetime

import schedule_criteria_pb2 as _schedule_criteria_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RunType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IRRIGATE: _ClassVar[RunType]
    CYCLE: _ClassVar[RunType]
    PAUSE: _ClassVar[RunType]
IRRIGATE: RunType
CYCLE: RunType
PAUSE: RunType

class ScheduleRun(_message.Message):
    __slots__ = ("schedule_id", "start_time", "end_time", "schedule_type", "zone_runs", "schedule_name", "icon_url")
    SCHEDULE_ID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ZONE_RUNS_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_URL_FIELD_NUMBER: _ClassVar[int]
    schedule_id: str
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    schedule_type: _schedule_criteria_pb2.ScheduleType
    zone_runs: _containers.RepeatedCompositeFieldContainer[ScheduleZoneRun]
    schedule_name: _wrappers_pb2.StringValue
    icon_url: str
    def __init__(self, schedule_id: _Optional[str] = ..., start_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., schedule_type: _Optional[_Union[_schedule_criteria_pb2.ScheduleType, str]] = ..., zone_runs: _Optional[_Iterable[_Union[ScheduleZoneRun, _Mapping]]] = ..., schedule_name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., icon_url: _Optional[str] = ...) -> None: ...

class ScheduleZoneRun(_message.Message):
    __slots__ = ("type", "start_time", "end_time", "zone_name", "zone_id", "photo_id", "zone_number")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    ZONE_NAME_FIELD_NUMBER: _ClassVar[int]
    ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    PHOTO_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    type: RunType
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    zone_name: str
    zone_id: str
    photo_id: str
    zone_number: int
    def __init__(self, type: _Optional[_Union[RunType, str]] = ..., start_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., zone_name: _Optional[str] = ..., zone_id: _Optional[str] = ..., photo_id: _Optional[str] = ..., zone_number: _Optional[int] = ...) -> None: ...
