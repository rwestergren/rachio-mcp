import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WireStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GOOD: _ClassVar[WireStatus]
    OPEN_LINE: _ClassVar[WireStatus]
    UNDER_CURRENT: _ClassVar[WireStatus]
    CHECK_LOW: _ClassVar[WireStatus]
    CHECK_HIGH: _ClassVar[WireStatus]
    OVER_CURRENT: _ClassVar[WireStatus]
GOOD: WireStatus
OPEN_LINE: WireStatus
UNDER_CURRENT: WireStatus
CHECK_LOW: WireStatus
CHECK_HIGH: WireStatus
OVER_CURRENT: WireStatus

class ControllerState(_message.Message):
    __slots__ = ("device_id", "health", "state", "rain_delay_expiration", "correct_firmware", "correct_rain_delay", "correct_schedule", "current_running_zone", "current_running_schedule", "last_run", "next_run", "firmware_version", "rain_sensor_tripped", "rssi", "desired_state", "desired_rain_delay_expiration", "flex_nodes", "desired_settle_time", "flow_firmware_version", "desired_idle_leak_detection", "desired_idle_leak_time", "desired_light_bar_setting")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_STATE: _ClassVar[ControllerState.State]
        STANDBY: _ClassVar[ControllerState.State]
        IDLE: _ClassVar[ControllerState.State]
        DELAY: _ClassVar[ControllerState.State]
        PAUSED: _ClassVar[ControllerState.State]
        WATERING: _ClassVar[ControllerState.State]
        UNBORN: _ClassVar[ControllerState.State]
        STARTUP: _ClassVar[ControllerState.State]
        UNKNOWN: _ClassVar[ControllerState.State]
        OFFLINE: _ClassVar[ControllerState.State]
        EXTENDED_OFFLINE: _ClassVar[ControllerState.State]
        PROVISIONING: _ClassVar[ControllerState.State]
    NO_STATE: ControllerState.State
    STANDBY: ControllerState.State
    IDLE: ControllerState.State
    DELAY: ControllerState.State
    PAUSED: ControllerState.State
    WATERING: ControllerState.State
    UNBORN: ControllerState.State
    STARTUP: ControllerState.State
    UNKNOWN: ControllerState.State
    OFFLINE: ControllerState.State
    EXTENDED_OFFLINE: ControllerState.State
    PROVISIONING: ControllerState.State
    class DesiredState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DESIRED_ACTIVE: _ClassVar[ControllerState.DesiredState]
        DESIRED_STANDBY: _ClassVar[ControllerState.DesiredState]
    DESIRED_ACTIVE: ControllerState.DesiredState
    DESIRED_STANDBY: ControllerState.DesiredState
    class Health(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_HEALTH: _ClassVar[ControllerState.Health]
        GOOD: _ClassVar[ControllerState.Health]
        WARNING: _ClassVar[ControllerState.Health]
        ERROR: _ClassVar[ControllerState.Health]
    NO_HEALTH: ControllerState.Health
    GOOD: ControllerState.Health
    WARNING: ControllerState.Health
    ERROR: ControllerState.Health
    class LightBarSetting(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ONE_HUNDRED_PERCENT: _ClassVar[ControllerState.LightBarSetting]
        OFF: _ClassVar[ControllerState.LightBarSetting]
        TWENTY_FIVE_PERCENT: _ClassVar[ControllerState.LightBarSetting]
    ONE_HUNDRED_PERCENT: ControllerState.LightBarSetting
    OFF: ControllerState.LightBarSetting
    TWENTY_FIVE_PERCENT: ControllerState.LightBarSetting
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    HEALTH_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    RAIN_DELAY_EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    CORRECT_FIRMWARE_FIELD_NUMBER: _ClassVar[int]
    CORRECT_RAIN_DELAY_FIELD_NUMBER: _ClassVar[int]
    CORRECT_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_RUNNING_ZONE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_RUNNING_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    LAST_RUN_FIELD_NUMBER: _ClassVar[int]
    NEXT_RUN_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    RAIN_SENSOR_TRIPPED_FIELD_NUMBER: _ClassVar[int]
    RSSI_FIELD_NUMBER: _ClassVar[int]
    DESIRED_STATE_FIELD_NUMBER: _ClassVar[int]
    DESIRED_RAIN_DELAY_EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    FLEX_NODES_FIELD_NUMBER: _ClassVar[int]
    DESIRED_SETTLE_TIME_FIELD_NUMBER: _ClassVar[int]
    FLOW_FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    DESIRED_IDLE_LEAK_DETECTION_FIELD_NUMBER: _ClassVar[int]
    DESIRED_IDLE_LEAK_TIME_FIELD_NUMBER: _ClassVar[int]
    DESIRED_LIGHT_BAR_SETTING_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    health: ControllerState.Health
    state: ControllerState.State
    rain_delay_expiration: _timestamp_pb2.Timestamp
    correct_firmware: bool
    correct_rain_delay: bool
    correct_schedule: bool
    current_running_zone: ZoneRun
    current_running_schedule: ImmediateScheduleRun
    last_run: _timestamp_pb2.Timestamp
    next_run: _timestamp_pb2.Timestamp
    firmware_version: str
    rain_sensor_tripped: bool
    rssi: int
    desired_state: ControllerState.DesiredState
    desired_rain_delay_expiration: _timestamp_pb2.Timestamp
    flex_nodes: _containers.RepeatedCompositeFieldContainer[FlexNodeState]
    desired_settle_time: int
    flow_firmware_version: str
    desired_idle_leak_detection: bool
    desired_idle_leak_time: int
    desired_light_bar_setting: ControllerState.LightBarSetting
    def __init__(self, device_id: _Optional[str] = ..., health: _Optional[_Union[ControllerState.Health, str]] = ..., state: _Optional[_Union[ControllerState.State, str]] = ..., rain_delay_expiration: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., correct_firmware: bool = ..., correct_rain_delay: bool = ..., correct_schedule: bool = ..., current_running_zone: _Optional[_Union[ZoneRun, _Mapping]] = ..., current_running_schedule: _Optional[_Union[ImmediateScheduleRun, _Mapping]] = ..., last_run: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., next_run: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., firmware_version: _Optional[str] = ..., rain_sensor_tripped: bool = ..., rssi: _Optional[int] = ..., desired_state: _Optional[_Union[ControllerState.DesiredState, str]] = ..., desired_rain_delay_expiration: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., flex_nodes: _Optional[_Iterable[_Union[FlexNodeState, _Mapping]]] = ..., desired_settle_time: _Optional[int] = ..., flow_firmware_version: _Optional[str] = ..., desired_idle_leak_detection: bool = ..., desired_idle_leak_time: _Optional[int] = ..., desired_light_bar_setting: _Optional[_Union[ControllerState.LightBarSetting, str]] = ...) -> None: ...

class ImmediateScheduleRun(_message.Message):
    __slots__ = ("type", "schedule_id", "run")
    class ScheduleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SCHEDULED: _ClassVar[ImmediateScheduleRun.ScheduleType]
        MANUAL: _ClassVar[ImmediateScheduleRun.ScheduleType]
    SCHEDULED: ImmediateScheduleRun.ScheduleType
    MANUAL: ImmediateScheduleRun.ScheduleType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_ID_FIELD_NUMBER: _ClassVar[int]
    RUN_FIELD_NUMBER: _ClassVar[int]
    type: ImmediateScheduleRun.ScheduleType
    schedule_id: str
    run: _containers.RepeatedCompositeFieldContainer[ZoneRun]
    def __init__(self, type: _Optional[_Union[ImmediateScheduleRun.ScheduleType, str]] = ..., schedule_id: _Optional[str] = ..., run: _Optional[_Iterable[_Union[ZoneRun, _Mapping]]] = ...) -> None: ...

class ZoneRun(_message.Message):
    __slots__ = ("index", "zone_number", "paused", "start", "end", "type")
    class RunType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        IRRIGATE: _ClassVar[ZoneRun.RunType]
        SOAK: _ClassVar[ZoneRun.RunType]
        PAUSE: _ClassVar[ZoneRun.RunType]
    IRRIGATE: ZoneRun.RunType
    SOAK: ZoneRun.RunType
    PAUSE: ZoneRun.RunType
    INDEX_FIELD_NUMBER: _ClassVar[int]
    ZONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    PAUSED_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    index: int
    zone_number: int
    paused: bool
    start: _timestamp_pb2.Timestamp
    end: _timestamp_pb2.Timestamp
    type: ZoneRun.RunType
    def __init__(self, index: _Optional[int] = ..., zone_number: _Optional[int] = ..., paused: bool = ..., start: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., type: _Optional[_Union[ZoneRun.RunType, str]] = ...) -> None: ...

class ZoneState(_message.Message):
    __slots__ = ("last_run", "next_run", "health", "last_run_start_current", "last_run_end_current", "last_current_reading_milliamps", "last_run_end_time", "wire_status")
    class Health(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        GOOD: _ClassVar[ZoneState.Health]
        WARNING: _ClassVar[ZoneState.Health]
        ERROR: _ClassVar[ZoneState.Health]
        OPEN_LINE: _ClassVar[ZoneState.Health]
        OVER_CURRENT: _ClassVar[ZoneState.Health]
        UNDER_CURRENT: _ClassVar[ZoneState.Health]
        CHECK: _ClassVar[ZoneState.Health]
    GOOD: ZoneState.Health
    WARNING: ZoneState.Health
    ERROR: ZoneState.Health
    OPEN_LINE: ZoneState.Health
    OVER_CURRENT: ZoneState.Health
    UNDER_CURRENT: ZoneState.Health
    CHECK: ZoneState.Health
    LAST_RUN_FIELD_NUMBER: _ClassVar[int]
    NEXT_RUN_FIELD_NUMBER: _ClassVar[int]
    HEALTH_FIELD_NUMBER: _ClassVar[int]
    LAST_RUN_START_CURRENT_FIELD_NUMBER: _ClassVar[int]
    LAST_RUN_END_CURRENT_FIELD_NUMBER: _ClassVar[int]
    LAST_CURRENT_READING_MILLIAMPS_FIELD_NUMBER: _ClassVar[int]
    LAST_RUN_END_TIME_FIELD_NUMBER: _ClassVar[int]
    WIRE_STATUS_FIELD_NUMBER: _ClassVar[int]
    last_run: _timestamp_pb2.Timestamp
    next_run: _timestamp_pb2.Timestamp
    health: ZoneState.Health
    last_run_start_current: int
    last_run_end_current: int
    last_current_reading_milliamps: _wrappers_pb2.Int32Value
    last_run_end_time: _timestamp_pb2.Timestamp
    wire_status: WireStatus
    def __init__(self, last_run: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., next_run: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., health: _Optional[_Union[ZoneState.Health, str]] = ..., last_run_start_current: _Optional[int] = ..., last_run_end_current: _Optional[int] = ..., last_current_reading_milliamps: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., last_run_end_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., wire_status: _Optional[_Union[WireStatus, str]] = ...) -> None: ...

class FlexNodeState(_message.Message):
    __slots__ = ("flex_type", "device_id", "flex_pin", "paired", "correct_config", "last_heartbeat", "battery_level", "link_quality", "link_quality_reading")
    class FlexNodeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FLOW: _ClassVar[FlexNodeState.FlexNodeType]
    FLOW: FlexNodeState.FlexNodeType
    class BatteryLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BATTERY_LOW: _ClassVar[FlexNodeState.BatteryLevel]
        BATTERY_GOOD: _ClassVar[FlexNodeState.BatteryLevel]
    BATTERY_LOW: FlexNodeState.BatteryLevel
    BATTERY_GOOD: FlexNodeState.BatteryLevel
    class LinkQuality(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LINK_POOR: _ClassVar[FlexNodeState.LinkQuality]
        LINK_GOOD: _ClassVar[FlexNodeState.LinkQuality]
        LINK_EXCELLENT: _ClassVar[FlexNodeState.LinkQuality]
    LINK_POOR: FlexNodeState.LinkQuality
    LINK_GOOD: FlexNodeState.LinkQuality
    LINK_EXCELLENT: FlexNodeState.LinkQuality
    FLEX_TYPE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    FLEX_PIN_FIELD_NUMBER: _ClassVar[int]
    PAIRED_FIELD_NUMBER: _ClassVar[int]
    CORRECT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    LAST_HEARTBEAT_FIELD_NUMBER: _ClassVar[int]
    BATTERY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    LINK_QUALITY_FIELD_NUMBER: _ClassVar[int]
    LINK_QUALITY_READING_FIELD_NUMBER: _ClassVar[int]
    flex_type: FlexNodeState.FlexNodeType
    device_id: str
    flex_pin: str
    paired: bool
    correct_config: bool
    last_heartbeat: _timestamp_pb2.Timestamp
    battery_level: FlexNodeState.BatteryLevel
    link_quality: FlexNodeState.LinkQuality
    link_quality_reading: float
    def __init__(self, flex_type: _Optional[_Union[FlexNodeState.FlexNodeType, str]] = ..., device_id: _Optional[str] = ..., flex_pin: _Optional[str] = ..., paired: bool = ..., correct_config: bool = ..., last_heartbeat: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., battery_level: _Optional[_Union[FlexNodeState.BatteryLevel, str]] = ..., link_quality: _Optional[_Union[FlexNodeState.LinkQuality, str]] = ..., link_quality_reading: _Optional[float] = ...) -> None: ...
