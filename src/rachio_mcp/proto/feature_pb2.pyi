import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Feature(_message.Message):
    __slots__ = ("id", "name", "group", "expiration", "created", "updated")
    class FeatureGroup(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FLOW: _ClassVar[Feature.FeatureGroup]
        WEATHER_INTELLIGENCE: _ClassVar[Feature.FeatureGroup]
        YARD_MAPPER: _ClassVar[Feature.FeatureGroup]
        MUNI_INSIGHTS: _ClassVar[Feature.FeatureGroup]
        PRO: _ClassVar[Feature.FeatureGroup]
        GROWTH: _ClassVar[Feature.FeatureGroup]
        YARD_CARE: _ClassVar[Feature.FeatureGroup]
        FIRMWARE: _ClassVar[Feature.FeatureGroup]
        SCHEDULE: _ClassVar[Feature.FeatureGroup]
        INTEGRATION: _ClassVar[Feature.FeatureGroup]

    FLOW: Feature.FeatureGroup
    WEATHER_INTELLIGENCE: Feature.FeatureGroup
    YARD_MAPPER: Feature.FeatureGroup
    MUNI_INSIGHTS: Feature.FeatureGroup
    PRO: Feature.FeatureGroup
    GROWTH: Feature.FeatureGroup
    YARD_CARE: Feature.FeatureGroup
    FIRMWARE: Feature.FeatureGroup
    SCHEDULE: Feature.FeatureGroup
    INTEGRATION: Feature.FeatureGroup
    class FeatureName(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACTUAL_USAGE_DETECTION: _ClassVar[Feature.FeatureName]
        LEAK_DETECTION: _ClassVar[Feature.FeatureName]
        AUTO_SHUTOFF: _ClassVar[Feature.FeatureName]
        WEATHER_INTELLIGENCE_PLUS: _ClassVar[Feature.FeatureName]
        IDLE_FLOW_DETECTION: _ClassVar[Feature.FeatureName]
        YARD_MAP: _ClassVar[Feature.FeatureName]
        SEGMENTS: _ClassVar[Feature.FeatureName]
        CALIBRATION_V2: _ClassVar[Feature.FeatureName]
        PRO_MAP: _ClassVar[Feature.FeatureName]
        YARDS_LIKE_MINE: _ClassVar[Feature.FeatureName]
        YARD_CARE_UI: _ClassVar[Feature.FeatureName]
        YARDCARE_DASHBOARD_WIDGET: _ClassVar[Feature.FeatureName]
        YARDCARE_QUICK_RUN_ALERT: _ClassVar[Feature.FeatureName]
        HOMEKIT: _ClassVar[Feature.FeatureName]
        LORA: _ClassVar[Feature.FeatureName]
        PGG_LED: _ClassVar[Feature.FeatureName]
        FLEX_DAILY_SCHEDULE: _ClassVar[Feature.FeatureName]
        FLEX_MONTHLY_SCHEDULE: _ClassVar[Feature.FeatureName]
        FIXED_SCHEDULE: _ClassVar[Feature.FeatureName]
        WIRELESS_FLOW_SENSOR: _ClassVar[Feature.FeatureName]
        GENERATION_HOMEKIT: _ClassVar[Feature.FeatureName]
        THRIVE_UI: _ClassVar[Feature.FeatureName]
        THRIVE_IN_APP_PURCHASE: _ClassVar[Feature.FeatureName]
        WATER_PARK: _ClassVar[Feature.FeatureName]
        ADAPTIVE_SCHEDULING: _ClassVar[Feature.FeatureName]
        KUSTOMER_SUPPORT: _ClassVar[Feature.FeatureName]
        AMPERAGE_MONITORING: _ClassVar[Feature.FeatureName]
        WEATHER_ADJUST: _ClassVar[Feature.FeatureName]

    ACTUAL_USAGE_DETECTION: Feature.FeatureName
    LEAK_DETECTION: Feature.FeatureName
    AUTO_SHUTOFF: Feature.FeatureName
    WEATHER_INTELLIGENCE_PLUS: Feature.FeatureName
    IDLE_FLOW_DETECTION: Feature.FeatureName
    YARD_MAP: Feature.FeatureName
    SEGMENTS: Feature.FeatureName
    CALIBRATION_V2: Feature.FeatureName
    PRO_MAP: Feature.FeatureName
    YARDS_LIKE_MINE: Feature.FeatureName
    YARD_CARE_UI: Feature.FeatureName
    YARDCARE_DASHBOARD_WIDGET: Feature.FeatureName
    YARDCARE_QUICK_RUN_ALERT: Feature.FeatureName
    HOMEKIT: Feature.FeatureName
    LORA: Feature.FeatureName
    PGG_LED: Feature.FeatureName
    FLEX_DAILY_SCHEDULE: Feature.FeatureName
    FLEX_MONTHLY_SCHEDULE: Feature.FeatureName
    FIXED_SCHEDULE: Feature.FeatureName
    WIRELESS_FLOW_SENSOR: Feature.FeatureName
    GENERATION_HOMEKIT: Feature.FeatureName
    THRIVE_UI: Feature.FeatureName
    THRIVE_IN_APP_PURCHASE: Feature.FeatureName
    WATER_PARK: Feature.FeatureName
    ADAPTIVE_SCHEDULING: Feature.FeatureName
    KUSTOMER_SUPPORT: Feature.FeatureName
    AMPERAGE_MONITORING: Feature.FeatureName
    WEATHER_ADJUST: Feature.FeatureName
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: Feature.FeatureName
    group: Feature.FeatureGroup
    expiration: _timestamp_pb2.Timestamp
    created: _timestamp_pb2.Timestamp
    updated: _timestamp_pb2.Timestamp
    def __init__(
        self,
        id: _Optional[str] = ...,
        name: _Optional[_Union[Feature.FeatureName, str]] = ...,
        group: _Optional[_Union[Feature.FeatureGroup, str]] = ...,
        expiration: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        created: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        updated: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
    ) -> None: ...
