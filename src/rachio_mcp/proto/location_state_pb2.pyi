import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LocationState(_message.Message):
    __slots__ = ("location_id", "health", "state", "last_run", "next_run", "usage_liters", "local_average_usage_liters", "firmware_version")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STANDBY: _ClassVar[LocationState.State]
        IDLE: _ClassVar[LocationState.State]
        DELAY: _ClassVar[LocationState.State]
        PAUSED: _ClassVar[LocationState.State]
        WATERING: _ClassVar[LocationState.State]
        UNKNOWN: _ClassVar[LocationState.State]
        UNBORN: _ClassVar[LocationState.State]
        STARTUP: _ClassVar[LocationState.State]
        OFFLINE: _ClassVar[LocationState.State]
        EXTENDED_OFFLINE: _ClassVar[LocationState.State]
        PROVISIONING: _ClassVar[LocationState.State]
    STANDBY: LocationState.State
    IDLE: LocationState.State
    DELAY: LocationState.State
    PAUSED: LocationState.State
    WATERING: LocationState.State
    UNKNOWN: LocationState.State
    UNBORN: LocationState.State
    STARTUP: LocationState.State
    OFFLINE: LocationState.State
    EXTENDED_OFFLINE: LocationState.State
    PROVISIONING: LocationState.State
    class Health(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        GOOD: _ClassVar[LocationState.Health]
        WARNING: _ClassVar[LocationState.Health]
        ERROR: _ClassVar[LocationState.Health]
    GOOD: LocationState.Health
    WARNING: LocationState.Health
    ERROR: LocationState.Health
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    HEALTH_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    LAST_RUN_FIELD_NUMBER: _ClassVar[int]
    NEXT_RUN_FIELD_NUMBER: _ClassVar[int]
    USAGE_LITERS_FIELD_NUMBER: _ClassVar[int]
    LOCAL_AVERAGE_USAGE_LITERS_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    location_id: str
    health: LocationState.Health
    state: LocationState.State
    last_run: _timestamp_pb2.Timestamp
    next_run: _timestamp_pb2.Timestamp
    usage_liters: float
    local_average_usage_liters: float
    firmware_version: str
    def __init__(self, location_id: _Optional[str] = ..., health: _Optional[_Union[LocationState.Health, str]] = ..., state: _Optional[_Union[LocationState.State, str]] = ..., last_run: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., next_run: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., usage_liters: _Optional[float] = ..., local_average_usage_liters: _Optional[float] = ..., firmware_version: _Optional[str] = ...) -> None: ...
