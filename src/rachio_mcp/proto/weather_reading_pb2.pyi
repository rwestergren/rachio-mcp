import core_pb2 as _core_pb2
import weather_type_pb2 as _weather_type_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IReadingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OBSERVED: _ClassVar[IReadingType]
    FORECASTED: _ClassVar[IReadingType]

OBSERVED: IReadingType
FORECASTED: IReadingType

class WeatherReading(_message.Message):
    __slots__ = (
        "temperature_min",
        "temperature_max",
        "precip_intensity",
        "precip_probability",
        "calculated_precip",
        "wind_speed",
        "humidity",
        "cloud_cover",
        "dew_point",
        "weather_summary",
        "weather_type",
        "weather_station_id",
        "date",
        "et",
        "sunriseTime",
        "sunriseDate",
        "sunsetTime",
        "sunsetDate",
        "reading_type",
        "is_metric",
        "weather_type_url",
        "zoned_sunrise_time",
        "zoned_sunset_time",
    )
    TEMPERATURE_MIN_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_MAX_FIELD_NUMBER: _ClassVar[int]
    PRECIP_INTENSITY_FIELD_NUMBER: _ClassVar[int]
    PRECIP_PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    CALCULATED_PRECIP_FIELD_NUMBER: _ClassVar[int]
    WIND_SPEED_FIELD_NUMBER: _ClassVar[int]
    HUMIDITY_FIELD_NUMBER: _ClassVar[int]
    CLOUD_COVER_FIELD_NUMBER: _ClassVar[int]
    DEW_POINT_FIELD_NUMBER: _ClassVar[int]
    WEATHER_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    WEATHER_TYPE_FIELD_NUMBER: _ClassVar[int]
    WEATHER_STATION_ID_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    ET_FIELD_NUMBER: _ClassVar[int]
    SUNRISETIME_FIELD_NUMBER: _ClassVar[int]
    SUNRISEDATE_FIELD_NUMBER: _ClassVar[int]
    SUNSETTIME_FIELD_NUMBER: _ClassVar[int]
    SUNSETDATE_FIELD_NUMBER: _ClassVar[int]
    READING_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_METRIC_FIELD_NUMBER: _ClassVar[int]
    WEATHER_TYPE_URL_FIELD_NUMBER: _ClassVar[int]
    ZONED_SUNRISE_TIME_FIELD_NUMBER: _ClassVar[int]
    ZONED_SUNSET_TIME_FIELD_NUMBER: _ClassVar[int]
    temperature_min: int
    temperature_max: int
    precip_intensity: float
    precip_probability: float
    calculated_precip: float
    wind_speed: float
    humidity: float
    cloud_cover: float
    dew_point: float
    weather_summary: str
    weather_type: _weather_type_pb2.WeatherType
    weather_station_id: str
    date: _core_pb2.Date
    et: float
    sunriseTime: _core_pb2.Time
    sunriseDate: _core_pb2.Date
    sunsetTime: _core_pb2.Time
    sunsetDate: _core_pb2.Date
    reading_type: IReadingType
    is_metric: bool
    weather_type_url: str
    zoned_sunrise_time: _core_pb2.Time
    zoned_sunset_time: _core_pb2.Time
    def __init__(
        self,
        temperature_min: _Optional[int] = ...,
        temperature_max: _Optional[int] = ...,
        precip_intensity: _Optional[float] = ...,
        precip_probability: _Optional[float] = ...,
        calculated_precip: _Optional[float] = ...,
        wind_speed: _Optional[float] = ...,
        humidity: _Optional[float] = ...,
        cloud_cover: _Optional[float] = ...,
        dew_point: _Optional[float] = ...,
        weather_summary: _Optional[str] = ...,
        weather_type: _Optional[_Union[_weather_type_pb2.WeatherType, str]] = ...,
        weather_station_id: _Optional[str] = ...,
        date: _Optional[_Union[_core_pb2.Date, _Mapping]] = ...,
        et: _Optional[float] = ...,
        sunriseTime: _Optional[_Union[_core_pb2.Time, _Mapping]] = ...,
        sunriseDate: _Optional[_Union[_core_pb2.Date, _Mapping]] = ...,
        sunsetTime: _Optional[_Union[_core_pb2.Time, _Mapping]] = ...,
        sunsetDate: _Optional[_Union[_core_pb2.Date, _Mapping]] = ...,
        reading_type: _Optional[_Union[IReadingType, str]] = ...,
        is_metric: bool = ...,
        weather_type_url: _Optional[str] = ...,
        zoned_sunrise_time: _Optional[_Union[_core_pb2.Time, _Mapping]] = ...,
        zoned_sunset_time: _Optional[_Union[_core_pb2.Time, _Mapping]] = ...,
    ) -> None: ...

class WeatherNormal(_message.Message):
    __slots__ = (
        "month",
        "max_temp",
        "min_temp",
        "avg_temp",
        "prcp",
        "station_id",
        "et",
    )
    MONTH_FIELD_NUMBER: _ClassVar[int]
    MAX_TEMP_FIELD_NUMBER: _ClassVar[int]
    MIN_TEMP_FIELD_NUMBER: _ClassVar[int]
    AVG_TEMP_FIELD_NUMBER: _ClassVar[int]
    PRCP_FIELD_NUMBER: _ClassVar[int]
    STATION_ID_FIELD_NUMBER: _ClassVar[int]
    ET_FIELD_NUMBER: _ClassVar[int]
    month: int
    max_temp: float
    min_temp: float
    avg_temp: float
    prcp: float
    station_id: str
    et: float
    def __init__(
        self,
        month: _Optional[int] = ...,
        max_temp: _Optional[float] = ...,
        min_temp: _Optional[float] = ...,
        avg_temp: _Optional[float] = ...,
        prcp: _Optional[float] = ...,
        station_id: _Optional[str] = ...,
        et: _Optional[float] = ...,
    ) -> None: ...
