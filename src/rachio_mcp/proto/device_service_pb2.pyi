import datetime

import core_pb2 as _core_pb2
import device_pb2 as _device_pb2
import provision_pb2 as _provision_pb2
import irrigation_controller_pb2 as _irrigation_controller_pb2
import zone_pb2 as _zone_pb2
import weather_station_pb2 as _weather_station_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
import sensor_pb2 as _sensor_pb2
import controller_state_pb2 as _controller_state_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
import schedule_run_pb2 as _schedule_run_pb2
import skip_sequence_pb2 as _skip_sequence_pb2
import location_service_pb2 as _location_service_pb2
import location_pb2 as _location_pb2
import alert_pb2 as _alert_pb2
import feature_pb2 as _feature_pb2
import yard_like_mine_pb2 as _yard_like_mine_pb2
import schedule_criteria_pb2 as _schedule_criteria_pb2
import media_model_pb2 as _media_model_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetProvisionRequest(_message.Message):
    __slots__ = ("serial_number", "pin", "mac_address")
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    PIN_FIELD_NUMBER: _ClassVar[int]
    MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    serial_number: str
    pin: str
    mac_address: str
    def __init__(
        self,
        serial_number: _Optional[str] = ...,
        pin: _Optional[str] = ...,
        mac_address: _Optional[str] = ...,
    ) -> None: ...

class GetProvisionResponse(_message.Message):
    __slots__ = ("provision",)
    PROVISION_FIELD_NUMBER: _ClassVar[int]
    provision: _provision_pb2.Provision
    def __init__(
        self, provision: _Optional[_Union[_provision_pb2.Provision, _Mapping]] = ...
    ) -> None: ...

class GetProvisionedDeviceRequest(_message.Message):
    __slots__ = ("serial_number",)
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    serial_number: str
    def __init__(self, serial_number: _Optional[str] = ...) -> None: ...

class GetProvisionedDeviceResponse(_message.Message):
    __slots__ = ("device_id", "location_id", "owner_user_id")
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_USER_ID_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    location_id: str
    owner_user_id: str
    def __init__(
        self,
        device_id: _Optional[str] = ...,
        location_id: _Optional[str] = ...,
        owner_user_id: _Optional[str] = ...,
    ) -> None: ...

class CreateProvisionRequest(_message.Message):
    __slots__ = (
        "serial_number",
        "pin",
        "homekit_pin",
        "status",
        "manufacturer",
        "mac",
        "test_status",
        "test_result",
        "model",
        "firmware_version",
        "pro",
        "manufacturing_date",
        "weather_intelligence_plus",
        "qr_code_payload",
    )
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    PIN_FIELD_NUMBER: _ClassVar[int]
    HOMEKIT_PIN_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
    MAC_FIELD_NUMBER: _ClassVar[int]
    TEST_STATUS_FIELD_NUMBER: _ClassVar[int]
    TEST_RESULT_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    PRO_FIELD_NUMBER: _ClassVar[int]
    MANUFACTURING_DATE_FIELD_NUMBER: _ClassVar[int]
    WEATHER_INTELLIGENCE_PLUS_FIELD_NUMBER: _ClassVar[int]
    QR_CODE_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    serial_number: str
    pin: str
    homekit_pin: str
    status: _provision_pb2.ProvisionStatus
    manufacturer: _provision_pb2.Manufacturer
    mac: _wrappers_pb2.StringValue
    test_status: _wrappers_pb2.StringValue
    test_result: _wrappers_pb2.StringValue
    model: str
    firmware_version: _wrappers_pb2.StringValue
    pro: bool
    manufacturing_date: _timestamp_pb2.Timestamp
    weather_intelligence_plus: bool
    qr_code_payload: _wrappers_pb2.StringValue
    def __init__(
        self,
        serial_number: _Optional[str] = ...,
        pin: _Optional[str] = ...,
        homekit_pin: _Optional[str] = ...,
        status: _Optional[_Union[_provision_pb2.ProvisionStatus, str]] = ...,
        manufacturer: _Optional[_Union[_provision_pb2.Manufacturer, str]] = ...,
        mac: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...,
        test_status: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...,
        test_result: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...,
        model: _Optional[str] = ...,
        firmware_version: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...,
        pro: bool = ...,
        manufacturing_date: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        weather_intelligence_plus: bool = ...,
        qr_code_payload: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...,
    ) -> None: ...

class CreateProvisionResponse(_message.Message):
    __slots__ = ("provision",)
    PROVISION_FIELD_NUMBER: _ClassVar[int]
    provision: _provision_pb2.Provision
    def __init__(
        self, provision: _Optional[_Union[_provision_pb2.Provision, _Mapping]] = ...
    ) -> None: ...

class UpdateProvisionRequest(_message.Message):
    __slots__ = (
        "serial_number",
        "status",
        "mac",
        "test_status",
        "test_result",
        "firmware_version",
        "pro",
        "manufacturing_date",
        "model",
        "qr_code_payload",
        "last_known_firmware_version",
        "refurbished_date",
    )
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MAC_FIELD_NUMBER: _ClassVar[int]
    TEST_STATUS_FIELD_NUMBER: _ClassVar[int]
    TEST_RESULT_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    PRO_FIELD_NUMBER: _ClassVar[int]
    MANUFACTURING_DATE_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    QR_CODE_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    LAST_KNOWN_FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    REFURBISHED_DATE_FIELD_NUMBER: _ClassVar[int]
    serial_number: str
    status: _provision_pb2.ProvisionStatus
    mac: _wrappers_pb2.StringValue
    test_status: _wrappers_pb2.StringValue
    test_result: _wrappers_pb2.StringValue
    firmware_version: _wrappers_pb2.StringValue
    pro: _wrappers_pb2.BoolValue
    manufacturing_date: _timestamp_pb2.Timestamp
    model: _wrappers_pb2.StringValue
    qr_code_payload: _wrappers_pb2.StringValue
    last_known_firmware_version: _wrappers_pb2.StringValue
    refurbished_date: _timestamp_pb2.Timestamp
    def __init__(
        self,
        serial_number: _Optional[str] = ...,
        status: _Optional[_Union[_provision_pb2.ProvisionStatus, str]] = ...,
        mac: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...,
        test_status: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...,
        test_result: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...,
        firmware_version: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...,
        pro: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        manufacturing_date: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        model: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...,
        qr_code_payload: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...,
        last_known_firmware_version: _Optional[
            _Union[_wrappers_pb2.StringValue, _Mapping]
        ] = ...,
        refurbished_date: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
    ) -> None: ...

class UpdateProvisionResponse(_message.Message):
    __slots__ = ("provision",)
    PROVISION_FIELD_NUMBER: _ClassVar[int]
    provision: _provision_pb2.Provision
    def __init__(
        self, provision: _Optional[_Union[_provision_pb2.Provision, _Mapping]] = ...
    ) -> None: ...

class AddProvisionFeatureRequest(_message.Message):
    __slots__ = ("serial_number", "feature_id")
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    FEATURE_ID_FIELD_NUMBER: _ClassVar[int]
    serial_number: str
    feature_id: str
    def __init__(
        self, serial_number: _Optional[str] = ..., feature_id: _Optional[str] = ...
    ) -> None: ...

class AddProvisionFeatureResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateBasicZoneRequest(_message.Message):
    __slots__ = (
        "zone_id",
        "name",
        "enabled",
        "soil_type",
        "crop_type",
        "nozzle_type",
        "exposure_type",
        "photo_bytes",
        "slope_type",
        "group_id",
        "valve_count",
        "valve_brand",
        "amperage_monitoring_enabled",
        "amperage_auto_shut_off_enabled",
        "baseline_current_milliamps",
        "high_current_threshold_pct",
        "low_current_threshold_pct",
    )
    ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    SOIL_TYPE_FIELD_NUMBER: _ClassVar[int]
    CROP_TYPE_FIELD_NUMBER: _ClassVar[int]
    NOZZLE_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXPOSURE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PHOTO_BYTES_FIELD_NUMBER: _ClassVar[int]
    SLOPE_TYPE_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    VALVE_COUNT_FIELD_NUMBER: _ClassVar[int]
    VALVE_BRAND_FIELD_NUMBER: _ClassVar[int]
    AMPERAGE_MONITORING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    AMPERAGE_AUTO_SHUT_OFF_ENABLED_FIELD_NUMBER: _ClassVar[int]
    BASELINE_CURRENT_MILLIAMPS_FIELD_NUMBER: _ClassVar[int]
    HIGH_CURRENT_THRESHOLD_PCT_FIELD_NUMBER: _ClassVar[int]
    LOW_CURRENT_THRESHOLD_PCT_FIELD_NUMBER: _ClassVar[int]
    zone_id: str
    name: _wrappers_pb2.StringValue
    enabled: _wrappers_pb2.BoolValue
    soil_type: _irrigation_controller_pb2.SoilTypeWrapper
    crop_type: _irrigation_controller_pb2.CropTypeWrapper
    nozzle_type: _irrigation_controller_pb2.NozzleTypeWrapper
    exposure_type: _irrigation_controller_pb2.ExposureTypeWrapper
    photo_bytes: _wrappers_pb2.BytesValue
    slope_type: _irrigation_controller_pb2.SlopeTypeWrapper
    group_id: _wrappers_pb2.StringValue
    valve_count: _wrappers_pb2.Int32Value
    valve_brand: _zone_pb2.ValveBrandWrapper
    amperage_monitoring_enabled: _wrappers_pb2.BoolValue
    amperage_auto_shut_off_enabled: _wrappers_pb2.BoolValue
    baseline_current_milliamps: _wrappers_pb2.Int32Value
    high_current_threshold_pct: _wrappers_pb2.DoubleValue
    low_current_threshold_pct: _wrappers_pb2.DoubleValue
    def __init__(
        self,
        zone_id: _Optional[str] = ...,
        name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...,
        enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        soil_type: _Optional[
            _Union[_irrigation_controller_pb2.SoilTypeWrapper, _Mapping]
        ] = ...,
        crop_type: _Optional[
            _Union[_irrigation_controller_pb2.CropTypeWrapper, _Mapping]
        ] = ...,
        nozzle_type: _Optional[
            _Union[_irrigation_controller_pb2.NozzleTypeWrapper, _Mapping]
        ] = ...,
        exposure_type: _Optional[
            _Union[_irrigation_controller_pb2.ExposureTypeWrapper, _Mapping]
        ] = ...,
        photo_bytes: _Optional[_Union[_wrappers_pb2.BytesValue, _Mapping]] = ...,
        slope_type: _Optional[
            _Union[_irrigation_controller_pb2.SlopeTypeWrapper, _Mapping]
        ] = ...,
        group_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...,
        valve_count: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...,
        valve_brand: _Optional[_Union[_zone_pb2.ValveBrandWrapper, _Mapping]] = ...,
        amperage_monitoring_enabled: _Optional[
            _Union[_wrappers_pb2.BoolValue, _Mapping]
        ] = ...,
        amperage_auto_shut_off_enabled: _Optional[
            _Union[_wrappers_pb2.BoolValue, _Mapping]
        ] = ...,
        baseline_current_milliamps: _Optional[
            _Union[_wrappers_pb2.Int32Value, _Mapping]
        ] = ...,
        high_current_threshold_pct: _Optional[
            _Union[_wrappers_pb2.DoubleValue, _Mapping]
        ] = ...,
        low_current_threshold_pct: _Optional[
            _Union[_wrappers_pb2.DoubleValue, _Mapping]
        ] = ...,
    ) -> None: ...

class UpdateBasicZoneResponse(_message.Message):
    __slots__ = ("zone",)
    ZONE_FIELD_NUMBER: _ClassVar[int]
    zone: _zone_pb2.ZoneDetail
    def __init__(
        self, zone: _Optional[_Union[_zone_pb2.ZoneDetail, _Mapping]] = ...
    ) -> None: ...

class UpdatePhotoDetailsRequest(_message.Message):
    __slots__ = ("id", "share_permission_granted", "shared_primary")
    ID_FIELD_NUMBER: _ClassVar[int]
    SHARE_PERMISSION_GRANTED_FIELD_NUMBER: _ClassVar[int]
    SHARED_PRIMARY_FIELD_NUMBER: _ClassVar[int]
    id: str
    share_permission_granted: bool
    shared_primary: bool
    def __init__(
        self,
        id: _Optional[str] = ...,
        share_permission_granted: bool = ...,
        shared_primary: bool = ...,
    ) -> None: ...

class UpdateYLMPhotoDetailsRequest(_message.Message):
    __slots__ = (
        "id",
        "device_id",
        "code",
        "share_permission_granted",
        "shared_primary",
    )
    ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    SHARE_PERMISSION_GRANTED_FIELD_NUMBER: _ClassVar[int]
    SHARED_PRIMARY_FIELD_NUMBER: _ClassVar[int]
    id: str
    device_id: str
    code: str
    share_permission_granted: bool
    shared_primary: bool
    def __init__(
        self,
        id: _Optional[str] = ...,
        device_id: _Optional[str] = ...,
        code: _Optional[str] = ...,
        share_permission_granted: bool = ...,
        shared_primary: bool = ...,
    ) -> None: ...

class UpdatePhotoDetailsResponse(_message.Message):
    __slots__ = ("photo",)
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    photo: _media_model_pb2.Photo
    def __init__(
        self, photo: _Optional[_Union[_media_model_pb2.Photo, _Mapping]] = ...
    ) -> None: ...

class UpdateAdvancedZoneRequest(_message.Message):
    __slots__ = (
        "zone_id",
        "available_water_capacity",
        "root_zone_depth",
        "efficiency",
        "flow_rate",
        "crop_coefficient",
        "managed_allowed_depletion",
        "area",
        "customer_feedback_scale",
        "dynamic_crop_coefficient_enabled",
    )
    ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_WATER_CAPACITY_FIELD_NUMBER: _ClassVar[int]
    ROOT_ZONE_DEPTH_FIELD_NUMBER: _ClassVar[int]
    EFFICIENCY_FIELD_NUMBER: _ClassVar[int]
    FLOW_RATE_FIELD_NUMBER: _ClassVar[int]
    CROP_COEFFICIENT_FIELD_NUMBER: _ClassVar[int]
    MANAGED_ALLOWED_DEPLETION_FIELD_NUMBER: _ClassVar[int]
    AREA_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_FEEDBACK_SCALE_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_CROP_COEFFICIENT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    zone_id: str
    available_water_capacity: _wrappers_pb2.DoubleValue
    root_zone_depth: _wrappers_pb2.DoubleValue
    efficiency: _wrappers_pb2.DoubleValue
    flow_rate: _wrappers_pb2.DoubleValue
    crop_coefficient: _wrappers_pb2.DoubleValue
    managed_allowed_depletion: _wrappers_pb2.DoubleValue
    area: _wrappers_pb2.DoubleValue
    customer_feedback_scale: _wrappers_pb2.Int32Value
    dynamic_crop_coefficient_enabled: bool
    def __init__(
        self,
        zone_id: _Optional[str] = ...,
        available_water_capacity: _Optional[
            _Union[_wrappers_pb2.DoubleValue, _Mapping]
        ] = ...,
        root_zone_depth: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ...,
        efficiency: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ...,
        flow_rate: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ...,
        crop_coefficient: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ...,
        managed_allowed_depletion: _Optional[
            _Union[_wrappers_pb2.DoubleValue, _Mapping]
        ] = ...,
        area: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ...,
        customer_feedback_scale: _Optional[
            _Union[_wrappers_pb2.Int32Value, _Mapping]
        ] = ...,
        dynamic_crop_coefficient_enabled: bool = ...,
    ) -> None: ...

class UpdateAdvancedZoneResponse(_message.Message):
    __slots__ = ("zone",)
    ZONE_FIELD_NUMBER: _ClassVar[int]
    zone: _zone_pb2.ZoneDetail
    def __init__(
        self, zone: _Optional[_Union[_zone_pb2.ZoneDetail, _Mapping]] = ...
    ) -> None: ...

class ListZonesRequest(_message.Message):
    __slots__ = ("device_id", "include_extra_data", "include_moisture_data")
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_EXTRA_DATA_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_MOISTURE_DATA_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    include_extra_data: _wrappers_pb2.BoolValue
    include_moisture_data: _wrappers_pb2.BoolValue
    def __init__(
        self,
        device_id: _Optional[str] = ...,
        include_extra_data: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        include_moisture_data: _Optional[
            _Union[_wrappers_pb2.BoolValue, _Mapping]
        ] = ...,
    ) -> None: ...

class ListZonesResponse(_message.Message):
    __slots__ = ("zone_summary",)
    ZONE_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    zone_summary: _containers.RepeatedCompositeFieldContainer[ZoneSummary]
    def __init__(
        self, zone_summary: _Optional[_Iterable[_Union[ZoneSummary, _Mapping]]] = ...
    ) -> None: ...

class GetZoneDetailRequest(_message.Message):
    __slots__ = ("zone_id", "force_imperial")
    ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    FORCE_IMPERIAL_FIELD_NUMBER: _ClassVar[int]
    zone_id: str
    force_imperial: bool
    def __init__(
        self, zone_id: _Optional[str] = ..., force_imperial: bool = ...
    ) -> None: ...

class GetZoneDetailResponse(_message.Message):
    __slots__ = ("zone_summary",)
    ZONE_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    zone_summary: ZoneSummary
    def __init__(
        self, zone_summary: _Optional[_Union[ZoneSummary, _Mapping]] = ...
    ) -> None: ...

class ZoneSummary(_message.Message):
    __slots__ = ("zone_detail", "zone_state")
    ZONE_DETAIL_FIELD_NUMBER: _ClassVar[int]
    ZONE_STATE_FIELD_NUMBER: _ClassVar[int]
    zone_detail: _zone_pb2.ZoneDetail
    zone_state: _controller_state_pb2.ZoneState
    def __init__(
        self,
        zone_detail: _Optional[_Union[_zone_pb2.ZoneDetail, _Mapping]] = ...,
        zone_state: _Optional[_Union[_controller_state_pb2.ZoneState, _Mapping]] = ...,
    ) -> None: ...

class GetZonePhotoRequest(_message.Message):
    __slots__ = ("zone_id", "photo_id")
    ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    PHOTO_ID_FIELD_NUMBER: _ClassVar[int]
    zone_id: str
    photo_id: str
    def __init__(
        self, zone_id: _Optional[str] = ..., photo_id: _Optional[str] = ...
    ) -> None: ...

class GetZonePhotoResponse(_message.Message):
    __slots__ = ("photo_bytes",)
    PHOTO_BYTES_FIELD_NUMBER: _ClassVar[int]
    photo_bytes: _wrappers_pb2.BytesValue
    def __init__(
        self, photo_bytes: _Optional[_Union[_wrappers_pb2.BytesValue, _Mapping]] = ...
    ) -> None: ...

class AddZonePerimeterRequest(_message.Message):
    __slots__ = ("device_id", "zone_id", "zone_perimeter", "area")
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_PERIMETER_FIELD_NUMBER: _ClassVar[int]
    AREA_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    zone_id: str
    zone_perimeter: str
    area: float
    def __init__(
        self,
        device_id: _Optional[str] = ...,
        zone_id: _Optional[str] = ...,
        zone_perimeter: _Optional[str] = ...,
        area: _Optional[float] = ...,
    ) -> None: ...

class AddZonePerimeterResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AddZoneNozzlesRequest(_message.Message):
    __slots__ = ("device_id", "zone_id", "zone_nozzles")
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_NOZZLES_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    zone_id: str
    zone_nozzles: str
    def __init__(
        self,
        device_id: _Optional[str] = ...,
        zone_id: _Optional[str] = ...,
        zone_nozzles: _Optional[str] = ...,
    ) -> None: ...

class AddZoneNozzlesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetZonePerimeterRequest(_message.Message):
    __slots__ = ("device_id", "zone_id")
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    zone_id: str
    def __init__(
        self, device_id: _Optional[str] = ..., zone_id: _Optional[str] = ...
    ) -> None: ...

class GetZonePerimeterResponse(_message.Message):
    __slots__ = ("zone_perimeter",)
    ZONE_PERIMETER_FIELD_NUMBER: _ClassVar[int]
    zone_perimeter: str
    def __init__(self, zone_perimeter: _Optional[str] = ...) -> None: ...

class GetZoneNozzlesRequest(_message.Message):
    __slots__ = ("device_id", "zone_id")
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    zone_id: str
    def __init__(
        self, device_id: _Optional[str] = ..., zone_id: _Optional[str] = ...
    ) -> None: ...

class GetZoneNozzlesResponse(_message.Message):
    __slots__ = ("zone_nozzles",)
    ZONE_NOZZLES_FIELD_NUMBER: _ClassVar[int]
    zone_nozzles: str
    def __init__(self, zone_nozzles: _Optional[str] = ...) -> None: ...

class UpdateZonePerimeterRequest(_message.Message):
    __slots__ = ("device_id", "zone_id", "zone_perimeter", "area")
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_PERIMETER_FIELD_NUMBER: _ClassVar[int]
    AREA_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    zone_id: str
    zone_perimeter: str
    area: float
    def __init__(
        self,
        device_id: _Optional[str] = ...,
        zone_id: _Optional[str] = ...,
        zone_perimeter: _Optional[str] = ...,
        area: _Optional[float] = ...,
    ) -> None: ...

class UpdateZonePerimeterResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateZoneNozzlesRequest(_message.Message):
    __slots__ = ("device_id", "zone_id", "zone_nozzles")
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_NOZZLES_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    zone_id: str
    zone_nozzles: str
    def __init__(
        self,
        device_id: _Optional[str] = ...,
        zone_id: _Optional[str] = ...,
        zone_nozzles: _Optional[str] = ...,
    ) -> None: ...

class UpdateZoneNozzlesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TriggerZoneTestRequest(_message.Message):
    __slots__ = ("device_id",)
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    def __init__(self, device_id: _Optional[str] = ...) -> None: ...

class TriggerZoneTestResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetDeviceRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetDeviceResponse(_message.Message):
    __slots__ = ("device",)
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    device: _device_pb2.Device
    def __init__(
        self, device: _Optional[_Union[_device_pb2.Device, _Mapping]] = ...
    ) -> None: ...

class ListDevicesRequest(_message.Message):
    __slots__ = ("location_id", "owner_id")
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_ID_FIELD_NUMBER: _ClassVar[int]
    location_id: str
    owner_id: str
    def __init__(
        self, location_id: _Optional[str] = ..., owner_id: _Optional[str] = ...
    ) -> None: ...

class ListDevicesResponse(_message.Message):
    __slots__ = ("device",)
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    device: _containers.RepeatedCompositeFieldContainer[_device_pb2.Device]
    def __init__(
        self, device: _Optional[_Iterable[_Union[_device_pb2.Device, _Mapping]]] = ...
    ) -> None: ...

class GetDeviceDetailsRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetDeviceDetailsResponse(_message.Message):
    __slots__ = (
        "gen1_irrigation_controller",
        "gen2_irrigation_controller",
        "linked_sensor",
        "virtual_weather_station",
        "gen3_irrigation_controller",
        "wireless_flow_sensor",
        "virtual_irrigation_controller",
    )
    GEN1_IRRIGATION_CONTROLLER_FIELD_NUMBER: _ClassVar[int]
    GEN2_IRRIGATION_CONTROLLER_FIELD_NUMBER: _ClassVar[int]
    LINKED_SENSOR_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_WEATHER_STATION_FIELD_NUMBER: _ClassVar[int]
    GEN3_IRRIGATION_CONTROLLER_FIELD_NUMBER: _ClassVar[int]
    WIRELESS_FLOW_SENSOR_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_IRRIGATION_CONTROLLER_FIELD_NUMBER: _ClassVar[int]
    gen1_irrigation_controller: _irrigation_controller_pb2.Gen1IrrigationController
    gen2_irrigation_controller: _irrigation_controller_pb2.Gen2IrrigationController
    linked_sensor: _sensor_pb2.LinkedSensor
    virtual_weather_station: _weather_station_pb2.VirtualWeatherStation
    gen3_irrigation_controller: _irrigation_controller_pb2.Gen3IrrigationController
    wireless_flow_sensor: _sensor_pb2.WirelessFlowSensor
    virtual_irrigation_controller: (
        _irrigation_controller_pb2.VirtualIrrigationController
    )
    def __init__(
        self,
        gen1_irrigation_controller: _Optional[
            _Union[_irrigation_controller_pb2.Gen1IrrigationController, _Mapping]
        ] = ...,
        gen2_irrigation_controller: _Optional[
            _Union[_irrigation_controller_pb2.Gen2IrrigationController, _Mapping]
        ] = ...,
        linked_sensor: _Optional[_Union[_sensor_pb2.LinkedSensor, _Mapping]] = ...,
        virtual_weather_station: _Optional[
            _Union[_weather_station_pb2.VirtualWeatherStation, _Mapping]
        ] = ...,
        gen3_irrigation_controller: _Optional[
            _Union[_irrigation_controller_pb2.Gen3IrrigationController, _Mapping]
        ] = ...,
        wireless_flow_sensor: _Optional[
            _Union[_sensor_pb2.WirelessFlowSensor, _Mapping]
        ] = ...,
        virtual_irrigation_controller: _Optional[
            _Union[_irrigation_controller_pb2.VirtualIrrigationController, _Mapping]
        ] = ...,
    ) -> None: ...

class GetDeviceStateRequest(_message.Message):
    __slots__ = ("device_id",)
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    def __init__(self, device_id: _Optional[str] = ...) -> None: ...

class GetDeviceStateResponse(_message.Message):
    __slots__ = ("state",)
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: _controller_state_pb2.ControllerState
    def __init__(
        self,
        state: _Optional[_Union[_controller_state_pb2.ControllerState, _Mapping]] = ...,
    ) -> None: ...

class DeleteDeviceRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DeleteDeviceResponse(_message.Message):
    __slots__ = ("deleted",)
    DELETED_FIELD_NUMBER: _ClassVar[int]
    deleted: bool
    def __init__(self, deleted: bool = ...) -> None: ...

class GetNascentIrrigationControllerRequest(_message.Message):
    __slots__ = ("serial_number",)
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    serial_number: str
    def __init__(self, serial_number: _Optional[str] = ...) -> None: ...

class GetNascentIrrigationControllerResponse(_message.Message):
    __slots__ = ("nascent_irrigation_controller",)
    NASCENT_IRRIGATION_CONTROLLER_FIELD_NUMBER: _ClassVar[int]
    nascent_irrigation_controller: (
        _irrigation_controller_pb2.NascentIrrigationController
    )
    def __init__(
        self,
        nascent_irrigation_controller: _Optional[
            _Union[_irrigation_controller_pb2.NascentIrrigationController, _Mapping]
        ] = ...,
    ) -> None: ...

class GetNascentWirelessFlowSensorRequest(_message.Message):
    __slots__ = ("serial_number",)
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    serial_number: str
    def __init__(self, serial_number: _Optional[str] = ...) -> None: ...

class GetNascentWirelessFlowSensorResponse(_message.Message):
    __slots__ = ("nascent_wireless_flow_sensor",)
    NASCENT_WIRELESS_FLOW_SENSOR_FIELD_NUMBER: _ClassVar[int]
    nascent_wireless_flow_sensor: _sensor_pb2.NascentWirelessFlowSensor
    def __init__(
        self,
        nascent_wireless_flow_sensor: _Optional[
            _Union[_sensor_pb2.NascentWirelessFlowSensor, _Mapping]
        ] = ...,
    ) -> None: ...

class CreateGen1IrrigationControllerRequest(_message.Message):
    __slots__ = (
        "name",
        "geo_point",
        "location_id",
        "pin",
        "agent_id",
        "external_plan_id",
        "serial_number",
        "master_valve",
        "water_hammer",
        "wellpump_delay_active",
        "activation_code",
    )
    NAME_FIELD_NUMBER: _ClassVar[int]
    GEO_POINT_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    PIN_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    MASTER_VALVE_FIELD_NUMBER: _ClassVar[int]
    WATER_HAMMER_FIELD_NUMBER: _ClassVar[int]
    WELLPUMP_DELAY_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    ACTIVATION_CODE_FIELD_NUMBER: _ClassVar[int]
    name: str
    geo_point: _core_pb2.GeoPoint
    location_id: str
    pin: str
    agent_id: str
    external_plan_id: str
    serial_number: str
    master_valve: bool
    water_hammer: bool
    wellpump_delay_active: bool
    activation_code: _wrappers_pb2.StringValue
    def __init__(
        self,
        name: _Optional[str] = ...,
        geo_point: _Optional[_Union[_core_pb2.GeoPoint, _Mapping]] = ...,
        location_id: _Optional[str] = ...,
        pin: _Optional[str] = ...,
        agent_id: _Optional[str] = ...,
        external_plan_id: _Optional[str] = ...,
        serial_number: _Optional[str] = ...,
        master_valve: bool = ...,
        water_hammer: bool = ...,
        wellpump_delay_active: bool = ...,
        activation_code: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...,
    ) -> None: ...

class CreateGen1IrrigationControllerResponse(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _irrigation_controller_pb2.Gen1IrrigationController
    def __init__(
        self,
        value: _Optional[
            _Union[_irrigation_controller_pb2.Gen1IrrigationController, _Mapping]
        ] = ...,
    ) -> None: ...

class CreateGen2IrrigationControllerRequest(_message.Message):
    __slots__ = (
        "name",
        "geo_point",
        "location_id",
        "serial_number",
        "master_valve",
        "water_hammer",
        "wellpump_delay_active",
        "activation_code",
    )
    NAME_FIELD_NUMBER: _ClassVar[int]
    GEO_POINT_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    MASTER_VALVE_FIELD_NUMBER: _ClassVar[int]
    WATER_HAMMER_FIELD_NUMBER: _ClassVar[int]
    WELLPUMP_DELAY_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    ACTIVATION_CODE_FIELD_NUMBER: _ClassVar[int]
    name: str
    geo_point: _core_pb2.GeoPoint
    location_id: str
    serial_number: str
    master_valve: bool
    water_hammer: bool
    wellpump_delay_active: bool
    activation_code: _wrappers_pb2.StringValue
    def __init__(
        self,
        name: _Optional[str] = ...,
        geo_point: _Optional[_Union[_core_pb2.GeoPoint, _Mapping]] = ...,
        location_id: _Optional[str] = ...,
        serial_number: _Optional[str] = ...,
        master_valve: bool = ...,
        water_hammer: bool = ...,
        wellpump_delay_active: bool = ...,
        activation_code: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...,
    ) -> None: ...

class CreateGen2IrrigationControllerResponse(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _irrigation_controller_pb2.Gen2IrrigationController
    def __init__(
        self,
        value: _Optional[
            _Union[_irrigation_controller_pb2.Gen2IrrigationController, _Mapping]
        ] = ...,
    ) -> None: ...

class CreateGen3IrrigationControllerRequest(_message.Message):
    __slots__ = (
        "name",
        "geo_point",
        "location_id",
        "serial_number",
        "master_valve",
        "water_hammer",
        "wellpump_delay_active",
        "activation_code",
    )
    NAME_FIELD_NUMBER: _ClassVar[int]
    GEO_POINT_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    MASTER_VALVE_FIELD_NUMBER: _ClassVar[int]
    WATER_HAMMER_FIELD_NUMBER: _ClassVar[int]
    WELLPUMP_DELAY_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    ACTIVATION_CODE_FIELD_NUMBER: _ClassVar[int]
    name: str
    geo_point: _core_pb2.GeoPoint
    location_id: str
    serial_number: str
    master_valve: bool
    water_hammer: bool
    wellpump_delay_active: bool
    activation_code: _wrappers_pb2.StringValue
    def __init__(
        self,
        name: _Optional[str] = ...,
        geo_point: _Optional[_Union[_core_pb2.GeoPoint, _Mapping]] = ...,
        location_id: _Optional[str] = ...,
        serial_number: _Optional[str] = ...,
        master_valve: bool = ...,
        water_hammer: bool = ...,
        wellpump_delay_active: bool = ...,
        activation_code: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...,
    ) -> None: ...

class CreateGen3IrrigationControllerResponse(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _irrigation_controller_pb2.Gen3IrrigationController
    def __init__(
        self,
        value: _Optional[
            _Union[_irrigation_controller_pb2.Gen3IrrigationController, _Mapping]
        ] = ...,
    ) -> None: ...

class CreateVirtualIrrigationControllerRequest(_message.Message):
    __slots__ = ("name", "geo_point", "location_id", "serial_number", "model")
    NAME_FIELD_NUMBER: _ClassVar[int]
    GEO_POINT_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    name: str
    geo_point: _core_pb2.GeoPoint
    location_id: str
    serial_number: str
    model: _irrigation_controller_pb2.IrrigationControllerModelType
    def __init__(
        self,
        name: _Optional[str] = ...,
        geo_point: _Optional[_Union[_core_pb2.GeoPoint, _Mapping]] = ...,
        location_id: _Optional[str] = ...,
        serial_number: _Optional[str] = ...,
        model: _Optional[
            _Union[_irrigation_controller_pb2.IrrigationControllerModelType, str]
        ] = ...,
    ) -> None: ...

class CreateWirelessFlowSensorRequest(_message.Message):
    __slots__ = ("name", "serial_number", "controller_id", "location_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    serial_number: str
    controller_id: str
    location_id: str
    def __init__(
        self,
        name: _Optional[str] = ...,
        serial_number: _Optional[str] = ...,
        controller_id: _Optional[str] = ...,
        location_id: _Optional[str] = ...,
    ) -> None: ...

class CreateWirelessFlowSensorResponse(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _sensor_pb2.WirelessFlowSensor
    def __init__(
        self, value: _Optional[_Union[_sensor_pb2.WirelessFlowSensor, _Mapping]] = ...
    ) -> None: ...

class UpdateWirelessFlowSensorRequest(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: _wrappers_pb2.StringValue
    def __init__(
        self,
        id: _Optional[str] = ...,
        name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...,
    ) -> None: ...

class UpdateWirelessFlowSensorResponse(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _sensor_pb2.WirelessFlowSensor
    def __init__(
        self, value: _Optional[_Union[_sensor_pb2.WirelessFlowSensor, _Mapping]] = ...
    ) -> None: ...

class RmaWirelessFlowSensorRequest(_message.Message):
    __slots__ = ("serial_number",)
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    serial_number: str
    def __init__(self, serial_number: _Optional[str] = ...) -> None: ...

class RmaWirelessFlowSensorResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateLocationAndGen1IrrigationControllerRequest(_message.Message):
    __slots__ = ("location", "controller", "property_id")
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_ID_FIELD_NUMBER: _ClassVar[int]
    location: _location_service_pb2.CreateLocationRequest
    controller: CreateGen1IrrigationControllerRequest
    property_id: _wrappers_pb2.StringValue
    def __init__(
        self,
        location: _Optional[
            _Union[_location_service_pb2.CreateLocationRequest, _Mapping]
        ] = ...,
        controller: _Optional[
            _Union[CreateGen1IrrigationControllerRequest, _Mapping]
        ] = ...,
        property_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...,
    ) -> None: ...

class CreateLocationAndGen1IrrigationControllerResponse(_message.Message):
    __slots__ = ("location", "controller")
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_FIELD_NUMBER: _ClassVar[int]
    location: _location_pb2.Location
    controller: _irrigation_controller_pb2.Gen1IrrigationController
    def __init__(
        self,
        location: _Optional[_Union[_location_pb2.Location, _Mapping]] = ...,
        controller: _Optional[
            _Union[_irrigation_controller_pb2.Gen1IrrigationController, _Mapping]
        ] = ...,
    ) -> None: ...

class CreateLocationAndGen2IrrigationControllerRequest(_message.Message):
    __slots__ = ("location", "controller", "property_id")
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_ID_FIELD_NUMBER: _ClassVar[int]
    location: _location_service_pb2.CreateLocationRequest
    controller: CreateGen2IrrigationControllerRequest
    property_id: _wrappers_pb2.StringValue
    def __init__(
        self,
        location: _Optional[
            _Union[_location_service_pb2.CreateLocationRequest, _Mapping]
        ] = ...,
        controller: _Optional[
            _Union[CreateGen2IrrigationControllerRequest, _Mapping]
        ] = ...,
        property_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...,
    ) -> None: ...

class CreateLocationAndGen2IrrigationControllerResponse(_message.Message):
    __slots__ = ("location", "controller")
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_FIELD_NUMBER: _ClassVar[int]
    location: _location_pb2.Location
    controller: _irrigation_controller_pb2.Gen2IrrigationController
    def __init__(
        self,
        location: _Optional[_Union[_location_pb2.Location, _Mapping]] = ...,
        controller: _Optional[
            _Union[_irrigation_controller_pb2.Gen2IrrigationController, _Mapping]
        ] = ...,
    ) -> None: ...

class CreateLocationAndGen3IrrigationControllerRequest(_message.Message):
    __slots__ = ("location", "controller", "property_id")
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_ID_FIELD_NUMBER: _ClassVar[int]
    location: _location_service_pb2.CreateLocationRequest
    controller: CreateGen3IrrigationControllerRequest
    property_id: _wrappers_pb2.StringValue
    def __init__(
        self,
        location: _Optional[
            _Union[_location_service_pb2.CreateLocationRequest, _Mapping]
        ] = ...,
        controller: _Optional[
            _Union[CreateGen3IrrigationControllerRequest, _Mapping]
        ] = ...,
        property_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...,
    ) -> None: ...

class CreateLocationAndGen3IrrigationControllerResponse(_message.Message):
    __slots__ = ("location", "controller")
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_FIELD_NUMBER: _ClassVar[int]
    location: _location_pb2.Location
    controller: _irrigation_controller_pb2.Gen3IrrigationController
    def __init__(
        self,
        location: _Optional[_Union[_location_pb2.Location, _Mapping]] = ...,
        controller: _Optional[
            _Union[_irrigation_controller_pb2.Gen3IrrigationController, _Mapping]
        ] = ...,
    ) -> None: ...

class CreateLocationAndVirtualIrrigationControllerRequest(_message.Message):
    __slots__ = ("location", "controller")
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_FIELD_NUMBER: _ClassVar[int]
    location: _location_service_pb2.CreateLocationRequest
    controller: CreateVirtualIrrigationControllerRequest
    def __init__(
        self,
        location: _Optional[
            _Union[_location_service_pb2.CreateLocationRequest, _Mapping]
        ] = ...,
        controller: _Optional[
            _Union[CreateVirtualIrrigationControllerRequest, _Mapping]
        ] = ...,
    ) -> None: ...

class CreateLocationAndVirtualIrrigationControllerResponse(_message.Message):
    __slots__ = ("location", "controller")
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_FIELD_NUMBER: _ClassVar[int]
    location: _location_pb2.Location
    controller: _irrigation_controller_pb2.VirtualIrrigationController
    def __init__(
        self,
        location: _Optional[_Union[_location_pb2.Location, _Mapping]] = ...,
        controller: _Optional[
            _Union[_irrigation_controller_pb2.VirtualIrrigationController, _Mapping]
        ] = ...,
    ) -> None: ...

class UpdateIrrigationControllerRequest(_message.Message):
    __slots__ = (
        "id",
        "name",
        "geo_point",
        "location_id",
        "master_valve",
        "standby",
        "water_hammer",
        "add_photo_bytes",
        "remove_photo_id",
        "weather_intelligence_plus",
        "wellpump_delay_active",
        "settle_time",
        "idle_leak_detection",
        "idle_leak_time",
    )
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    GEO_POINT_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    MASTER_VALVE_FIELD_NUMBER: _ClassVar[int]
    STANDBY_FIELD_NUMBER: _ClassVar[int]
    WATER_HAMMER_FIELD_NUMBER: _ClassVar[int]
    ADD_PHOTO_BYTES_FIELD_NUMBER: _ClassVar[int]
    REMOVE_PHOTO_ID_FIELD_NUMBER: _ClassVar[int]
    WEATHER_INTELLIGENCE_PLUS_FIELD_NUMBER: _ClassVar[int]
    WELLPUMP_DELAY_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    SETTLE_TIME_FIELD_NUMBER: _ClassVar[int]
    IDLE_LEAK_DETECTION_FIELD_NUMBER: _ClassVar[int]
    IDLE_LEAK_TIME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: _wrappers_pb2.StringValue
    geo_point: _core_pb2.GeoPoint
    location_id: _wrappers_pb2.StringValue
    master_valve: _wrappers_pb2.BoolValue
    standby: _wrappers_pb2.BoolValue
    water_hammer: _wrappers_pb2.BoolValue
    add_photo_bytes: _containers.RepeatedCompositeFieldContainer[
        _wrappers_pb2.BytesValue
    ]
    remove_photo_id: _containers.RepeatedScalarFieldContainer[str]
    weather_intelligence_plus: _wrappers_pb2.BoolValue
    wellpump_delay_active: _wrappers_pb2.BoolValue
    settle_time: _wrappers_pb2.Int32Value
    idle_leak_detection: _wrappers_pb2.BoolValue
    idle_leak_time: _wrappers_pb2.Int32Value
    def __init__(
        self,
        id: _Optional[str] = ...,
        name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...,
        geo_point: _Optional[_Union[_core_pb2.GeoPoint, _Mapping]] = ...,
        location_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...,
        master_valve: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        standby: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        water_hammer: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        add_photo_bytes: _Optional[
            _Iterable[_Union[_wrappers_pb2.BytesValue, _Mapping]]
        ] = ...,
        remove_photo_id: _Optional[_Iterable[str]] = ...,
        weather_intelligence_plus: _Optional[
            _Union[_wrappers_pb2.BoolValue, _Mapping]
        ] = ...,
        wellpump_delay_active: _Optional[
            _Union[_wrappers_pb2.BoolValue, _Mapping]
        ] = ...,
        settle_time: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...,
        idle_leak_detection: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        idle_leak_time: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...,
    ) -> None: ...

class UpdateIrrigationControllerResponse(_message.Message):
    __slots__ = (
        "gen1_irrigation_controller",
        "gen2_irrigation_controller",
        "gen3_irrigation_controller",
        "virtual_irrigation_controller",
    )
    GEN1_IRRIGATION_CONTROLLER_FIELD_NUMBER: _ClassVar[int]
    GEN2_IRRIGATION_CONTROLLER_FIELD_NUMBER: _ClassVar[int]
    GEN3_IRRIGATION_CONTROLLER_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_IRRIGATION_CONTROLLER_FIELD_NUMBER: _ClassVar[int]
    gen1_irrigation_controller: _irrigation_controller_pb2.Gen1IrrigationController
    gen2_irrigation_controller: _irrigation_controller_pb2.Gen2IrrigationController
    gen3_irrigation_controller: _irrigation_controller_pb2.Gen3IrrigationController
    virtual_irrigation_controller: (
        _irrigation_controller_pb2.VirtualIrrigationController
    )
    def __init__(
        self,
        gen1_irrigation_controller: _Optional[
            _Union[_irrigation_controller_pb2.Gen1IrrigationController, _Mapping]
        ] = ...,
        gen2_irrigation_controller: _Optional[
            _Union[_irrigation_controller_pb2.Gen2IrrigationController, _Mapping]
        ] = ...,
        gen3_irrigation_controller: _Optional[
            _Union[_irrigation_controller_pb2.Gen3IrrigationController, _Mapping]
        ] = ...,
        virtual_irrigation_controller: _Optional[
            _Union[_irrigation_controller_pb2.VirtualIrrigationController, _Mapping]
        ] = ...,
    ) -> None: ...

class ListDevicePhotosRequest(_message.Message):
    __slots__ = ("device_id",)
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    def __init__(self, device_id: _Optional[str] = ...) -> None: ...

class ListDevicePhotosResponse(_message.Message):
    __slots__ = ("photo_id",)
    PHOTO_ID_FIELD_NUMBER: _ClassVar[int]
    photo_id: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.StringValue]
    def __init__(
        self,
        photo_id: _Optional[
            _Iterable[_Union[_wrappers_pb2.StringValue, _Mapping]]
        ] = ...,
    ) -> None: ...

class GetDevicePhotosRequest(_message.Message):
    __slots__ = ("device_id",)
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    def __init__(self, device_id: _Optional[str] = ...) -> None: ...

class GetDevicePhotosResponse(_message.Message):
    __slots__ = ("photo_bytes",)
    PHOTO_BYTES_FIELD_NUMBER: _ClassVar[int]
    photo_bytes: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.BytesValue]
    def __init__(
        self,
        photo_bytes: _Optional[
            _Iterable[_Union[_wrappers_pb2.BytesValue, _Mapping]]
        ] = ...,
    ) -> None: ...

class GetDevicePhotoRequest(_message.Message):
    __slots__ = ("device_id", "photo_id")
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    PHOTO_ID_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    photo_id: str
    def __init__(
        self, device_id: _Optional[str] = ..., photo_id: _Optional[str] = ...
    ) -> None: ...

class GetDevicePhotoResponse(_message.Message):
    __slots__ = ("photo_bytes",)
    PHOTO_BYTES_FIELD_NUMBER: _ClassVar[int]
    photo_bytes: _wrappers_pb2.BytesValue
    def __init__(
        self, photo_bytes: _Optional[_Union[_wrappers_pb2.BytesValue, _Mapping]] = ...
    ) -> None: ...

class UpdateLinkedSensorRequest(_message.Message):
    __slots__ = (
        "id",
        "make",
        "model",
        "kfactor",
        "offset",
        "enabled",
        "sensorType",
        "linked_controller_id",
    )
    class LinkedSensorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RAIN: _ClassVar[UpdateLinkedSensorRequest.LinkedSensorType]
        FLOW: _ClassVar[UpdateLinkedSensorRequest.LinkedSensorType]

    RAIN: UpdateLinkedSensorRequest.LinkedSensorType
    FLOW: UpdateLinkedSensorRequest.LinkedSensorType
    ID_FIELD_NUMBER: _ClassVar[int]
    MAKE_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    KFACTOR_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    SENSORTYPE_FIELD_NUMBER: _ClassVar[int]
    LINKED_CONTROLLER_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    make: _wrappers_pb2.StringValue
    model: _wrappers_pb2.StringValue
    kfactor: _wrappers_pb2.DoubleValue
    offset: _wrappers_pb2.DoubleValue
    enabled: bool
    sensorType: UpdateLinkedSensorRequest.LinkedSensorType
    linked_controller_id: str
    def __init__(
        self,
        id: _Optional[str] = ...,
        make: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...,
        model: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...,
        kfactor: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ...,
        offset: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ...,
        enabled: bool = ...,
        sensorType: _Optional[
            _Union[UpdateLinkedSensorRequest.LinkedSensorType, str]
        ] = ...,
        linked_controller_id: _Optional[str] = ...,
    ) -> None: ...

class UpdateLinkedSensorResponse(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _sensor_pb2.LinkedSensor
    def __init__(
        self, value: _Optional[_Union[_sensor_pb2.LinkedSensor, _Mapping]] = ...
    ) -> None: ...

class GetDesiredFirmwareRequest(_message.Message):
    __slots__ = ("device_id",)
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    def __init__(self, device_id: _Optional[str] = ...) -> None: ...

class GetDesiredFirmwareResponse(_message.Message):
    __slots__ = (
        "device_id",
        "current_firmware_name",
        "desired_firmware_name",
        "desired_firmware_url",
    )
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    CURRENT_FIRMWARE_NAME_FIELD_NUMBER: _ClassVar[int]
    DESIRED_FIRMWARE_NAME_FIELD_NUMBER: _ClassVar[int]
    DESIRED_FIRMWARE_URL_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    current_firmware_name: str
    desired_firmware_name: str
    desired_firmware_url: str
    def __init__(
        self,
        device_id: _Optional[str] = ...,
        current_firmware_name: _Optional[str] = ...,
        desired_firmware_name: _Optional[str] = ...,
        desired_firmware_url: _Optional[str] = ...,
    ) -> None: ...

class UpdateFirmwareRequest(_message.Message):
    __slots__ = ("device_id",)
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    def __init__(self, device_id: _Optional[str] = ...) -> None: ...

class UpdateFirmwareResponse(_message.Message):
    __slots__ = (
        "device_id",
        "current_firmware_name",
        "desired_firmware_name",
        "desired_firmware_url",
    )
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    CURRENT_FIRMWARE_NAME_FIELD_NUMBER: _ClassVar[int]
    DESIRED_FIRMWARE_NAME_FIELD_NUMBER: _ClassVar[int]
    DESIRED_FIRMWARE_URL_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    current_firmware_name: str
    desired_firmware_name: str
    desired_firmware_url: str
    def __init__(
        self,
        device_id: _Optional[str] = ...,
        current_firmware_name: _Optional[str] = ...,
        desired_firmware_name: _Optional[str] = ...,
        desired_firmware_url: _Optional[str] = ...,
    ) -> None: ...

class UpgradeToLatestFirmwareRequest(_message.Message):
    __slots__ = ("device_id",)
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    def __init__(self, device_id: _Optional[str] = ...) -> None: ...

class UpgradeToLatestFirmwareResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetManualScheduleRequest(_message.Message):
    __slots__ = (
        "device_id",
        "runs",
        "cycle_soak",
        "cycle_soak_duration",
        "cycle_duration",
        "soak_duration",
    )
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    RUNS_FIELD_NUMBER: _ClassVar[int]
    CYCLE_SOAK_FIELD_NUMBER: _ClassVar[int]
    CYCLE_SOAK_DURATION_FIELD_NUMBER: _ClassVar[int]
    CYCLE_DURATION_FIELD_NUMBER: _ClassVar[int]
    SOAK_DURATION_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    runs: _containers.RepeatedCompositeFieldContainer[ManualZoneRun]
    cycle_soak: bool
    cycle_soak_duration: int
    cycle_duration: _wrappers_pb2.Int32Value
    soak_duration: _wrappers_pb2.Int32Value
    def __init__(
        self,
        device_id: _Optional[str] = ...,
        runs: _Optional[_Iterable[_Union[ManualZoneRun, _Mapping]]] = ...,
        cycle_soak: bool = ...,
        cycle_soak_duration: _Optional[int] = ...,
        cycle_duration: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...,
        soak_duration: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...,
    ) -> None: ...

class ManualZoneRun(_message.Message):
    __slots__ = ("duration", "zone_number")
    DURATION_FIELD_NUMBER: _ClassVar[int]
    ZONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    duration: int
    zone_number: int
    def __init__(
        self, duration: _Optional[int] = ..., zone_number: _Optional[int] = ...
    ) -> None: ...

class SetManualScheduleResponse(_message.Message):
    __slots__ = ("manual_schedule_id",)
    MANUAL_SCHEDULE_ID_FIELD_NUMBER: _ClassVar[int]
    manual_schedule_id: int
    def __init__(self, manual_schedule_id: _Optional[int] = ...) -> None: ...

class StartZoneCalibrationRequest(_message.Message):
    __slots__ = ("zone_id",)
    ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    zone_id: str
    def __init__(self, zone_id: _Optional[str] = ...) -> None: ...

class StartZoneCalibrationResponse(_message.Message):
    __slots__ = ("manual_schedule_id", "correlation_id")
    MANUAL_SCHEDULE_ID_FIELD_NUMBER: _ClassVar[int]
    CORRELATION_ID_FIELD_NUMBER: _ClassVar[int]
    manual_schedule_id: int
    correlation_id: int
    def __init__(
        self,
        manual_schedule_id: _Optional[int] = ...,
        correlation_id: _Optional[int] = ...,
    ) -> None: ...

class StopZoneCalibrationRequest(_message.Message):
    __slots__ = ("zone_id",)
    ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    zone_id: str
    def __init__(self, zone_id: _Optional[str] = ...) -> None: ...

class StopZoneCalibrationResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ClearManualScheduleRequest(_message.Message):
    __slots__ = ("device_id",)
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    def __init__(self, device_id: _Optional[str] = ...) -> None: ...

class ClearManualScheduleResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetRainDelayRequest(_message.Message):
    __slots__ = ("device_id", "rain_delay_expiration")
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    RAIN_DELAY_EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    rain_delay_expiration: _timestamp_pb2.Timestamp
    def __init__(
        self,
        device_id: _Optional[str] = ...,
        rain_delay_expiration: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
    ) -> None: ...

class SetRainDelayResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StopWateringRequest(_message.Message):
    __slots__ = ("device_id",)
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    def __init__(self, device_id: _Optional[str] = ...) -> None: ...

class StopWateringResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetZoneDefaultRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetZoneDefaultResponse(_message.Message):
    __slots__ = ("zoneDefault",)
    ZONEDEFAULT_FIELD_NUMBER: _ClassVar[int]
    zoneDefault: ZoneDefault
    def __init__(
        self, zoneDefault: _Optional[_Union[ZoneDefault, _Mapping]] = ...
    ) -> None: ...

class ZoneDefault(_message.Message):
    __slots__ = (
        "available_water_capacity",
        "root_zone_depth",
        "efficiency",
        "flow_rate",
        "crop_coefficient",
        "managed_allowed_depletion",
    )
    AVAILABLE_WATER_CAPACITY_FIELD_NUMBER: _ClassVar[int]
    ROOT_ZONE_DEPTH_FIELD_NUMBER: _ClassVar[int]
    EFFICIENCY_FIELD_NUMBER: _ClassVar[int]
    FLOW_RATE_FIELD_NUMBER: _ClassVar[int]
    CROP_COEFFICIENT_FIELD_NUMBER: _ClassVar[int]
    MANAGED_ALLOWED_DEPLETION_FIELD_NUMBER: _ClassVar[int]
    available_water_capacity: float
    root_zone_depth: float
    efficiency: float
    flow_rate: float
    crop_coefficient: float
    managed_allowed_depletion: float
    def __init__(
        self,
        available_water_capacity: _Optional[float] = ...,
        root_zone_depth: _Optional[float] = ...,
        efficiency: _Optional[float] = ...,
        flow_rate: _Optional[float] = ...,
        crop_coefficient: _Optional[float] = ...,
        managed_allowed_depletion: _Optional[float] = ...,
    ) -> None: ...

class GetCalendarRequest(_message.Message):
    __slots__ = ("device_id", "start_time", "end_time")
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    def __init__(
        self,
        device_id: _Optional[str] = ...,
        start_time: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        end_time: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
    ) -> None: ...

class GetCalendarResponse(_message.Message):
    __slots__ = ("version_id", "runs", "skips")
    VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    RUNS_FIELD_NUMBER: _ClassVar[int]
    SKIPS_FIELD_NUMBER: _ClassVar[int]
    version_id: int
    runs: _containers.RepeatedCompositeFieldContainer[_schedule_run_pb2.ScheduleRun]
    skips: _containers.RepeatedCompositeFieldContainer[_skip_sequence_pb2.SkipSequence]
    def __init__(
        self,
        version_id: _Optional[int] = ...,
        runs: _Optional[
            _Iterable[_Union[_schedule_run_pb2.ScheduleRun, _Mapping]]
        ] = ...,
        skips: _Optional[
            _Iterable[_Union[_skip_sequence_pb2.SkipSequence, _Mapping]]
        ] = ...,
    ) -> None: ...

class GetYardLikeMineRequest(_message.Message):
    __slots__ = ("device_id", "offset", "limit")
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    offset: _wrappers_pb2.Int32Value
    limit: _wrappers_pb2.Int32Value
    def __init__(
        self,
        device_id: _Optional[str] = ...,
        offset: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...,
        limit: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...,
    ) -> None: ...

class GetYardLikeMineResponse(_message.Message):
    __slots__ = (
        "water_usage",
        "green_score",
        "yard",
        "end_of_yard_list",
        "current_list_offset",
    )
    WATER_USAGE_FIELD_NUMBER: _ClassVar[int]
    GREEN_SCORE_FIELD_NUMBER: _ClassVar[int]
    YARD_FIELD_NUMBER: _ClassVar[int]
    END_OF_YARD_LIST_FIELD_NUMBER: _ClassVar[int]
    CURRENT_LIST_OFFSET_FIELD_NUMBER: _ClassVar[int]
    water_usage: float
    green_score: float
    yard: _containers.RepeatedCompositeFieldContainer[_yard_like_mine_pb2.YardLikeMine]
    end_of_yard_list: bool
    current_list_offset: _wrappers_pb2.Int32Value
    def __init__(
        self,
        water_usage: _Optional[float] = ...,
        green_score: _Optional[float] = ...,
        yard: _Optional[
            _Iterable[_Union[_yard_like_mine_pb2.YardLikeMine, _Mapping]]
        ] = ...,
        end_of_yard_list: bool = ...,
        current_list_offset: _Optional[
            _Union[_wrappers_pb2.Int32Value, _Mapping]
        ] = ...,
    ) -> None: ...

class GetYardLikeMineDetailRequest(_message.Message):
    __slots__ = ("device_id",)
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    def __init__(self, device_id: _Optional[str] = ...) -> None: ...

class GetYardLikeMineDetailResponse(_message.Message):
    __slots__ = (
        "device_id",
        "water_usage",
        "zone_photo_id",
        "schedule_types",
        "updated",
        "is_updated",
    )
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    WATER_USAGE_FIELD_NUMBER: _ClassVar[int]
    ZONE_PHOTO_ID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_TYPES_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    IS_UPDATED_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    water_usage: float
    zone_photo_id: _containers.RepeatedScalarFieldContainer[str]
    schedule_types: _containers.RepeatedScalarFieldContainer[
        _schedule_criteria_pb2.ScheduleType
    ]
    updated: _timestamp_pb2.Timestamp
    is_updated: bool
    def __init__(
        self,
        device_id: _Optional[str] = ...,
        water_usage: _Optional[float] = ...,
        zone_photo_id: _Optional[_Iterable[str]] = ...,
        schedule_types: _Optional[
            _Iterable[_Union[_schedule_criteria_pb2.ScheduleType, str]]
        ] = ...,
        updated: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        is_updated: bool = ...,
    ) -> None: ...

class SkipForwardZoneRunRequest(_message.Message):
    __slots__ = ("device_id",)
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    def __init__(self, device_id: _Optional[str] = ...) -> None: ...

class SkipForwardZoneRunResponse(_message.Message):
    __slots__ = ("running_zone", "running_schedule")
    RUNNING_ZONE_FIELD_NUMBER: _ClassVar[int]
    RUNNING_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    running_zone: _controller_state_pb2.ZoneRun
    running_schedule: _controller_state_pb2.ImmediateScheduleRun
    def __init__(
        self,
        running_zone: _Optional[_Union[_controller_state_pb2.ZoneRun, _Mapping]] = ...,
        running_schedule: _Optional[
            _Union[_controller_state_pb2.ImmediateScheduleRun, _Mapping]
        ] = ...,
    ) -> None: ...

class SkipBackwardZoneRunRequest(_message.Message):
    __slots__ = ("device_id",)
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    def __init__(self, device_id: _Optional[str] = ...) -> None: ...

class SkipBackwardZoneRunResponse(_message.Message):
    __slots__ = ("running_zone", "running_schedule")
    RUNNING_ZONE_FIELD_NUMBER: _ClassVar[int]
    RUNNING_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    running_zone: _controller_state_pb2.ZoneRun
    running_schedule: _controller_state_pb2.ImmediateScheduleRun
    def __init__(
        self,
        running_zone: _Optional[_Union[_controller_state_pb2.ZoneRun, _Mapping]] = ...,
        running_schedule: _Optional[
            _Union[_controller_state_pb2.ImmediateScheduleRun, _Mapping]
        ] = ...,
    ) -> None: ...

class PauseZoneRunRequest(_message.Message):
    __slots__ = ("device_id", "seconds_paused")
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    SECONDS_PAUSED_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    seconds_paused: int
    def __init__(
        self, device_id: _Optional[str] = ..., seconds_paused: _Optional[int] = ...
    ) -> None: ...

class PauseZoneRunResponse(_message.Message):
    __slots__ = ("running_zone", "running_schedule")
    RUNNING_ZONE_FIELD_NUMBER: _ClassVar[int]
    RUNNING_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    running_zone: _controller_state_pb2.ZoneRun
    running_schedule: _controller_state_pb2.ImmediateScheduleRun
    def __init__(
        self,
        running_zone: _Optional[_Union[_controller_state_pb2.ZoneRun, _Mapping]] = ...,
        running_schedule: _Optional[
            _Union[_controller_state_pb2.ImmediateScheduleRun, _Mapping]
        ] = ...,
    ) -> None: ...

class ResumeZoneRunRequest(_message.Message):
    __slots__ = ("device_id",)
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    def __init__(self, device_id: _Optional[str] = ...) -> None: ...

class ResumeZoneRunResponse(_message.Message):
    __slots__ = ("running_zone", "running_schedule")
    RUNNING_ZONE_FIELD_NUMBER: _ClassVar[int]
    RUNNING_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    running_zone: _controller_state_pb2.ZoneRun
    running_schedule: _controller_state_pb2.ImmediateScheduleRun
    def __init__(
        self,
        running_zone: _Optional[_Union[_controller_state_pb2.ZoneRun, _Mapping]] = ...,
        running_schedule: _Optional[
            _Union[_controller_state_pb2.ImmediateScheduleRun, _Mapping]
        ] = ...,
    ) -> None: ...

class ExtendZoneRunRequest(_message.Message):
    __slots__ = ("device_id", "seconds_extended")
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    SECONDS_EXTENDED_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    seconds_extended: int
    def __init__(
        self, device_id: _Optional[str] = ..., seconds_extended: _Optional[int] = ...
    ) -> None: ...

class ExtendZoneRunResponse(_message.Message):
    __slots__ = ("running_zone", "running_schedule")
    RUNNING_ZONE_FIELD_NUMBER: _ClassVar[int]
    RUNNING_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    running_zone: _controller_state_pb2.ZoneRun
    running_schedule: _controller_state_pb2.ImmediateScheduleRun
    def __init__(
        self,
        running_zone: _Optional[_Union[_controller_state_pb2.ZoneRun, _Mapping]] = ...,
        running_schedule: _Optional[
            _Union[_controller_state_pb2.ImmediateScheduleRun, _Mapping]
        ] = ...,
    ) -> None: ...

class StopWateringQRRequest(_message.Message):
    __slots__ = ("device_id", "code")
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    code: str
    def __init__(
        self, device_id: _Optional[str] = ..., code: _Optional[str] = ...
    ) -> None: ...

class GetDeviceStateQRRequest(_message.Message):
    __slots__ = ("device_id", "code")
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    code: str
    def __init__(
        self, device_id: _Optional[str] = ..., code: _Optional[str] = ...
    ) -> None: ...

class GetDeviceStateQRResponse(_message.Message):
    __slots__ = ("state",)
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: _controller_state_pb2.ControllerState
    def __init__(
        self,
        state: _Optional[_Union[_controller_state_pb2.ControllerState, _Mapping]] = ...,
    ) -> None: ...

class GetDeviceDetailsQRRequest(_message.Message):
    __slots__ = ("id", "code")
    ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    id: str
    code: str
    def __init__(
        self, id: _Optional[str] = ..., code: _Optional[str] = ...
    ) -> None: ...

class GetDeviceDetailsYLMRequest(_message.Message):
    __slots__ = ("id", "code")
    ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    id: str
    code: str
    def __init__(
        self, id: _Optional[str] = ..., code: _Optional[str] = ...
    ) -> None: ...

class SetManualScheduleQRRequest(_message.Message):
    __slots__ = ("device_id", "runs", "code")
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    RUNS_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    runs: _containers.RepeatedCompositeFieldContainer[ManualZoneRun]
    code: str
    def __init__(
        self,
        device_id: _Optional[str] = ...,
        runs: _Optional[_Iterable[_Union[ManualZoneRun, _Mapping]]] = ...,
        code: _Optional[str] = ...,
    ) -> None: ...

class SkipForwardZoneRunQRRequest(_message.Message):
    __slots__ = ("device_id", "code")
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    code: str
    def __init__(
        self, device_id: _Optional[str] = ..., code: _Optional[str] = ...
    ) -> None: ...

class SkipBackwardZoneRunQRRequest(_message.Message):
    __slots__ = ("device_id", "code")
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    code: str
    def __init__(
        self, device_id: _Optional[str] = ..., code: _Optional[str] = ...
    ) -> None: ...

class PauseZoneRunQRRequest(_message.Message):
    __slots__ = ("device_id", "seconds_paused", "code")
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    SECONDS_PAUSED_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    seconds_paused: int
    code: str
    def __init__(
        self,
        device_id: _Optional[str] = ...,
        seconds_paused: _Optional[int] = ...,
        code: _Optional[str] = ...,
    ) -> None: ...

class ResumeZoneRunQRRequest(_message.Message):
    __slots__ = ("device_id", "code")
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    code: str
    def __init__(
        self, device_id: _Optional[str] = ..., code: _Optional[str] = ...
    ) -> None: ...

class ExtendZoneRunQRRequest(_message.Message):
    __slots__ = ("device_id", "seconds_extended", "code")
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    SECONDS_EXTENDED_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    seconds_extended: int
    code: str
    def __init__(
        self,
        device_id: _Optional[str] = ...,
        seconds_extended: _Optional[int] = ...,
        code: _Optional[str] = ...,
    ) -> None: ...

class ListZonesQRRequest(_message.Message):
    __slots__ = ("device_id", "code")
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    code: str
    def __init__(
        self, device_id: _Optional[str] = ..., code: _Optional[str] = ...
    ) -> None: ...

class ListZonesQRResponse(_message.Message):
    __slots__ = ("zone_summary",)
    ZONE_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    zone_summary: _containers.RepeatedCompositeFieldContainer[ZoneSummary]
    def __init__(
        self, zone_summary: _Optional[_Iterable[_Union[ZoneSummary, _Mapping]]] = ...
    ) -> None: ...

class ListZonesYLMRequest(_message.Message):
    __slots__ = ("device_id", "code")
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    code: str
    def __init__(
        self, device_id: _Optional[str] = ..., code: _Optional[str] = ...
    ) -> None: ...

class GetFlowSensorDataRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetFlowSensorDataResponse(_message.Message):
    __slots__ = ("flow_sensor_data",)
    FLOW_SENSOR_DATA_FIELD_NUMBER: _ClassVar[int]
    flow_sensor_data: _containers.RepeatedCompositeFieldContainer[
        _sensor_pb2.FlowSensor
    ]
    def __init__(
        self,
        flow_sensor_data: _Optional[
            _Iterable[_Union[_sensor_pb2.FlowSensor, _Mapping]]
        ] = ...,
    ) -> None: ...

class GetLastZoneRunStateRequest(_message.Message):
    __slots__ = ("device_id",)
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    def __init__(self, device_id: _Optional[str] = ...) -> None: ...

class GetLastZoneRunStateResponse(_message.Message):
    __slots__ = ("last_zone_run_states",)
    LAST_ZONE_RUN_STATES_FIELD_NUMBER: _ClassVar[int]
    last_zone_run_states: _containers.RepeatedCompositeFieldContainer[LastZoneRunState]
    def __init__(
        self,
        last_zone_run_states: _Optional[
            _Iterable[_Union[LastZoneRunState, _Mapping]]
        ] = ...,
    ) -> None: ...

class LastZoneRunState(_message.Message):
    __slots__ = (
        "id",
        "device_id",
        "zone_number",
        "last_run_start_current",
        "last_run_end_current",
        "last_run_start_time",
        "last_run_end_time",
    )
    ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    LAST_RUN_START_CURRENT_FIELD_NUMBER: _ClassVar[int]
    LAST_RUN_END_CURRENT_FIELD_NUMBER: _ClassVar[int]
    LAST_RUN_START_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_RUN_END_TIME_FIELD_NUMBER: _ClassVar[int]
    id: str
    device_id: str
    zone_number: int
    last_run_start_current: int
    last_run_end_current: int
    last_run_start_time: _timestamp_pb2.Timestamp
    last_run_end_time: _timestamp_pb2.Timestamp
    def __init__(
        self,
        id: _Optional[str] = ...,
        device_id: _Optional[str] = ...,
        zone_number: _Optional[int] = ...,
        last_run_start_current: _Optional[int] = ...,
        last_run_end_current: _Optional[int] = ...,
        last_run_start_time: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        last_run_end_time: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
    ) -> None: ...

class GetActiveAlertsRequest(_message.Message):
    __slots__ = ("device_id", "zone_id")
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    device_id: _core_pb2.StringList
    zone_id: _core_pb2.StringList
    def __init__(
        self,
        device_id: _Optional[_Union[_core_pb2.StringList, _Mapping]] = ...,
        zone_id: _Optional[_Union[_core_pb2.StringList, _Mapping]] = ...,
    ) -> None: ...

class GetActiveAlertsResponse(_message.Message):
    __slots__ = ("alerts",)
    ALERTS_FIELD_NUMBER: _ClassVar[int]
    alerts: _containers.RepeatedCompositeFieldContainer[_alert_pb2.Alert]
    def __init__(
        self, alerts: _Optional[_Iterable[_Union[_alert_pb2.Alert, _Mapping]]] = ...
    ) -> None: ...

class DismissAlertsRequest(_message.Message):
    __slots__ = ("alert_ids", "device_id", "zone_id")
    ALERT_IDS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    alert_ids: _containers.RepeatedScalarFieldContainer[str]
    device_id: str
    zone_id: str
    def __init__(
        self,
        alert_ids: _Optional[_Iterable[str]] = ...,
        device_id: _Optional[str] = ...,
        zone_id: _Optional[str] = ...,
    ) -> None: ...

class DismissAlertsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateZoneFlowRequest(_message.Message):
    __slots__ = (
        "zone_id",
        "flow_metering_enabled",
        "flow_auto_shut_off_enabled",
        "flow_high_threshold_pct",
        "flow_low_threshold_pct",
        "flow_baseline",
        "flow_calibration_result",
    )
    ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    FLOW_METERING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    FLOW_AUTO_SHUT_OFF_ENABLED_FIELD_NUMBER: _ClassVar[int]
    FLOW_HIGH_THRESHOLD_PCT_FIELD_NUMBER: _ClassVar[int]
    FLOW_LOW_THRESHOLD_PCT_FIELD_NUMBER: _ClassVar[int]
    FLOW_BASELINE_FIELD_NUMBER: _ClassVar[int]
    FLOW_CALIBRATION_RESULT_FIELD_NUMBER: _ClassVar[int]
    zone_id: str
    flow_metering_enabled: _wrappers_pb2.BoolValue
    flow_auto_shut_off_enabled: _wrappers_pb2.BoolValue
    flow_high_threshold_pct: _wrappers_pb2.DoubleValue
    flow_low_threshold_pct: _wrappers_pb2.DoubleValue
    flow_baseline: _wrappers_pb2.DoubleValue
    flow_calibration_result: _irrigation_controller_pb2.FlowCalibrationResultWrapper
    def __init__(
        self,
        zone_id: _Optional[str] = ...,
        flow_metering_enabled: _Optional[
            _Union[_wrappers_pb2.BoolValue, _Mapping]
        ] = ...,
        flow_auto_shut_off_enabled: _Optional[
            _Union[_wrappers_pb2.BoolValue, _Mapping]
        ] = ...,
        flow_high_threshold_pct: _Optional[
            _Union[_wrappers_pb2.DoubleValue, _Mapping]
        ] = ...,
        flow_low_threshold_pct: _Optional[
            _Union[_wrappers_pb2.DoubleValue, _Mapping]
        ] = ...,
        flow_baseline: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ...,
        flow_calibration_result: _Optional[
            _Union[_irrigation_controller_pb2.FlowCalibrationResultWrapper, _Mapping]
        ] = ...,
    ) -> None: ...

class UpdateZoneFlowResponse(_message.Message):
    __slots__ = ("zone",)
    ZONE_FIELD_NUMBER: _ClassVar[int]
    zone: _zone_pb2.ZoneDetail
    def __init__(
        self, zone: _Optional[_Union[_zone_pb2.ZoneDetail, _Mapping]] = ...
    ) -> None: ...

class CopyIrrigationControllerRequest(_message.Message):
    __slots__ = ("source_device_id", "destination_device_id")
    SOURCE_DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    source_device_id: str
    destination_device_id: str
    def __init__(
        self,
        source_device_id: _Optional[str] = ...,
        destination_device_id: _Optional[str] = ...,
    ) -> None: ...

class CopyIrrigationControllerResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetDeviceFeaturesRequest(_message.Message):
    __slots__ = ("device_id",)
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    def __init__(self, device_id: _Optional[str] = ...) -> None: ...

class GetDeviceFeaturesResponse(_message.Message):
    __slots__ = ("features",)
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    features: _containers.RepeatedCompositeFieldContainer[_feature_pb2.Feature]
    def __init__(
        self,
        features: _Optional[_Iterable[_Union[_feature_pb2.Feature, _Mapping]]] = ...,
    ) -> None: ...

class GetLocationIdForDeviceRequest(_message.Message):
    __slots__ = ("device_id",)
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    def __init__(self, device_id: _Optional[str] = ...) -> None: ...

class GetLocationIdForDeviceResponse(_message.Message):
    __slots__ = ("location_id",)
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    location_id: str
    def __init__(self, location_id: _Optional[str] = ...) -> None: ...

class GetNetworkStateRequest(_message.Message):
    __slots__ = ("device_id",)
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    def __init__(self, device_id: _Optional[str] = ...) -> None: ...

class GetNetworkStateResponse(_message.Message):
    __slots__ = (
        "device_id",
        "pin",
        "rssi",
        "dns1",
        "dns2",
        "netmask",
        "gateway",
        "ip_address",
        "ssid",
        "band",
    )
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    PIN_FIELD_NUMBER: _ClassVar[int]
    RSSI_FIELD_NUMBER: _ClassVar[int]
    DNS1_FIELD_NUMBER: _ClassVar[int]
    DNS2_FIELD_NUMBER: _ClassVar[int]
    NETMASK_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SSID_FIELD_NUMBER: _ClassVar[int]
    BAND_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    pin: str
    rssi: int
    dns1: str
    dns2: str
    netmask: str
    gateway: str
    ip_address: str
    ssid: str
    band: str
    def __init__(
        self,
        device_id: _Optional[str] = ...,
        pin: _Optional[str] = ...,
        rssi: _Optional[int] = ...,
        dns1: _Optional[str] = ...,
        dns2: _Optional[str] = ...,
        netmask: _Optional[str] = ...,
        gateway: _Optional[str] = ...,
        ip_address: _Optional[str] = ...,
        ssid: _Optional[str] = ...,
        band: _Optional[str] = ...,
    ) -> None: ...

class AddDeviceFeatureRequest(_message.Message):
    __slots__ = ("device_id", "name", "group")
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    name: _feature_pb2.Feature.FeatureName
    group: _feature_pb2.Feature.FeatureGroup
    def __init__(
        self,
        device_id: _Optional[str] = ...,
        name: _Optional[_Union[_feature_pb2.Feature.FeatureName, str]] = ...,
        group: _Optional[_Union[_feature_pb2.Feature.FeatureGroup, str]] = ...,
    ) -> None: ...

class AddDeviceFeatureResponse(_message.Message):
    __slots__ = ("feature_added",)
    FEATURE_ADDED_FIELD_NUMBER: _ClassVar[int]
    feature_added: bool
    def __init__(self, feature_added: bool = ...) -> None: ...

class DebugFlowRequest(_message.Message):
    __slots__ = ("device_id", "duration")
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    duration: int
    def __init__(
        self, device_id: _Optional[str] = ..., duration: _Optional[int] = ...
    ) -> None: ...

class DebugFlowResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StopDebugFlowRequest(_message.Message):
    __slots__ = ("device_id",)
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    def __init__(self, device_id: _Optional[str] = ...) -> None: ...

class StopDebugFlowResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LastSeenControllerRequest(_message.Message):
    __slots__ = ("serial_number",)
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    serial_number: str
    def __init__(self, serial_number: _Optional[str] = ...) -> None: ...

class LastSeenControllerResponse(_message.Message):
    __slots__ = ("lastSeen",)
    LASTSEEN_FIELD_NUMBER: _ClassVar[int]
    lastSeen: _timestamp_pb2.Timestamp
    def __init__(
        self,
        lastSeen: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
    ) -> None: ...

class PingFlexNodesRequest(_message.Message):
    __slots__ = ("device_id",)
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    def __init__(self, device_id: _Optional[str] = ...) -> None: ...

class PingFlexNodesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AssignProvisionRequest(_message.Message):
    __slots__ = ("manufacturer", "model")
    MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    manufacturer: _provision_pb2.Manufacturer
    model: _irrigation_controller_pb2.IrrigationControllerModelType
    def __init__(
        self,
        manufacturer: _Optional[_Union[_provision_pb2.Manufacturer, str]] = ...,
        model: _Optional[
            _Union[_irrigation_controller_pb2.IrrigationControllerModelType, str]
        ] = ...,
    ) -> None: ...

class AssignProvisionResponse(_message.Message):
    __slots__ = ("provision",)
    PROVISION_FIELD_NUMBER: _ClassVar[int]
    provision: _provision_pb2.Provision
    def __init__(
        self, provision: _Optional[_Union[_provision_pb2.Provision, _Mapping]] = ...
    ) -> None: ...

class CountAvailableProvisionRequest(_message.Message):
    __slots__ = ("manufacturer", "model")
    MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    manufacturer: _provision_pb2.Manufacturer
    model: _irrigation_controller_pb2.IrrigationControllerModelType
    def __init__(
        self,
        manufacturer: _Optional[_Union[_provision_pb2.Manufacturer, str]] = ...,
        model: _Optional[
            _Union[_irrigation_controller_pb2.IrrigationControllerModelType, str]
        ] = ...,
    ) -> None: ...

class CountAvailableProvisionResponse(_message.Message):
    __slots__ = ("available",)
    AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    available: int
    def __init__(self, available: _Optional[int] = ...) -> None: ...

class SetLightBarSettingRequest(_message.Message):
    __slots__ = ("device_id", "light_bar_setting")
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    LIGHT_BAR_SETTING_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    light_bar_setting: _controller_state_pb2.ControllerState.LightBarSetting
    def __init__(
        self,
        device_id: _Optional[str] = ...,
        light_bar_setting: _Optional[
            _Union[_controller_state_pb2.ControllerState.LightBarSetting, str]
        ] = ...,
    ) -> None: ...

class SetLightBarSettingResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateZoneGroupRequest(_message.Message):
    __slots__ = (
        "device_id",
        "type",
        "name",
        "description",
        "area",
        "activity_level",
        "yard_health",
        "perimeter",
        "zone_ids",
    )
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    AREA_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    YARD_HEALTH_FIELD_NUMBER: _ClassVar[int]
    PERIMETER_FIELD_NUMBER: _ClassVar[int]
    ZONE_IDS_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    type: _zone_pb2.ZoneGroupType
    name: str
    description: _wrappers_pb2.StringValue
    area: _wrappers_pb2.DoubleValue
    activity_level: _irrigation_controller_pb2.ActivityLevelWrapper
    yard_health: _irrigation_controller_pb2.YardHealthWrapper
    perimeter: _wrappers_pb2.StringValue
    zone_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(
        self,
        device_id: _Optional[str] = ...,
        type: _Optional[_Union[_zone_pb2.ZoneGroupType, str]] = ...,
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
    ) -> None: ...

class CreateZoneGroupResponse(_message.Message):
    __slots__ = ("zone_group",)
    ZONE_GROUP_FIELD_NUMBER: _ClassVar[int]
    zone_group: _zone_pb2.ZoneGroup
    def __init__(
        self, zone_group: _Optional[_Union[_zone_pb2.ZoneGroup, _Mapping]] = ...
    ) -> None: ...

class UpdateZoneGroupRequest(_message.Message):
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
    id: str
    device_id: str
    type: _zone_pb2.ZoneGroupTypeWrapper
    name: _wrappers_pb2.StringValue
    description: _wrappers_pb2.StringValue
    area: _wrappers_pb2.DoubleValue
    activity_level: _irrigation_controller_pb2.ActivityLevelWrapper
    yard_health: _irrigation_controller_pb2.YardHealthWrapper
    perimeter: _wrappers_pb2.StringValue
    zone_ids: _core_pb2.StringList
    def __init__(
        self,
        id: _Optional[str] = ...,
        device_id: _Optional[str] = ...,
        type: _Optional[_Union[_zone_pb2.ZoneGroupTypeWrapper, _Mapping]] = ...,
        name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...,
        description: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...,
        area: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ...,
        activity_level: _Optional[
            _Union[_irrigation_controller_pb2.ActivityLevelWrapper, _Mapping]
        ] = ...,
        yard_health: _Optional[
            _Union[_irrigation_controller_pb2.YardHealthWrapper, _Mapping]
        ] = ...,
        perimeter: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...,
        zone_ids: _Optional[_Union[_core_pb2.StringList, _Mapping]] = ...,
    ) -> None: ...

class UpdateZoneGroupResponse(_message.Message):
    __slots__ = ("zone_group",)
    ZONE_GROUP_FIELD_NUMBER: _ClassVar[int]
    zone_group: _zone_pb2.ZoneGroup
    def __init__(
        self, zone_group: _Optional[_Union[_zone_pb2.ZoneGroup, _Mapping]] = ...
    ) -> None: ...

class ListZoneGroupsRequest(_message.Message):
    __slots__ = ("device_id",)
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    def __init__(self, device_id: _Optional[str] = ...) -> None: ...

class ListZoneGroupsResponse(_message.Message):
    __slots__ = ("zone_groups",)
    ZONE_GROUPS_FIELD_NUMBER: _ClassVar[int]
    zone_groups: _containers.RepeatedCompositeFieldContainer[_zone_pb2.ZoneGroup]
    def __init__(
        self,
        zone_groups: _Optional[_Iterable[_Union[_zone_pb2.ZoneGroup, _Mapping]]] = ...,
    ) -> None: ...

class GetZoneGroupRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetZoneGroupResponse(_message.Message):
    __slots__ = ("zone_group",)
    ZONE_GROUP_FIELD_NUMBER: _ClassVar[int]
    zone_group: _zone_pb2.ZoneGroup
    def __init__(
        self, zone_group: _Optional[_Union[_zone_pb2.ZoneGroup, _Mapping]] = ...
    ) -> None: ...

class DeleteZoneGroupRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DeleteZoneGroupResponse(_message.Message):
    __slots__ = ("deleted",)
    DELETED_FIELD_NUMBER: _ClassVar[int]
    deleted: bool
    def __init__(self, deleted: bool = ...) -> None: ...

class BirthGen1Request(_message.Message):
    __slots__ = ("serial_number", "user_id")
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    serial_number: str
    user_id: str
    def __init__(
        self, serial_number: _Optional[str] = ..., user_id: _Optional[str] = ...
    ) -> None: ...

class BirthGen1Response(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class UpgradeWeatherIntelligenceRequest(_message.Message):
    __slots__ = ("location_id",)
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    location_id: str
    def __init__(self, location_id: _Optional[str] = ...) -> None: ...

class UpgradeWeatherIntelligenceResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetExtendedWarrantyEligibilityRequest(_message.Message):
    __slots__ = ("user_id", "device_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    device_id: str
    def __init__(
        self, user_id: _Optional[str] = ..., device_id: _Optional[str] = ...
    ) -> None: ...

class GetExtendedWarrantyEligibilityResponse(_message.Message):
    __slots__ = ("extendedWarrantyEligibilityStatus", "purchaseUrl")
    class ExtendedWarrantyEligibilityStatus(
        int, metaclass=_enum_type_wrapper.EnumTypeWrapper
    ):
        __slots__ = ()
        INELIGIBLE: _ClassVar[
            GetExtendedWarrantyEligibilityResponse.ExtendedWarrantyEligibilityStatus
        ]
        ELIGIBLE: _ClassVar[
            GetExtendedWarrantyEligibilityResponse.ExtendedWarrantyEligibilityStatus
        ]
        ACTIVE: _ClassVar[
            GetExtendedWarrantyEligibilityResponse.ExtendedWarrantyEligibilityStatus
        ]

    INELIGIBLE: GetExtendedWarrantyEligibilityResponse.ExtendedWarrantyEligibilityStatus
    ELIGIBLE: GetExtendedWarrantyEligibilityResponse.ExtendedWarrantyEligibilityStatus
    ACTIVE: GetExtendedWarrantyEligibilityResponse.ExtendedWarrantyEligibilityStatus
    EXTENDEDWARRANTYELIGIBILITYSTATUS_FIELD_NUMBER: _ClassVar[int]
    PURCHASEURL_FIELD_NUMBER: _ClassVar[int]
    extendedWarrantyEligibilityStatus: (
        GetExtendedWarrantyEligibilityResponse.ExtendedWarrantyEligibilityStatus
    )
    purchaseUrl: str
    def __init__(
        self,
        extendedWarrantyEligibilityStatus: _Optional[
            _Union[
                GetExtendedWarrantyEligibilityResponse.ExtendedWarrantyEligibilityStatus,
                str,
            ]
        ] = ...,
        purchaseUrl: _Optional[str] = ...,
    ) -> None: ...

class UpdateDynamicCropCoefficientRequest(_message.Message):
    __slots__ = ("device_id", "zone_ids", "enabled")
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_IDS_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    zone_ids: _containers.RepeatedScalarFieldContainer[str]
    enabled: bool
    def __init__(
        self,
        device_id: _Optional[str] = ...,
        zone_ids: _Optional[_Iterable[str]] = ...,
        enabled: bool = ...,
    ) -> None: ...

class UpdateDynamicCropCoefficientResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
