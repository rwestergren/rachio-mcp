import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
import core_pb2 as _core_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN: _ClassVar[DeviceType]
    CONTROLLER_GEN1: _ClassVar[DeviceType]
    CONTROLLER_GEN2: _ClassVar[DeviceType]
    SENSOR_LINKED: _ClassVar[DeviceType]
    WEATHER_STATION_PHYSICAL: _ClassVar[DeviceType]
    WEATHER_STATION_VIRTUAL: _ClassVar[DeviceType]
    CONTROLLER_GEN3: _ClassVar[DeviceType]
    WIRELESS_FLOW_SENSOR: _ClassVar[DeviceType]
    CONTROLLER_VIRTUAL: _ClassVar[DeviceType]

class WiringPosition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SLOT_ONE: _ClassVar[WiringPosition]
    SLOT_TWO: _ClassVar[WiringPosition]
UNKNOWN: DeviceType
CONTROLLER_GEN1: DeviceType
CONTROLLER_GEN2: DeviceType
SENSOR_LINKED: DeviceType
WEATHER_STATION_PHYSICAL: DeviceType
WEATHER_STATION_VIRTUAL: DeviceType
CONTROLLER_GEN3: DeviceType
WIRELESS_FLOW_SENSOR: DeviceType
CONTROLLER_VIRTUAL: DeviceType
SLOT_ONE: WiringPosition
SLOT_TWO: WiringPosition

class Device(_message.Message):
    __slots__ = ("id", "type", "created", "updated", "name", "geo_point", "location_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    GEO_POINT_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    type: DeviceType
    created: _timestamp_pb2.Timestamp
    updated: _timestamp_pb2.Timestamp
    name: str
    geo_point: _core_pb2.GeoPoint
    location_id: str
    def __init__(self, id: _Optional[str] = ..., type: _Optional[_Union[DeviceType, str]] = ..., created: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., name: _Optional[str] = ..., geo_point: _Optional[_Union[_core_pb2.GeoPoint, _Mapping]] = ..., location_id: _Optional[str] = ...) -> None: ...
