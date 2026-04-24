import datetime

import core_pb2 as _core_pb2
import location_summary_pb2 as _location_summary_pb2
import weather_reading_pb2 as _weather_reading_pb2
import weather_station_pb2 as _weather_station_pb2
import user_pb2 as _user_pb2
import location_pb2 as _location_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
import schedule_restriction_criteria_pb2 as _schedule_restriction_criteria_pb2
import location_restriction_pb2 as _location_restriction_pb2
import location_threshold_pb2 as _location_threshold_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
import schedule_run_pb2 as _schedule_run_pb2
import skip_sequence_pb2 as _skip_sequence_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Role(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MANAGER: _ClassVar[Role]
    QUICK_RUN: _ClassVar[Role]
    OWNER: _ClassVar[Role]
    TRANSFER_OWNERSHIP: _ClassVar[Role]
    YARDS_LIKE_MINE: _ClassVar[Role]

MANAGER: Role
QUICK_RUN: Role
OWNER: Role
TRANSFER_OWNERSHIP: Role
YARDS_LIKE_MINE: Role

class GetWeatherByLocationRequest(_message.Message):
    __slots__ = ("location_id", "start_date", "end_date")
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    location_id: str
    start_date: _core_pb2.Date
    end_date: _core_pb2.Date
    def __init__(
        self,
        location_id: _Optional[str] = ...,
        start_date: _Optional[_Union[_core_pb2.Date, _Mapping]] = ...,
        end_date: _Optional[_Union[_core_pb2.Date, _Mapping]] = ...,
    ) -> None: ...

class GetClosestWeatherStationsRequest(_message.Message):
    __slots__ = ("location_id", "allow_personal")
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    ALLOW_PERSONAL_FIELD_NUMBER: _ClassVar[int]
    location_id: str
    allow_personal: bool
    def __init__(
        self, location_id: _Optional[str] = ..., allow_personal: bool = ...
    ) -> None: ...

class GetClosestWeatherStationsResponse(_message.Message):
    __slots__ = ("stations",)
    STATIONS_FIELD_NUMBER: _ClassVar[int]
    stations: _containers.RepeatedCompositeFieldContainer[
        _weather_station_pb2.WeatherStation
    ]
    def __init__(
        self,
        stations: _Optional[
            _Iterable[_Union[_weather_station_pb2.WeatherStation, _Mapping]]
        ] = ...,
    ) -> None: ...

class GetWeatherResponse(_message.Message):
    __slots__ = ("weather_readings",)
    WEATHER_READINGS_FIELD_NUMBER: _ClassVar[int]
    weather_readings: _containers.RepeatedCompositeFieldContainer[
        _weather_reading_pb2.WeatherReading
    ]
    def __init__(
        self,
        weather_readings: _Optional[
            _Iterable[_Union[_weather_reading_pb2.WeatherReading, _Mapping]]
        ] = ...,
    ) -> None: ...

class GetLocationRequest(_message.Message):
    __slots__ = ("location_id", "include_state")
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_STATE_FIELD_NUMBER: _ClassVar[int]
    location_id: str
    include_state: bool
    def __init__(
        self, location_id: _Optional[str] = ..., include_state: bool = ...
    ) -> None: ...

class GetLocationResponse(_message.Message):
    __slots__ = ("location_summary",)
    LOCATION_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    location_summary: _location_summary_pb2.LocationSummary
    def __init__(
        self,
        location_summary: _Optional[
            _Union[_location_summary_pb2.LocationSummary, _Mapping]
        ] = ...,
    ) -> None: ...

class GetRestrictionRequest(_message.Message):
    __slots__ = ("location_id",)
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    location_id: str
    def __init__(self, location_id: _Optional[str] = ...) -> None: ...

class GetRestrictionResponse(_message.Message):
    __slots__ = ("restriction",)
    RESTRICTION_FIELD_NUMBER: _ClassVar[int]
    restriction: _location_restriction_pb2.LocationRestriction
    def __init__(
        self,
        restriction: _Optional[
            _Union[_location_restriction_pb2.LocationRestriction, _Mapping]
        ] = ...,
    ) -> None: ...

class UpdateRestrictionRequest(_message.Message):
    __slots__ = ("location_id", "schedule_restriction_criteria")
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_RESTRICTION_CRITERIA_FIELD_NUMBER: _ClassVar[int]
    location_id: str
    schedule_restriction_criteria: (
        _schedule_restriction_criteria_pb2.ScheduleRestrictionCriteria
    )
    def __init__(
        self,
        location_id: _Optional[str] = ...,
        schedule_restriction_criteria: _Optional[
            _Union[
                _schedule_restriction_criteria_pb2.ScheduleRestrictionCriteria, _Mapping
            ]
        ] = ...,
    ) -> None: ...

class UpdateRestrictionResponse(_message.Message):
    __slots__ = ("restriction",)
    RESTRICTION_FIELD_NUMBER: _ClassVar[int]
    restriction: _location_restriction_pb2.LocationRestriction
    def __init__(
        self,
        restriction: _Optional[
            _Union[_location_restriction_pb2.LocationRestriction, _Mapping]
        ] = ...,
    ) -> None: ...

class ClearRestrictionRequest(_message.Message):
    __slots__ = ("location_id",)
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    location_id: str
    def __init__(self, location_id: _Optional[str] = ...) -> None: ...

class ClearRestrictionResponse(_message.Message):
    __slots__ = ("cleared",)
    CLEARED_FIELD_NUMBER: _ClassVar[int]
    cleared: bool
    def __init__(self, cleared: bool = ...) -> None: ...

class ListLocationsRequest(_message.Message):
    __slots__ = ("include_state",)
    INCLUDE_STATE_FIELD_NUMBER: _ClassVar[int]
    include_state: bool
    def __init__(self, include_state: bool = ...) -> None: ...

class ListLocationsResponse(_message.Message):
    __slots__ = ("location_summary",)
    LOCATION_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    location_summary: _containers.RepeatedCompositeFieldContainer[
        _location_summary_pb2.LocationSummary
    ]
    def __init__(
        self,
        location_summary: _Optional[
            _Iterable[_Union[_location_summary_pb2.LocationSummary, _Mapping]]
        ] = ...,
    ) -> None: ...

class DeleteLocationRequest(_message.Message):
    __slots__ = ("location_id",)
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    location_id: str
    def __init__(self, location_id: _Optional[str] = ...) -> None: ...

class DeleteLocationResponse(_message.Message):
    __slots__ = ("deleted",)
    DELETED_FIELD_NUMBER: _ClassVar[int]
    deleted: bool
    def __init__(self, deleted: bool = ...) -> None: ...

class UpdateLocationRequest(_message.Message):
    __slots__ = (
        "location_id",
        "name",
        "device_ids_to_add",
        "device_ids_to_remove",
        "address",
        "geo_point",
        "photo_bytes",
        "include_all_weather_stations",
        "weather_station_id",
    )
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_IDS_TO_ADD_FIELD_NUMBER: _ClassVar[int]
    DEVICE_IDS_TO_REMOVE_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    GEO_POINT_FIELD_NUMBER: _ClassVar[int]
    PHOTO_BYTES_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ALL_WEATHER_STATIONS_FIELD_NUMBER: _ClassVar[int]
    WEATHER_STATION_ID_FIELD_NUMBER: _ClassVar[int]
    location_id: str
    name: _wrappers_pb2.StringValue
    device_ids_to_add: _containers.RepeatedScalarFieldContainer[str]
    device_ids_to_remove: _containers.RepeatedScalarFieldContainer[str]
    address: _core_pb2.Address
    geo_point: _core_pb2.GeoPoint
    photo_bytes: _wrappers_pb2.BytesValue
    include_all_weather_stations: _wrappers_pb2.BoolValue
    weather_station_id: _core_pb2.NullableString
    def __init__(
        self,
        location_id: _Optional[str] = ...,
        name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...,
        device_ids_to_add: _Optional[_Iterable[str]] = ...,
        device_ids_to_remove: _Optional[_Iterable[str]] = ...,
        address: _Optional[_Union[_core_pb2.Address, _Mapping]] = ...,
        geo_point: _Optional[_Union[_core_pb2.GeoPoint, _Mapping]] = ...,
        photo_bytes: _Optional[_Union[_wrappers_pb2.BytesValue, _Mapping]] = ...,
        include_all_weather_stations: _Optional[
            _Union[_wrappers_pb2.BoolValue, _Mapping]
        ] = ...,
        weather_station_id: _Optional[_Union[_core_pb2.NullableString, _Mapping]] = ...,
    ) -> None: ...

class UpdateLocationResponse(_message.Message):
    __slots__ = ("location",)
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    location: _location_pb2.Location
    def __init__(
        self, location: _Optional[_Union[_location_pb2.Location, _Mapping]] = ...
    ) -> None: ...

class UpdateLocationThresholdRequest(_message.Message):
    __slots__ = ("location_id", "location_threshold")
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    location_id: str
    location_threshold: _location_threshold_pb2.LocationThreshold
    def __init__(
        self,
        location_id: _Optional[str] = ...,
        location_threshold: _Optional[
            _Union[_location_threshold_pb2.LocationThreshold, _Mapping]
        ] = ...,
    ) -> None: ...

class UpdateLocationThresholdResponse(_message.Message):
    __slots__ = ("location",)
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    location: _location_pb2.Location
    def __init__(
        self, location: _Optional[_Union[_location_pb2.Location, _Mapping]] = ...
    ) -> None: ...

class GetAvailableThresholdValuesRequest(_message.Message):
    __slots__ = ("threshold_name",)
    THRESHOLD_NAME_FIELD_NUMBER: _ClassVar[int]
    threshold_name: _location_threshold_pb2.ThresholdName
    def __init__(
        self,
        threshold_name: _Optional[
            _Union[_location_threshold_pb2.ThresholdName, str]
        ] = ...,
    ) -> None: ...

class GetAvailableThresholdValuesResponse(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, value: _Optional[_Iterable[float]] = ...) -> None: ...

class CreateLocationRequest(_message.Message):
    __slots__ = (
        "name",
        "device_id",
        "address",
        "geo_point",
        "photo_bytes",
        "weather_station_id",
        "weather_station_latitude",
        "weather_station_longitude",
        "weather_station_has_precip",
    )
    NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    GEO_POINT_FIELD_NUMBER: _ClassVar[int]
    PHOTO_BYTES_FIELD_NUMBER: _ClassVar[int]
    WEATHER_STATION_ID_FIELD_NUMBER: _ClassVar[int]
    WEATHER_STATION_LATITUDE_FIELD_NUMBER: _ClassVar[int]
    WEATHER_STATION_LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    WEATHER_STATION_HAS_PRECIP_FIELD_NUMBER: _ClassVar[int]
    name: str
    device_id: _containers.RepeatedScalarFieldContainer[str]
    address: _core_pb2.Address
    geo_point: _core_pb2.GeoPoint
    photo_bytes: _wrappers_pb2.BytesValue
    weather_station_id: str
    weather_station_latitude: _wrappers_pb2.DoubleValue
    weather_station_longitude: _wrappers_pb2.DoubleValue
    weather_station_has_precip: _wrappers_pb2.BoolValue
    def __init__(
        self,
        name: _Optional[str] = ...,
        device_id: _Optional[_Iterable[str]] = ...,
        address: _Optional[_Union[_core_pb2.Address, _Mapping]] = ...,
        geo_point: _Optional[_Union[_core_pb2.GeoPoint, _Mapping]] = ...,
        photo_bytes: _Optional[_Union[_wrappers_pb2.BytesValue, _Mapping]] = ...,
        weather_station_id: _Optional[str] = ...,
        weather_station_latitude: _Optional[
            _Union[_wrappers_pb2.DoubleValue, _Mapping]
        ] = ...,
        weather_station_longitude: _Optional[
            _Union[_wrappers_pb2.DoubleValue, _Mapping]
        ] = ...,
        weather_station_has_precip: _Optional[
            _Union[_wrappers_pb2.BoolValue, _Mapping]
        ] = ...,
    ) -> None: ...

class CreateLocationResponse(_message.Message):
    __slots__ = ("location",)
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    location: _location_pb2.Location
    def __init__(
        self, location: _Optional[_Union[_location_pb2.Location, _Mapping]] = ...
    ) -> None: ...

class GetLocationPhotoRequest(_message.Message):
    __slots__ = ("location_id", "photo_id")
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    PHOTO_ID_FIELD_NUMBER: _ClassVar[int]
    location_id: str
    photo_id: str
    def __init__(
        self, location_id: _Optional[str] = ..., photo_id: _Optional[str] = ...
    ) -> None: ...

class GetLocationPhotoResponse(_message.Message):
    __slots__ = ("photo_bytes",)
    PHOTO_BYTES_FIELD_NUMBER: _ClassVar[int]
    photo_bytes: _wrappers_pb2.BytesValue
    def __init__(
        self, photo_bytes: _Optional[_Union[_wrappers_pb2.BytesValue, _Mapping]] = ...
    ) -> None: ...

class ShareLocationWithEmailRequest(_message.Message):
    __slots__ = ("location_id", "role", "email_address")
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    location_id: str
    role: Role
    email_address: str
    def __init__(
        self,
        location_id: _Optional[str] = ...,
        role: _Optional[_Union[Role, str]] = ...,
        email_address: _Optional[str] = ...,
    ) -> None: ...

class ShareLocationWithEmailResponse(_message.Message):
    __slots__ = ("shared_location", "message", "user_exists")
    SHARED_LOCATION_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    USER_EXISTS_FIELD_NUMBER: _ClassVar[int]
    shared_location: SharedLocation
    message: str
    user_exists: bool
    def __init__(
        self,
        shared_location: _Optional[_Union[SharedLocation, _Mapping]] = ...,
        message: _Optional[str] = ...,
        user_exists: bool = ...,
    ) -> None: ...

class AskForYLMPhotoPermissionsRequest(_message.Message):
    __slots__ = ("location_id", "expires")
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_FIELD_NUMBER: _ClassVar[int]
    location_id: str
    expires: _timestamp_pb2.Timestamp
    def __init__(
        self,
        location_id: _Optional[str] = ...,
        expires: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
    ) -> None: ...

class AskForYLMPhotoPermissionsResponse(_message.Message):
    __slots__ = ("shared_location_grant",)
    SHARED_LOCATION_GRANT_FIELD_NUMBER: _ClassVar[int]
    shared_location_grant: SharedLocationGrant
    def __init__(
        self,
        shared_location_grant: _Optional[_Union[SharedLocationGrant, _Mapping]] = ...,
    ) -> None: ...

class ShareLocationQRRequest(_message.Message):
    __slots__ = ("location_id", "expires", "email_address")
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    location_id: str
    expires: _timestamp_pb2.Timestamp
    email_address: str
    def __init__(
        self,
        location_id: _Optional[str] = ...,
        expires: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        email_address: _Optional[str] = ...,
    ) -> None: ...

class ShareLocationQRResponse(_message.Message):
    __slots__ = ("shared_location_grant",)
    SHARED_LOCATION_GRANT_FIELD_NUMBER: _ClassVar[int]
    shared_location_grant: SharedLocationGrant
    def __init__(
        self,
        shared_location_grant: _Optional[_Union[SharedLocationGrant, _Mapping]] = ...,
    ) -> None: ...

class AcceptSharedLocationRequest(_message.Message):
    __slots__ = ("code",)
    CODE_FIELD_NUMBER: _ClassVar[int]
    code: str
    def __init__(self, code: _Optional[str] = ...) -> None: ...

class AcceptSharedLocationResponse(_message.Message):
    __slots__ = ("shared_location",)
    SHARED_LOCATION_FIELD_NUMBER: _ClassVar[int]
    shared_location: SharedLocation
    def __init__(
        self, shared_location: _Optional[_Union[SharedLocation, _Mapping]] = ...
    ) -> None: ...

class ViewSharedLocationsRequest(_message.Message):
    __slots__ = ("location_id",)
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    location_id: str
    def __init__(self, location_id: _Optional[str] = ...) -> None: ...

class ViewSharedLocationsResponse(_message.Message):
    __slots__ = ("shared_locations",)
    SHARED_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    shared_locations: _containers.RepeatedCompositeFieldContainer[SharedLocation]
    def __init__(
        self,
        shared_locations: _Optional[_Iterable[_Union[SharedLocation, _Mapping]]] = ...,
    ) -> None: ...

class ViewSharedLocationGrantsRequest(_message.Message):
    __slots__ = ("include_pending", "location_id")
    INCLUDE_PENDING_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    include_pending: bool
    location_id: str
    def __init__(
        self, include_pending: bool = ..., location_id: _Optional[str] = ...
    ) -> None: ...

class ViewSharedLocationGrantsResponse(_message.Message):
    __slots__ = ("shared_location_grants",)
    SHARED_LOCATION_GRANTS_FIELD_NUMBER: _ClassVar[int]
    shared_location_grants: _containers.RepeatedCompositeFieldContainer[
        SharedLocationGrant
    ]
    def __init__(
        self,
        shared_location_grants: _Optional[
            _Iterable[_Union[SharedLocationGrant, _Mapping]]
        ] = ...,
    ) -> None: ...

class DeleteSharedLocationRequest(_message.Message):
    __slots__ = ("location_id", "account_shared_with")
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_SHARED_WITH_FIELD_NUMBER: _ClassVar[int]
    location_id: str
    account_shared_with: str
    def __init__(
        self,
        location_id: _Optional[str] = ...,
        account_shared_with: _Optional[str] = ...,
    ) -> None: ...

class DeleteSharedLocationResponse(_message.Message):
    __slots__ = ("deleted",)
    DELETED_FIELD_NUMBER: _ClassVar[int]
    deleted: bool
    def __init__(self, deleted: bool = ...) -> None: ...

class DeleteSharedLocationGrantRequest(_message.Message):
    __slots__ = ("code",)
    CODE_FIELD_NUMBER: _ClassVar[int]
    code: str
    def __init__(self, code: _Optional[str] = ...) -> None: ...

class DeleteSharedLocationGrantResponse(_message.Message):
    __slots__ = ("deleted",)
    DELETED_FIELD_NUMBER: _ClassVar[int]
    deleted: bool
    def __init__(self, deleted: bool = ...) -> None: ...

class UpdateLocationFavoriteRequest(_message.Message):
    __slots__ = ("location_id", "favorited")
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    FAVORITED_FIELD_NUMBER: _ClassVar[int]
    location_id: str
    favorited: bool
    def __init__(
        self, location_id: _Optional[str] = ..., favorited: bool = ...
    ) -> None: ...

class UpdateLocationFavoriteResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SharedLocation(_message.Message):
    __slots__ = ("user", "location_id", "role", "accepted_date")
    USER_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_DATE_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    location_id: str
    role: Role
    accepted_date: _timestamp_pb2.Timestamp
    def __init__(
        self,
        user: _Optional[_Union[_user_pb2.User, _Mapping]] = ...,
        location_id: _Optional[str] = ...,
        role: _Optional[_Union[Role, str]] = ...,
        accepted_date: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
    ) -> None: ...

class SharedLocationGrant(_message.Message):
    __slots__ = ("location_id", "code", "role", "expires", "url", "email_address")
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    location_id: str
    code: str
    role: Role
    expires: _timestamp_pb2.Timestamp
    url: str
    email_address: str
    def __init__(
        self,
        location_id: _Optional[str] = ...,
        code: _Optional[str] = ...,
        role: _Optional[_Union[Role, str]] = ...,
        expires: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        url: _Optional[str] = ...,
        email_address: _Optional[str] = ...,
    ) -> None: ...

class GetLocationDayRequest(_message.Message):
    __slots__ = ("location_id", "date")
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    location_id: str
    date: _core_pb2.Date
    def __init__(
        self,
        location_id: _Optional[str] = ...,
        date: _Optional[_Union[_core_pb2.Date, _Mapping]] = ...,
    ) -> None: ...

class GetCalendarForTimeRangeRequest(_message.Message):
    __slots__ = ("location_id", "start_time", "end_time", "include_historical")
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_HISTORICAL_FIELD_NUMBER: _ClassVar[int]
    location_id: str
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    include_historical: bool
    def __init__(
        self,
        location_id: _Optional[str] = ...,
        start_time: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        end_time: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        include_historical: bool = ...,
    ) -> None: ...

class GetCalendarForTimeRangeResponse(_message.Message):
    __slots__ = ("watering_day",)
    WATERING_DAY_FIELD_NUMBER: _ClassVar[int]
    watering_day: _containers.RepeatedCompositeFieldContainer[_location_pb2.WateringDay]
    def __init__(
        self,
        watering_day: _Optional[
            _Iterable[_Union[_location_pb2.WateringDay, _Mapping]]
        ] = ...,
    ) -> None: ...

class GetLocationCalendarRequest(_message.Message):
    __slots__ = ("location_id", "start_time", "end_time")
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    location_id: str
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    def __init__(
        self,
        location_id: _Optional[str] = ...,
        start_time: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        end_time: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
    ) -> None: ...

class GetLocationCalendarResponse(_message.Message):
    __slots__ = ("location_id", "runs", "skips", "rain_delay_expiration")
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    RUNS_FIELD_NUMBER: _ClassVar[int]
    SKIPS_FIELD_NUMBER: _ClassVar[int]
    RAIN_DELAY_EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    location_id: str
    runs: _containers.RepeatedCompositeFieldContainer[_schedule_run_pb2.ScheduleRun]
    skips: _containers.RepeatedCompositeFieldContainer[_skip_sequence_pb2.SkipSequence]
    rain_delay_expiration: _timestamp_pb2.Timestamp
    def __init__(
        self,
        location_id: _Optional[str] = ...,
        runs: _Optional[
            _Iterable[_Union[_schedule_run_pb2.ScheduleRun, _Mapping]]
        ] = ...,
        skips: _Optional[
            _Iterable[_Union[_skip_sequence_pb2.SkipSequence, _Mapping]]
        ] = ...,
        rain_delay_expiration: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
    ) -> None: ...

class ValidateQRCodeRequest(_message.Message):
    __slots__ = ("location_id", "code")
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    location_id: str
    code: str
    def __init__(
        self, location_id: _Optional[str] = ..., code: _Optional[str] = ...
    ) -> None: ...

class ValidateQRCodeResponse(_message.Message):
    __slots__ = ("location_summary",)
    LOCATION_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    location_summary: _location_summary_pb2.LocationSummary
    def __init__(
        self,
        location_summary: _Optional[
            _Union[_location_summary_pb2.LocationSummary, _Mapping]
        ] = ...,
    ) -> None: ...

class ValidateYLMCodeRequest(_message.Message):
    __slots__ = ("location_id", "code")
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    location_id: str
    code: str
    def __init__(
        self, location_id: _Optional[str] = ..., code: _Optional[str] = ...
    ) -> None: ...

class ValidateYLMCodeResponse(_message.Message):
    __slots__ = ("location_summary",)
    LOCATION_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    location_summary: _location_summary_pb2.LocationSummary
    def __init__(
        self,
        location_summary: _Optional[
            _Union[_location_summary_pb2.LocationSummary, _Mapping]
        ] = ...,
    ) -> None: ...

class UpdateLocationWeatherStationRequest(_message.Message):
    __slots__ = ("location_id", "station_id")
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    STATION_ID_FIELD_NUMBER: _ClassVar[int]
    location_id: str
    station_id: str
    def __init__(
        self, location_id: _Optional[str] = ..., station_id: _Optional[str] = ...
    ) -> None: ...

class UpdateLocationWeatherStationResponse(_message.Message):
    __slots__ = ("virtualWeatherStation",)
    VIRTUALWEATHERSTATION_FIELD_NUMBER: _ClassVar[int]
    virtualWeatherStation: _weather_station_pb2.VirtualWeatherStation
    def __init__(
        self,
        virtualWeatherStation: _Optional[
            _Union[_weather_station_pb2.VirtualWeatherStation, _Mapping]
        ] = ...,
    ) -> None: ...

class GetYardAreaRequest(_message.Message):
    __slots__ = ("location_id",)
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    location_id: str
    def __init__(self, location_id: _Optional[str] = ...) -> None: ...

class GetYardAreaResponse(_message.Message):
    __slots__ = ("yard_area",)
    YARD_AREA_FIELD_NUMBER: _ClassVar[int]
    yard_area: float
    def __init__(self, yard_area: _Optional[float] = ...) -> None: ...

class DeleteLocationByIrrigationControllerSerialNumberRequest(_message.Message):
    __slots__ = ("serial_number",)
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    serial_number: str
    def __init__(self, serial_number: _Optional[str] = ...) -> None: ...

class DeleteLocationByIrrigationControllerSerialNumberResponse(_message.Message):
    __slots__ = ("deleted",)
    DELETED_FIELD_NUMBER: _ClassVar[int]
    deleted: bool
    def __init__(self, deleted: bool = ...) -> None: ...
