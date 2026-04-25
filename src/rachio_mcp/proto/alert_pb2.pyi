import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AlertType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ZONE_HIGH_FLOW: _ClassVar[AlertType]
    ZONE_LOW_FLOW: _ClassVar[AlertType]
    ZONE_HIGH_FLOW_NO_SHUTOFF: _ClassVar[AlertType]
    ZONE_HIGH_FLOW_SHUTOFF: _ClassVar[AlertType]
    ZONE_LOW_AMPERAGE: _ClassVar[AlertType]
    ZONE_HIGH_AMPERAGE: _ClassVar[AlertType]
ZONE_HIGH_FLOW: AlertType
ZONE_LOW_FLOW: AlertType
ZONE_HIGH_FLOW_NO_SHUTOFF: AlertType
ZONE_HIGH_FLOW_SHUTOFF: AlertType
ZONE_LOW_AMPERAGE: AlertType
ZONE_HIGH_AMPERAGE: AlertType

class Alert(_message.Message):
    __slots__ = ("id", "entity_id", "type", "title", "subtitle", "summary", "dismissed", "dismissed_timestamp", "created", "updated")
    ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    SUBTITLE_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    DISMISSED_FIELD_NUMBER: _ClassVar[int]
    DISMISSED_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    id: str
    entity_id: str
    type: AlertType
    title: str
    subtitle: str
    summary: str
    dismissed: bool
    dismissed_timestamp: _timestamp_pb2.Timestamp
    created: _timestamp_pb2.Timestamp
    updated: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., entity_id: _Optional[str] = ..., type: _Optional[_Union[AlertType, str]] = ..., title: _Optional[str] = ..., subtitle: _Optional[str] = ..., summary: _Optional[str] = ..., dismissed: bool = ..., dismissed_timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
