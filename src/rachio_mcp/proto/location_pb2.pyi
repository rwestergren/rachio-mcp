import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
import core_pb2 as _core_pb2
import location_threshold_pb2 as _location_threshold_pb2
import device_pb2 as _device_pb2
import schedule_criteria_pb2 as _schedule_criteria_pb2
import skip_sequence_pb2 as _skip_sequence_pb2
import weather_station_pb2 as _weather_station_pb2
import irrigation_controller_pb2 as _irrigation_controller_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Location(_message.Message):
    __slots__ = ("id", "created", "updated", "name", "device_id", "devices", "address", "geo_point", "photo_id", "time_zone", "include_all_weather_stations", "owner", "threshold", "subscription_ids", "weather_station_id", "irrigation_controller_properties")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICES_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    GEO_POINT_FIELD_NUMBER: _ClassVar[int]
    PHOTO_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ALL_WEATHER_STATIONS_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_IDS_FIELD_NUMBER: _ClassVar[int]
    WEATHER_STATION_ID_FIELD_NUMBER: _ClassVar[int]
    IRRIGATION_CONTROLLER_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    id: str
    created: _timestamp_pb2.Timestamp
    updated: _timestamp_pb2.Timestamp
    name: str
    device_id: _containers.RepeatedScalarFieldContainer[str]
    devices: _containers.RepeatedCompositeFieldContainer[DeviceInfo]
    address: _core_pb2.Address
    geo_point: _core_pb2.GeoPoint
    photo_id: str
    time_zone: str
    include_all_weather_stations: bool
    owner: bool
    threshold: _containers.RepeatedCompositeFieldContainer[_location_threshold_pb2.LocationThreshold]
    subscription_ids: _containers.RepeatedScalarFieldContainer[str]
    weather_station_id: _wrappers_pb2.StringValue
    irrigation_controller_properties: _irrigation_controller_pb2.IrrigationControllerProperties
    def __init__(self, id: _Optional[str] = ..., created: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., name: _Optional[str] = ..., device_id: _Optional[_Iterable[str]] = ..., devices: _Optional[_Iterable[_Union[DeviceInfo, _Mapping]]] = ..., address: _Optional[_Union[_core_pb2.Address, _Mapping]] = ..., geo_point: _Optional[_Union[_core_pb2.GeoPoint, _Mapping]] = ..., photo_id: _Optional[str] = ..., time_zone: _Optional[str] = ..., include_all_weather_stations: bool = ..., owner: bool = ..., threshold: _Optional[_Iterable[_Union[_location_threshold_pb2.LocationThreshold, _Mapping]]] = ..., subscription_ids: _Optional[_Iterable[str]] = ..., weather_station_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., irrigation_controller_properties: _Optional[_Union[_irrigation_controller_pb2.IrrigationControllerProperties, _Mapping]] = ...) -> None: ...

class DeviceInfo(_message.Message):
    __slots__ = ("id", "type", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    type: _device_pb2.DeviceType
    name: str
    def __init__(self, id: _Optional[str] = ..., type: _Optional[_Union[_device_pb2.DeviceType, str]] = ..., name: _Optional[str] = ...) -> None: ...

class WateringDay(_message.Message):
    __slots__ = ("schedule_id", "schedule_type", "date", "skipped", "schedule_name", "start_time", "end_time")
    class SkipCause(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MANUAL: _ClassVar[WateringDay.SkipCause]
        FREEZE: _ClassVar[WateringDay.SkipCause]
        WIND: _ClassVar[WateringDay.SkipCause]
        CLIMATE: _ClassVar[WateringDay.SkipCause]
        RAIN: _ClassVar[WateringDay.SkipCause]
        NONE: _ClassVar[WateringDay.SkipCause]
    MANUAL: WateringDay.SkipCause
    FREEZE: WateringDay.SkipCause
    WIND: WateringDay.SkipCause
    CLIMATE: WateringDay.SkipCause
    RAIN: WateringDay.SkipCause
    NONE: WateringDay.SkipCause
    SCHEDULE_ID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    SKIPPED_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_NAME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    schedule_id: str
    schedule_type: _schedule_criteria_pb2.ScheduleType
    date: _core_pb2.Date
    skipped: bool
    schedule_name: str
    start_time: _core_pb2.Time
    end_time: _core_pb2.Time
    def __init__(self, schedule_id: _Optional[str] = ..., schedule_type: _Optional[_Union[_schedule_criteria_pb2.ScheduleType, str]] = ..., date: _Optional[_Union[_core_pb2.Date, _Mapping]] = ..., skipped: bool = ..., schedule_name: _Optional[str] = ..., start_time: _Optional[_Union[_core_pb2.Time, _Mapping]] = ..., end_time: _Optional[_Union[_core_pb2.Time, _Mapping]] = ...) -> None: ...
