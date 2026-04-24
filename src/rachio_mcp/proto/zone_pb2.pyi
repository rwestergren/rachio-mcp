import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
import alert_pb2 as _alert_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
import media_model_pb2 as _media_model_pb2
import irrigation_controller_pb2 as _irrigation_controller_pb2
import agronomic_data_model_pb2 as _agronomic_data_model_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ZoneDisabledReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ZONE_NOT_DISABLED: _ClassVar[ZoneDisabledReason]
    MANUAL: _ClassVar[ZoneDisabledReason]
    HIGH_FLOW: _ClassVar[ZoneDisabledReason]
    LOW_FLOW: _ClassVar[ZoneDisabledReason]
    HIGH_CURRENT: _ClassVar[ZoneDisabledReason]
    LOW_CURRENT: _ClassVar[ZoneDisabledReason]

class ZoneGroupType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FRONT_YARD: _ClassVar[ZoneGroupType]
    BACK_YARD: _ClassVar[ZoneGroupType]
    USER_DEFINED: _ClassVar[ZoneGroupType]

class ValveBrand(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GENERIC: _ClassVar[ValveBrand]
    ASCO_BERMAD_CLAVAL: _ClassVar[ValveBrand]
    CHAMPION: _ClassVar[ValveBrand]
    GREENLAWN: _ClassVar[ValveBrand]
    GRISWOLD: _ClassVar[ValveBrand]
    HARDIE_IRRITROL: _ClassVar[ValveBrand]
    HUNTER: _ClassVar[ValveBrand]
    IMPERIAL_ATTV: _ClassVar[ValveBrand]
    NELSON: _ClassVar[ValveBrand]
    ORBIT: _ClassVar[ValveBrand]
    RAINBIRD_A_SERIES_COIL: _ClassVar[ValveBrand]
    RAINBIRD_B_SERIES_COIL: _ClassVar[ValveBrand]
    RAINBIRD_DV_SERIES: _ClassVar[ValveBrand]
    SUPERIOR: _ClassVar[ValveBrand]
    TORO_ONE_INCH: _ClassVar[ValveBrand]
    TORO_THREE_QUARTER_INCH: _ClassVar[ValveBrand]
    WEATHERMATIC: _ClassVar[ValveBrand]

ZONE_NOT_DISABLED: ZoneDisabledReason
MANUAL: ZoneDisabledReason
HIGH_FLOW: ZoneDisabledReason
LOW_FLOW: ZoneDisabledReason
HIGH_CURRENT: ZoneDisabledReason
LOW_CURRENT: ZoneDisabledReason
FRONT_YARD: ZoneGroupType
BACK_YARD: ZoneGroupType
USER_DEFINED: ZoneGroupType
GENERIC: ValveBrand
ASCO_BERMAD_CLAVAL: ValveBrand
CHAMPION: ValveBrand
GREENLAWN: ValveBrand
GRISWOLD: ValveBrand
HARDIE_IRRITROL: ValveBrand
HUNTER: ValveBrand
IMPERIAL_ATTV: ValveBrand
NELSON: ValveBrand
ORBIT: ValveBrand
RAINBIRD_A_SERIES_COIL: ValveBrand
RAINBIRD_B_SERIES_COIL: ValveBrand
RAINBIRD_DV_SERIES: ValveBrand
SUPERIOR: ValveBrand
TORO_ONE_INCH: ValveBrand
TORO_THREE_QUARTER_INCH: ValveBrand
WEATHERMATIC: ValveBrand

class ZoneDetail(_message.Message):
    __slots__ = (
        "id",
        "enabled",
        "zone_number",
        "name",
        "created",
        "updated",
        "area",
        "deleted",
        "device_id",
        "available_water_capacity",
        "root_zone_depth",
        "efficiency",
        "flow_rate",
        "crop_coefficient",
        "managed_allowed_depletion",
        "soil_type",
        "crop_type",
        "nozzle_type",
        "exposure_type",
        "photo_id",
        "slope_type",
        "has_moisture_data",
        "soil_moisture_level_at_end_of_day_pct",
        "isMetric",
        "zone_disabled_reason",
        "disabled_timestamp",
        "alerts",
        "flow_metering_enabled",
        "flow_auto_shut_off_enabled",
        "flow_calibrated",
        "flow_high_threshold_pct",
        "flow_low_threshold_pct",
        "flow_baseline",
        "flow_calibrated_timestamp",
        "soil_moisture_level_amount",
        "flow_calibration_result",
        "flow_manual_calibration",
        "appMessageBanner",
        "group_id",
        "photos",
        "watering_efficiency",
        "dynamic_crop_coefficient_enabled",
        "dynamic_crop_coefficient",
        "valve_count",
        "valve_brand",
        "amperage_monitoring_enabled",
        "amperage_auto_shut_off_enabled",
        "baseline_current_milliamps",
        "high_current_threshold_pct",
        "low_current_threshold_pct",
        "perimeter_geojson",
        "nozzle_locations_geojson",
    )
    ID_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    ZONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    AREA_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_WATER_CAPACITY_FIELD_NUMBER: _ClassVar[int]
    ROOT_ZONE_DEPTH_FIELD_NUMBER: _ClassVar[int]
    EFFICIENCY_FIELD_NUMBER: _ClassVar[int]
    FLOW_RATE_FIELD_NUMBER: _ClassVar[int]
    CROP_COEFFICIENT_FIELD_NUMBER: _ClassVar[int]
    MANAGED_ALLOWED_DEPLETION_FIELD_NUMBER: _ClassVar[int]
    SOIL_TYPE_FIELD_NUMBER: _ClassVar[int]
    CROP_TYPE_FIELD_NUMBER: _ClassVar[int]
    NOZZLE_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXPOSURE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PHOTO_ID_FIELD_NUMBER: _ClassVar[int]
    SLOPE_TYPE_FIELD_NUMBER: _ClassVar[int]
    HAS_MOISTURE_DATA_FIELD_NUMBER: _ClassVar[int]
    SOIL_MOISTURE_LEVEL_AT_END_OF_DAY_PCT_FIELD_NUMBER: _ClassVar[int]
    ISMETRIC_FIELD_NUMBER: _ClassVar[int]
    ZONE_DISABLED_REASON_FIELD_NUMBER: _ClassVar[int]
    DISABLED_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ALERTS_FIELD_NUMBER: _ClassVar[int]
    FLOW_METERING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    FLOW_AUTO_SHUT_OFF_ENABLED_FIELD_NUMBER: _ClassVar[int]
    FLOW_CALIBRATED_FIELD_NUMBER: _ClassVar[int]
    FLOW_HIGH_THRESHOLD_PCT_FIELD_NUMBER: _ClassVar[int]
    FLOW_LOW_THRESHOLD_PCT_FIELD_NUMBER: _ClassVar[int]
    FLOW_BASELINE_FIELD_NUMBER: _ClassVar[int]
    FLOW_CALIBRATED_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SOIL_MOISTURE_LEVEL_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    FLOW_CALIBRATION_RESULT_FIELD_NUMBER: _ClassVar[int]
    FLOW_MANUAL_CALIBRATION_FIELD_NUMBER: _ClassVar[int]
    APPMESSAGEBANNER_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    PHOTOS_FIELD_NUMBER: _ClassVar[int]
    WATERING_EFFICIENCY_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_CROP_COEFFICIENT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_CROP_COEFFICIENT_FIELD_NUMBER: _ClassVar[int]
    VALVE_COUNT_FIELD_NUMBER: _ClassVar[int]
    VALVE_BRAND_FIELD_NUMBER: _ClassVar[int]
    AMPERAGE_MONITORING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    AMPERAGE_AUTO_SHUT_OFF_ENABLED_FIELD_NUMBER: _ClassVar[int]
    BASELINE_CURRENT_MILLIAMPS_FIELD_NUMBER: _ClassVar[int]
    HIGH_CURRENT_THRESHOLD_PCT_FIELD_NUMBER: _ClassVar[int]
    LOW_CURRENT_THRESHOLD_PCT_FIELD_NUMBER: _ClassVar[int]
    PERIMETER_GEOJSON_FIELD_NUMBER: _ClassVar[int]
    NOZZLE_LOCATIONS_GEOJSON_FIELD_NUMBER: _ClassVar[int]
    id: str
    enabled: bool
    zone_number: int
    name: str
    created: _timestamp_pb2.Timestamp
    updated: _timestamp_pb2.Timestamp
    area: float
    deleted: bool
    device_id: str
    available_water_capacity: float
    root_zone_depth: float
    efficiency: float
    flow_rate: float
    crop_coefficient: float
    managed_allowed_depletion: float
    soil_type: _irrigation_controller_pb2.SoilType
    crop_type: _irrigation_controller_pb2.CropType
    nozzle_type: _irrigation_controller_pb2.NozzleType
    exposure_type: _irrigation_controller_pb2.ExposureType
    photo_id: str
    slope_type: _irrigation_controller_pb2.SlopeType
    has_moisture_data: bool
    soil_moisture_level_at_end_of_day_pct: float
    isMetric: bool
    zone_disabled_reason: ZoneDisabledReason
    disabled_timestamp: _timestamp_pb2.Timestamp
    alerts: _containers.RepeatedCompositeFieldContainer[_alert_pb2.Alert]
    flow_metering_enabled: bool
    flow_auto_shut_off_enabled: bool
    flow_calibrated: bool
    flow_high_threshold_pct: _wrappers_pb2.DoubleValue
    flow_low_threshold_pct: _wrappers_pb2.DoubleValue
    flow_baseline: _wrappers_pb2.DoubleValue
    flow_calibrated_timestamp: _timestamp_pb2.Timestamp
    soil_moisture_level_amount: float
    flow_calibration_result: _irrigation_controller_pb2.FlowCalibrationResultWrapper
    flow_manual_calibration: bool
    appMessageBanner: _containers.RepeatedCompositeFieldContainer[
        _irrigation_controller_pb2.AppMessageBanner
    ]
    group_id: _wrappers_pb2.StringValue
    photos: _containers.RepeatedCompositeFieldContainer[_media_model_pb2.Photo]
    watering_efficiency: _agronomic_data_model_pb2.WateringEfficiencyWrapper
    dynamic_crop_coefficient_enabled: bool
    dynamic_crop_coefficient: float
    valve_count: int
    valve_brand: ValveBrand
    amperage_monitoring_enabled: bool
    amperage_auto_shut_off_enabled: bool
    baseline_current_milliamps: _wrappers_pb2.Int32Value
    high_current_threshold_pct: float
    low_current_threshold_pct: float
    perimeter_geojson: _wrappers_pb2.StringValue
    nozzle_locations_geojson: _wrappers_pb2.StringValue
    def __init__(
        self,
        id: _Optional[str] = ...,
        enabled: bool = ...,
        zone_number: _Optional[int] = ...,
        name: _Optional[str] = ...,
        created: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        updated: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        area: _Optional[float] = ...,
        deleted: bool = ...,
        device_id: _Optional[str] = ...,
        available_water_capacity: _Optional[float] = ...,
        root_zone_depth: _Optional[float] = ...,
        efficiency: _Optional[float] = ...,
        flow_rate: _Optional[float] = ...,
        crop_coefficient: _Optional[float] = ...,
        managed_allowed_depletion: _Optional[float] = ...,
        soil_type: _Optional[_Union[_irrigation_controller_pb2.SoilType, str]] = ...,
        crop_type: _Optional[_Union[_irrigation_controller_pb2.CropType, str]] = ...,
        nozzle_type: _Optional[
            _Union[_irrigation_controller_pb2.NozzleType, str]
        ] = ...,
        exposure_type: _Optional[
            _Union[_irrigation_controller_pb2.ExposureType, str]
        ] = ...,
        photo_id: _Optional[str] = ...,
        slope_type: _Optional[_Union[_irrigation_controller_pb2.SlopeType, str]] = ...,
        has_moisture_data: bool = ...,
        soil_moisture_level_at_end_of_day_pct: _Optional[float] = ...,
        isMetric: bool = ...,
        zone_disabled_reason: _Optional[_Union[ZoneDisabledReason, str]] = ...,
        disabled_timestamp: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        alerts: _Optional[_Iterable[_Union[_alert_pb2.Alert, _Mapping]]] = ...,
        flow_metering_enabled: bool = ...,
        flow_auto_shut_off_enabled: bool = ...,
        flow_calibrated: bool = ...,
        flow_high_threshold_pct: _Optional[
            _Union[_wrappers_pb2.DoubleValue, _Mapping]
        ] = ...,
        flow_low_threshold_pct: _Optional[
            _Union[_wrappers_pb2.DoubleValue, _Mapping]
        ] = ...,
        flow_baseline: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ...,
        flow_calibrated_timestamp: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        soil_moisture_level_amount: _Optional[float] = ...,
        flow_calibration_result: _Optional[
            _Union[_irrigation_controller_pb2.FlowCalibrationResultWrapper, _Mapping]
        ] = ...,
        flow_manual_calibration: bool = ...,
        appMessageBanner: _Optional[
            _Iterable[_Union[_irrigation_controller_pb2.AppMessageBanner, _Mapping]]
        ] = ...,
        group_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...,
        photos: _Optional[_Iterable[_Union[_media_model_pb2.Photo, _Mapping]]] = ...,
        watering_efficiency: _Optional[
            _Union[_agronomic_data_model_pb2.WateringEfficiencyWrapper, _Mapping]
        ] = ...,
        dynamic_crop_coefficient_enabled: bool = ...,
        dynamic_crop_coefficient: _Optional[float] = ...,
        valve_count: _Optional[int] = ...,
        valve_brand: _Optional[_Union[ValveBrand, str]] = ...,
        amperage_monitoring_enabled: bool = ...,
        amperage_auto_shut_off_enabled: bool = ...,
        baseline_current_milliamps: _Optional[
            _Union[_wrappers_pb2.Int32Value, _Mapping]
        ] = ...,
        high_current_threshold_pct: _Optional[float] = ...,
        low_current_threshold_pct: _Optional[float] = ...,
        perimeter_geojson: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...,
        nozzle_locations_geojson: _Optional[
            _Union[_wrappers_pb2.StringValue, _Mapping]
        ] = ...,
    ) -> None: ...

class ZoneGroup(_message.Message):
    __slots__ = (
        "id",
        "device_id",
        "type",
        "name",
        "description",
        "area",
        "activity_level",
        "yard_health",
        "perimeter",
        "zone_ids",
        "created",
        "updated",
    )
    ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    AREA_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    YARD_HEALTH_FIELD_NUMBER: _ClassVar[int]
    PERIMETER_FIELD_NUMBER: _ClassVar[int]
    ZONE_IDS_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    id: str
    device_id: str
    type: ZoneGroupType
    name: str
    description: _wrappers_pb2.StringValue
    area: _wrappers_pb2.DoubleValue
    activity_level: _irrigation_controller_pb2.ActivityLevelWrapper
    yard_health: _irrigation_controller_pb2.YardHealthWrapper
    perimeter: _wrappers_pb2.StringValue
    zone_ids: _containers.RepeatedScalarFieldContainer[str]
    created: _timestamp_pb2.Timestamp
    updated: _timestamp_pb2.Timestamp
    def __init__(
        self,
        id: _Optional[str] = ...,
        device_id: _Optional[str] = ...,
        type: _Optional[_Union[ZoneGroupType, str]] = ...,
        name: _Optional[str] = ...,
        description: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...,
        area: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ...,
        activity_level: _Optional[
            _Union[_irrigation_controller_pb2.ActivityLevelWrapper, _Mapping]
        ] = ...,
        yard_health: _Optional[
            _Union[_irrigation_controller_pb2.YardHealthWrapper, _Mapping]
        ] = ...,
        perimeter: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...,
        zone_ids: _Optional[_Iterable[str]] = ...,
        created: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        updated: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
    ) -> None: ...

class ZoneGroupTypeWrapper(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: ZoneGroupType
    def __init__(self, value: _Optional[_Union[ZoneGroupType, str]] = ...) -> None: ...

class ValveBrandWrapper(_message.Message):
    __slots__ = ("brand",)
    BRAND_FIELD_NUMBER: _ClassVar[int]
    brand: ValveBrand
    def __init__(self, brand: _Optional[_Union[ValveBrand, str]] = ...) -> None: ...
