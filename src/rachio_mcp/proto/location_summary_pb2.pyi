import location_pb2 as _location_pb2
import location_state_pb2 as _location_state_pb2
import user_pb2 as _user_pb2
import alert_pb2 as _alert_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LocationSummary(_message.Message):
    __slots__ = ("location", "state", "owner", "favorite", "has_messages", "tier_one_count", "tier_two_count", "active_alert_types")
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    FAVORITE_FIELD_NUMBER: _ClassVar[int]
    HAS_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    TIER_ONE_COUNT_FIELD_NUMBER: _ClassVar[int]
    TIER_TWO_COUNT_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_ALERT_TYPES_FIELD_NUMBER: _ClassVar[int]
    location: _location_pb2.Location
    state: _location_state_pb2.LocationState
    owner: _user_pb2.User
    favorite: bool
    has_messages: bool
    tier_one_count: int
    tier_two_count: int
    active_alert_types: _containers.RepeatedScalarFieldContainer[_alert_pb2.AlertType]
    def __init__(self, location: _Optional[_Union[_location_pb2.Location, _Mapping]] = ..., state: _Optional[_Union[_location_state_pb2.LocationState, _Mapping]] = ..., owner: _Optional[_Union[_user_pb2.User, _Mapping]] = ..., favorite: bool = ..., has_messages: bool = ..., tier_one_count: _Optional[int] = ..., tier_two_count: _Optional[int] = ..., active_alert_types: _Optional[_Iterable[_Union[_alert_pb2.AlertType, str]]] = ...) -> None: ...
