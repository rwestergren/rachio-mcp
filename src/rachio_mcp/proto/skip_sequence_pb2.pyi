import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SkipSequence(_message.Message):
    __slots__ = ("id", "schedule_id", "start_time", "end_time", "cause", "disabled", "force", "weather_station_id", "schedule_name")
    class SkipCause(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MANUAL: _ClassVar[SkipSequence.SkipCause]
        FREEZE: _ClassVar[SkipSequence.SkipCause]
        WIND: _ClassVar[SkipSequence.SkipCause]
        CLIMATE: _ClassVar[SkipSequence.SkipCause]
        RAIN: _ClassVar[SkipSequence.SkipCause]
        NONE: _ClassVar[SkipSequence.SkipCause]
    MANUAL: SkipSequence.SkipCause
    FREEZE: SkipSequence.SkipCause
    WIND: SkipSequence.SkipCause
    CLIMATE: SkipSequence.SkipCause
    RAIN: SkipSequence.SkipCause
    NONE: SkipSequence.SkipCause
    ID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_ID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    CAUSE_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    WEATHER_STATION_ID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    schedule_id: _wrappers_pb2.StringValue
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    cause: SkipSequence.SkipCause
    disabled: bool
    force: bool
    weather_station_id: str
    schedule_name: str
    def __init__(self, id: _Optional[str] = ..., schedule_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., start_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., cause: _Optional[_Union[SkipSequence.SkipCause, str]] = ..., disabled: bool = ..., force: bool = ..., weather_station_id: _Optional[str] = ..., schedule_name: _Optional[str] = ...) -> None: ...
