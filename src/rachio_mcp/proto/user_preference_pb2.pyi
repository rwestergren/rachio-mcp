from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PreferenceName(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN_NAME: _ClassVar[PreferenceName]
    DEVICE_OFFLINE_EMAIL: _ClassVar[PreferenceName]
    DEVICE_OFFLINE_PUSH: _ClassVar[PreferenceName]
    ZONE_FAULT_EMAIL: _ClassVar[PreferenceName]
    ZONE_FAULT_PUSH: _ClassVar[PreferenceName]
    RAIN_SENSOR_STATUS_PUSH: _ClassVar[PreferenceName]
    WEATHER_SKIP_PUSH: _ClassVar[PreferenceName]
    WEATHER_SKIP_EMAIL: _ClassVar[PreferenceName]
    SEASONAL_SHIFT_EMAIL: _ClassVar[PreferenceName]
    SEASONAL_SHIFT_PUSH: _ClassVar[PreferenceName]
    SCHEDULE_STATUS_PUSH: _ClassVar[PreferenceName]
    IS_METRIC: _ClassVar[PreferenceName]
    IS_TIME_USAGE: _ClassVar[PreferenceName]
    RECEIVE_EMAILS_FROM_SHARED_CONTROLLERS: _ClassVar[PreferenceName]
    RECEIVE_PUSH_FROM_SHARED_DEVICES: _ClassVar[PreferenceName]
    FLOW_MONITORING_EMAIL: _ClassVar[PreferenceName]
    FLOW_MONITORING_PUSH: _ClassVar[PreferenceName]
    YARD_PHOTO_UPDATE_PUSH: _ClassVar[PreferenceName]
    YARD_PHOTO_UPDATE_EMAIL: _ClassVar[PreferenceName]
    THRIVE_NOTIFICATION_PUSH: _ClassVar[PreferenceName]
    THRIVE_NOTIFICATION_EMAIL: _ClassVar[PreferenceName]
    WEATHER_STATION_EMAIL: _ClassVar[PreferenceName]
    AMPERAGE_MONITORING_EMAIL: _ClassVar[PreferenceName]
    BASE_STATION_WIFI_OFFLINE_PUSH: _ClassVar[PreferenceName]
    VALVE_DISCONNECTED_PUSH: _ClassVar[PreferenceName]
    VALVE_BATTERY_LOW_PUSH: _ClassVar[PreferenceName]
    PROGRAM_START_PUSH: _ClassVar[PreferenceName]
    PROGRAM_SKIP_PUSH: _ClassVar[PreferenceName]
    VALVE_NO_FLOW_PUSH: _ClassVar[PreferenceName]
    AIR_QUALITY_PUSH: _ClassVar[PreferenceName]
    BASE_STATION_CONNECTION_STATUS_PUSH: _ClassVar[PreferenceName]
    LIGHTING_CONTROLLER_CONNECTION_STATUS_PUSH: _ClassVar[PreferenceName]
    CLIMATE_MONITORING_TRIGGERED_PUSH: _ClassVar[PreferenceName]
    LIGHTING_CONTROLLER_OVER_TEMPERATURE_EMAIL: _ClassVar[PreferenceName]
    LIGHTING_CONTROLLER_OVER_WATTAGE_EMAIL: _ClassVar[PreferenceName]

UNKNOWN_NAME: PreferenceName
DEVICE_OFFLINE_EMAIL: PreferenceName
DEVICE_OFFLINE_PUSH: PreferenceName
ZONE_FAULT_EMAIL: PreferenceName
ZONE_FAULT_PUSH: PreferenceName
RAIN_SENSOR_STATUS_PUSH: PreferenceName
WEATHER_SKIP_PUSH: PreferenceName
WEATHER_SKIP_EMAIL: PreferenceName
SEASONAL_SHIFT_EMAIL: PreferenceName
SEASONAL_SHIFT_PUSH: PreferenceName
SCHEDULE_STATUS_PUSH: PreferenceName
IS_METRIC: PreferenceName
IS_TIME_USAGE: PreferenceName
RECEIVE_EMAILS_FROM_SHARED_CONTROLLERS: PreferenceName
RECEIVE_PUSH_FROM_SHARED_DEVICES: PreferenceName
FLOW_MONITORING_EMAIL: PreferenceName
FLOW_MONITORING_PUSH: PreferenceName
YARD_PHOTO_UPDATE_PUSH: PreferenceName
YARD_PHOTO_UPDATE_EMAIL: PreferenceName
THRIVE_NOTIFICATION_PUSH: PreferenceName
THRIVE_NOTIFICATION_EMAIL: PreferenceName
WEATHER_STATION_EMAIL: PreferenceName
AMPERAGE_MONITORING_EMAIL: PreferenceName
BASE_STATION_WIFI_OFFLINE_PUSH: PreferenceName
VALVE_DISCONNECTED_PUSH: PreferenceName
VALVE_BATTERY_LOW_PUSH: PreferenceName
PROGRAM_START_PUSH: PreferenceName
PROGRAM_SKIP_PUSH: PreferenceName
VALVE_NO_FLOW_PUSH: PreferenceName
AIR_QUALITY_PUSH: PreferenceName
BASE_STATION_CONNECTION_STATUS_PUSH: PreferenceName
LIGHTING_CONTROLLER_CONNECTION_STATUS_PUSH: PreferenceName
CLIMATE_MONITORING_TRIGGERED_PUSH: PreferenceName
LIGHTING_CONTROLLER_OVER_TEMPERATURE_EMAIL: PreferenceName
LIGHTING_CONTROLLER_OVER_WATTAGE_EMAIL: PreferenceName

class UserPreference(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: PreferenceName
    value: bool
    def __init__(
        self, name: _Optional[_Union[PreferenceName, str]] = ..., value: bool = ...
    ) -> None: ...
