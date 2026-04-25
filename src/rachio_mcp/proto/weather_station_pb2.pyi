import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
import core_pb2 as _core_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WeatherStationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NATIONAL: _ClassVar[WeatherStationType]
    PWS: _ClassVar[WeatherStationType]
    WEATHER_FLOW: _ClassVar[WeatherStationType]
NATIONAL: WeatherStationType
PWS: WeatherStationType
WEATHER_FLOW: WeatherStationType

class VirtualWeatherStation(_message.Message):
    __slots__ = ("id", "station_id", "geo_point", "location_id", "has_precip", "stationType", "created", "updated", "distance")
    ID_FIELD_NUMBER: _ClassVar[int]
    STATION_ID_FIELD_NUMBER: _ClassVar[int]
    GEO_POINT_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    HAS_PRECIP_FIELD_NUMBER: _ClassVar[int]
    STATIONTYPE_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_FIELD_NUMBER: _ClassVar[int]
    id: str
    station_id: str
    geo_point: _core_pb2.GeoPoint
    location_id: str
    has_precip: bool
    stationType: WeatherStationType
    created: _timestamp_pb2.Timestamp
    updated: _timestamp_pb2.Timestamp
    distance: float
    def __init__(self, id: _Optional[str] = ..., station_id: _Optional[str] = ..., geo_point: _Optional[_Union[_core_pb2.GeoPoint, _Mapping]] = ..., location_id: _Optional[str] = ..., has_precip: bool = ..., stationType: _Optional[_Union[WeatherStationType, str]] = ..., created: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., distance: _Optional[float] = ...) -> None: ...

class WeatherStation(_message.Message):
    __slots__ = ("station_id", "geo_point", "city", "state", "country", "has_precip", "stationType", "more_info_url", "distance", "elevation")
    STATION_ID_FIELD_NUMBER: _ClassVar[int]
    GEO_POINT_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    HAS_PRECIP_FIELD_NUMBER: _ClassVar[int]
    STATIONTYPE_FIELD_NUMBER: _ClassVar[int]
    MORE_INFO_URL_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_FIELD_NUMBER: _ClassVar[int]
    ELEVATION_FIELD_NUMBER: _ClassVar[int]
    station_id: str
    geo_point: _core_pb2.GeoPoint
    city: str
    state: str
    country: str
    has_precip: bool
    stationType: WeatherStationType
    more_info_url: str
    distance: float
    elevation: int
    def __init__(self, station_id: _Optional[str] = ..., geo_point: _Optional[_Union[_core_pb2.GeoPoint, _Mapping]] = ..., city: _Optional[str] = ..., state: _Optional[str] = ..., country: _Optional[str] = ..., has_precip: bool = ..., stationType: _Optional[_Union[WeatherStationType, str]] = ..., more_info_url: _Optional[str] = ..., distance: _Optional[float] = ..., elevation: _Optional[int] = ...) -> None: ...
