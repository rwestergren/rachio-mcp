import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
import core_pb2 as _core_pb2
import alert_pb2 as _alert_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
import feature_pb2 as _feature_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FlowCalibrationResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CALIBRATION_SUCCESS: _ClassVar[FlowCalibrationResult]
    CALIBRATION_COMMUNICATION_ERROR: _ClassVar[FlowCalibrationResult]
    CALIBRATION_ZERO_READING: _ClassVar[FlowCalibrationResult]
    CALIBRATION_OVERFLOW: _ClassVar[FlowCalibrationResult]
    CALIBRATION_MANUAL: _ClassVar[FlowCalibrationResult]

class ActivityLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HIGH_ACTIVITY: _ClassVar[ActivityLevel]
    MEDIUM_ACTIVITY: _ClassVar[ActivityLevel]
    LOW_ACTIVITY: _ClassVar[ActivityLevel]

class YardHealth(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HEALTHY_YARD: _ClassVar[YardHealth]
    PATCHY_YARD: _ClassVar[YardHealth]
    BARE_YARD: _ClassVar[YardHealth]

class SoilType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SAND: _ClassVar[SoilType]
    LOAM: _ClassVar[SoilType]
    CLAY: _ClassVar[SoilType]
    LOAMY_SAND: _ClassVar[SoilType]
    SANDY_LOAM: _ClassVar[SoilType]
    CLAY_LOAM: _ClassVar[SoilType]
    SILTY_CLAY: _ClassVar[SoilType]

class CropType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COOL_SEASON_GRASS: _ClassVar[CropType]
    WARM_SEASON_GRASS: _ClassVar[CropType]
    SHRUBS: _ClassVar[CropType]
    PERENNIAL: _ClassVar[CropType]
    TREES: _ClassVar[CropType]
    ANNUAL: _ClassVar[CropType]
    XERISCAPE: _ClassVar[CropType]
    GARDEN: _ClassVar[CropType]
    FLOWER_BEDS: _ClassVar[CropType]

class NozzleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FIXED_SPRAY_HEAD: _ClassVar[NozzleType]
    ROTOR_HEAD: _ClassVar[NozzleType]
    ROTARY_NOZZLE: _ClassVar[NozzleType]
    EMITTER: _ClassVar[NozzleType]
    BUBBLER: _ClassVar[NozzleType]
    MISTER: _ClassVar[NozzleType]
    DRIPLINE: _ClassVar[NozzleType]
    K_RAIN: _ClassVar[NozzleType]
    HUNTER_MP_ROTATOR: _ClassVar[NozzleType]
    RAIN_BIRD_ROTARY_NOZZLE: _ClassVar[NozzleType]

class ExposureType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MOSTLY_SHADE: _ClassVar[ExposureType]
    LOTS_OF_SHADE: _ClassVar[ExposureType]
    SOME_SHADE: _ClassVar[ExposureType]
    LOTS_OF_SUN: _ClassVar[ExposureType]

class SlopeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ZERO_THREE: _ClassVar[SlopeType]
    FOUR_SIX: _ClassVar[SlopeType]
    SEVEN_TWELVE: _ClassVar[SlopeType]
    OVER_TWELVE: _ClassVar[SlopeType]

class IrrigationControllerModelType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GENERATION1_8ZONE: _ClassVar[IrrigationControllerModelType]
    GENERATION1_16ZONE: _ClassVar[IrrigationControllerModelType]
    GENERATION2_8ZONE: _ClassVar[IrrigationControllerModelType]
    GENERATION2_16ZONE: _ClassVar[IrrigationControllerModelType]
    VIRTUAL_8ZONE: _ClassVar[IrrigationControllerModelType]
    VIRTUAL_12ZONE: _ClassVar[IrrigationControllerModelType]
    VIRTUAL_16ZONE: _ClassVar[IrrigationControllerModelType]
    GENERATION3_4ZONE: _ClassVar[IrrigationControllerModelType]
    GENERATION3_6ZONE: _ClassVar[IrrigationControllerModelType]
    GENERATION3_8ZONE: _ClassVar[IrrigationControllerModelType]
    GENERATION3_10ZONE: _ClassVar[IrrigationControllerModelType]
    GENERATION3_12ZONE: _ClassVar[IrrigationControllerModelType]
    GENERATION3_14ZONE: _ClassVar[IrrigationControllerModelType]
    GENERATION3_16ZONE: _ClassVar[IrrigationControllerModelType]
    GENERATION3_4ZONE_USI: _ClassVar[IrrigationControllerModelType]
    GENERATION3_6ZONE_USI: _ClassVar[IrrigationControllerModelType]
    GENERATION3_8ZONE_USI: _ClassVar[IrrigationControllerModelType]
    GENERATION3_10ZONE_USI: _ClassVar[IrrigationControllerModelType]
    GENERATION3_12ZONE_USI: _ClassVar[IrrigationControllerModelType]
    GENERATION3_14ZONE_USI: _ClassVar[IrrigationControllerModelType]
    GENERATION3_16ZONE_USI: _ClassVar[IrrigationControllerModelType]
    GENERATION3_8ZONE_LITE: _ClassVar[IrrigationControllerModelType]
    GENERATION3_6ZONE_PRO: _ClassVar[IrrigationControllerModelType]
    GENERATION3_8ZONE_PRO: _ClassVar[IrrigationControllerModelType]
    GENERATION3_16ZONE_PRO: _ClassVar[IrrigationControllerModelType]
    GENERATION3_6ZONE_USI_PRO: _ClassVar[IrrigationControllerModelType]
    GENERATION3_8ZONE_USI_PRO: _ClassVar[IrrigationControllerModelType]
    GENERATION3_16ZONE_USI_PRO: _ClassVar[IrrigationControllerModelType]
    UNASSIGNED_GEN3: _ClassVar[IrrigationControllerModelType]

CALIBRATION_SUCCESS: FlowCalibrationResult
CALIBRATION_COMMUNICATION_ERROR: FlowCalibrationResult
CALIBRATION_ZERO_READING: FlowCalibrationResult
CALIBRATION_OVERFLOW: FlowCalibrationResult
CALIBRATION_MANUAL: FlowCalibrationResult
HIGH_ACTIVITY: ActivityLevel
MEDIUM_ACTIVITY: ActivityLevel
LOW_ACTIVITY: ActivityLevel
HEALTHY_YARD: YardHealth
PATCHY_YARD: YardHealth
BARE_YARD: YardHealth
SAND: SoilType
LOAM: SoilType
CLAY: SoilType
LOAMY_SAND: SoilType
SANDY_LOAM: SoilType
CLAY_LOAM: SoilType
SILTY_CLAY: SoilType
COOL_SEASON_GRASS: CropType
WARM_SEASON_GRASS: CropType
SHRUBS: CropType
PERENNIAL: CropType
TREES: CropType
ANNUAL: CropType
XERISCAPE: CropType
GARDEN: CropType
FLOWER_BEDS: CropType
FIXED_SPRAY_HEAD: NozzleType
ROTOR_HEAD: NozzleType
ROTARY_NOZZLE: NozzleType
EMITTER: NozzleType
BUBBLER: NozzleType
MISTER: NozzleType
DRIPLINE: NozzleType
K_RAIN: NozzleType
HUNTER_MP_ROTATOR: NozzleType
RAIN_BIRD_ROTARY_NOZZLE: NozzleType
MOSTLY_SHADE: ExposureType
LOTS_OF_SHADE: ExposureType
SOME_SHADE: ExposureType
LOTS_OF_SUN: ExposureType
ZERO_THREE: SlopeType
FOUR_SIX: SlopeType
SEVEN_TWELVE: SlopeType
OVER_TWELVE: SlopeType
GENERATION1_8ZONE: IrrigationControllerModelType
GENERATION1_16ZONE: IrrigationControllerModelType
GENERATION2_8ZONE: IrrigationControllerModelType
GENERATION2_16ZONE: IrrigationControllerModelType
VIRTUAL_8ZONE: IrrigationControllerModelType
VIRTUAL_12ZONE: IrrigationControllerModelType
VIRTUAL_16ZONE: IrrigationControllerModelType
GENERATION3_4ZONE: IrrigationControllerModelType
GENERATION3_6ZONE: IrrigationControllerModelType
GENERATION3_8ZONE: IrrigationControllerModelType
GENERATION3_10ZONE: IrrigationControllerModelType
GENERATION3_12ZONE: IrrigationControllerModelType
GENERATION3_14ZONE: IrrigationControllerModelType
GENERATION3_16ZONE: IrrigationControllerModelType
GENERATION3_4ZONE_USI: IrrigationControllerModelType
GENERATION3_6ZONE_USI: IrrigationControllerModelType
GENERATION3_8ZONE_USI: IrrigationControllerModelType
GENERATION3_10ZONE_USI: IrrigationControllerModelType
GENERATION3_12ZONE_USI: IrrigationControllerModelType
GENERATION3_14ZONE_USI: IrrigationControllerModelType
GENERATION3_16ZONE_USI: IrrigationControllerModelType
GENERATION3_8ZONE_LITE: IrrigationControllerModelType
GENERATION3_6ZONE_PRO: IrrigationControllerModelType
GENERATION3_8ZONE_PRO: IrrigationControllerModelType
GENERATION3_16ZONE_PRO: IrrigationControllerModelType
GENERATION3_6ZONE_USI_PRO: IrrigationControllerModelType
GENERATION3_8ZONE_USI_PRO: IrrigationControllerModelType
GENERATION3_16ZONE_USI_PRO: IrrigationControllerModelType
UNASSIGNED_GEN3: IrrigationControllerModelType

class NascentIrrigationController(_message.Message):
    __slots__ = (
        "serial_number",
        "mac_address",
        "model",
        "firmware_version",
        "homekit_pin",
        "activated",
        "default_firmware_version_url",
        "default_firmware_version",
        "activation_code_required",
        "program_id",
        "last_known_firmware_version",
    )
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    HOMEKIT_PIN_FIELD_NUMBER: _ClassVar[int]
    ACTIVATED_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_FIRMWARE_VERSION_URL_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    ACTIVATION_CODE_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    PROGRAM_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_KNOWN_FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    serial_number: str
    mac_address: str
    model: IrrigationControllerModelType
    firmware_version: _wrappers_pb2.StringValue
    homekit_pin: _wrappers_pb2.StringValue
    activated: bool
    default_firmware_version_url: _wrappers_pb2.StringValue
    default_firmware_version: _wrappers_pb2.StringValue
    activation_code_required: bool
    program_id: str
    last_known_firmware_version: _wrappers_pb2.StringValue
    def __init__(
        self,
        serial_number: _Optional[str] = ...,
        mac_address: _Optional[str] = ...,
        model: _Optional[_Union[IrrigationControllerModelType, str]] = ...,
        firmware_version: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...,
        homekit_pin: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...,
        activated: bool = ...,
        default_firmware_version_url: _Optional[
            _Union[_wrappers_pb2.StringValue, _Mapping]
        ] = ...,
        default_firmware_version: _Optional[
            _Union[_wrappers_pb2.StringValue, _Mapping]
        ] = ...,
        activation_code_required: bool = ...,
        program_id: _Optional[str] = ...,
        last_known_firmware_version: _Optional[
            _Union[_wrappers_pb2.StringValue, _Mapping]
        ] = ...,
    ) -> None: ...

class Gen1IrrigationController(_message.Message):
    __slots__ = (
        "id",
        "name",
        "geo_point",
        "location_id",
        "created",
        "updated",
        "zone_id",
        "mac_address",
        "model",
        "serial_number",
        "master_valve",
        "linked_sensor_wiring_position_one_id",
        "standby",
        "water_hammer",
        "agent_id",
        "external_plan_id",
        "pin",
        "weather_intelligence_plus",
        "wellpump_delay_active",
        "usda_hardiness_zone",
        "climate_region",
        "koppen",
    )
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    GEO_POINT_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    MASTER_VALVE_FIELD_NUMBER: _ClassVar[int]
    LINKED_SENSOR_WIRING_POSITION_ONE_ID_FIELD_NUMBER: _ClassVar[int]
    STANDBY_FIELD_NUMBER: _ClassVar[int]
    WATER_HAMMER_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    PIN_FIELD_NUMBER: _ClassVar[int]
    WEATHER_INTELLIGENCE_PLUS_FIELD_NUMBER: _ClassVar[int]
    WELLPUMP_DELAY_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    USDA_HARDINESS_ZONE_FIELD_NUMBER: _ClassVar[int]
    CLIMATE_REGION_FIELD_NUMBER: _ClassVar[int]
    KOPPEN_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    geo_point: _core_pb2.GeoPoint
    location_id: str
    created: _timestamp_pb2.Timestamp
    updated: _timestamp_pb2.Timestamp
    zone_id: _containers.RepeatedScalarFieldContainer[str]
    mac_address: str
    model: IrrigationControllerModelType
    serial_number: str
    master_valve: bool
    linked_sensor_wiring_position_one_id: str
    standby: bool
    water_hammer: bool
    agent_id: str
    external_plan_id: str
    pin: str
    weather_intelligence_plus: bool
    wellpump_delay_active: bool
    usda_hardiness_zone: _wrappers_pb2.StringValue
    climate_region: _wrappers_pb2.Int32Value
    koppen: _wrappers_pb2.StringValue
    def __init__(
        self,
        id: _Optional[str] = ...,
        name: _Optional[str] = ...,
        geo_point: _Optional[_Union[_core_pb2.GeoPoint, _Mapping]] = ...,
        location_id: _Optional[str] = ...,
        created: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        updated: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        zone_id: _Optional[_Iterable[str]] = ...,
        mac_address: _Optional[str] = ...,
        model: _Optional[_Union[IrrigationControllerModelType, str]] = ...,
        serial_number: _Optional[str] = ...,
        master_valve: bool = ...,
        linked_sensor_wiring_position_one_id: _Optional[str] = ...,
        standby: bool = ...,
        water_hammer: bool = ...,
        agent_id: _Optional[str] = ...,
        external_plan_id: _Optional[str] = ...,
        pin: _Optional[str] = ...,
        weather_intelligence_plus: bool = ...,
        wellpump_delay_active: bool = ...,
        usda_hardiness_zone: _Optional[
            _Union[_wrappers_pb2.StringValue, _Mapping]
        ] = ...,
        climate_region: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...,
        koppen: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...,
    ) -> None: ...

class Gen2IrrigationController(_message.Message):
    __slots__ = (
        "id",
        "name",
        "geo_point",
        "location_id",
        "created",
        "updated",
        "zone_id",
        "mac_address",
        "model",
        "serial_number",
        "master_valve",
        "linked_sensor_wiring_position_one_id",
        "linked_sensor_wiring_position_two_id",
        "standby",
        "water_hammer",
        "pin",
        "homekit_pin",
        "weather_intelligence_plus",
        "wellpump_delay_active",
        "usda_hardiness_zone",
        "climate_region",
        "koppen",
    )
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    GEO_POINT_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    MASTER_VALVE_FIELD_NUMBER: _ClassVar[int]
    LINKED_SENSOR_WIRING_POSITION_ONE_ID_FIELD_NUMBER: _ClassVar[int]
    LINKED_SENSOR_WIRING_POSITION_TWO_ID_FIELD_NUMBER: _ClassVar[int]
    STANDBY_FIELD_NUMBER: _ClassVar[int]
    WATER_HAMMER_FIELD_NUMBER: _ClassVar[int]
    PIN_FIELD_NUMBER: _ClassVar[int]
    HOMEKIT_PIN_FIELD_NUMBER: _ClassVar[int]
    WEATHER_INTELLIGENCE_PLUS_FIELD_NUMBER: _ClassVar[int]
    WELLPUMP_DELAY_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    USDA_HARDINESS_ZONE_FIELD_NUMBER: _ClassVar[int]
    CLIMATE_REGION_FIELD_NUMBER: _ClassVar[int]
    KOPPEN_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    geo_point: _core_pb2.GeoPoint
    location_id: str
    created: _timestamp_pb2.Timestamp
    updated: _timestamp_pb2.Timestamp
    zone_id: _containers.RepeatedScalarFieldContainer[str]
    mac_address: str
    model: IrrigationControllerModelType
    serial_number: str
    master_valve: bool
    linked_sensor_wiring_position_one_id: str
    linked_sensor_wiring_position_two_id: str
    standby: bool
    water_hammer: bool
    pin: str
    homekit_pin: str
    weather_intelligence_plus: bool
    wellpump_delay_active: bool
    usda_hardiness_zone: _wrappers_pb2.StringValue
    climate_region: _wrappers_pb2.Int32Value
    koppen: _wrappers_pb2.StringValue
    def __init__(
        self,
        id: _Optional[str] = ...,
        name: _Optional[str] = ...,
        geo_point: _Optional[_Union[_core_pb2.GeoPoint, _Mapping]] = ...,
        location_id: _Optional[str] = ...,
        created: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        updated: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        zone_id: _Optional[_Iterable[str]] = ...,
        mac_address: _Optional[str] = ...,
        model: _Optional[_Union[IrrigationControllerModelType, str]] = ...,
        serial_number: _Optional[str] = ...,
        master_valve: bool = ...,
        linked_sensor_wiring_position_one_id: _Optional[str] = ...,
        linked_sensor_wiring_position_two_id: _Optional[str] = ...,
        standby: bool = ...,
        water_hammer: bool = ...,
        pin: _Optional[str] = ...,
        homekit_pin: _Optional[str] = ...,
        weather_intelligence_plus: bool = ...,
        wellpump_delay_active: bool = ...,
        usda_hardiness_zone: _Optional[
            _Union[_wrappers_pb2.StringValue, _Mapping]
        ] = ...,
        climate_region: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...,
        koppen: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...,
    ) -> None: ...

class Gen3IrrigationController(_message.Message):
    __slots__ = (
        "id",
        "name",
        "geo_point",
        "location_id",
        "created",
        "updated",
        "zone_id",
        "mac_address",
        "model",
        "serial_number",
        "master_valve",
        "linked_sensor_wiring_position_one_id",
        "linked_sensor_wiring_position_two_id",
        "standby",
        "water_hammer",
        "pin",
        "homekit_pin",
        "weather_intelligence_plus",
        "wellpump_delay_active",
        "wireless_flow_sensor_id",
        "usda_hardiness_zone",
        "climate_region",
        "koppen",
    )
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    GEO_POINT_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    MASTER_VALVE_FIELD_NUMBER: _ClassVar[int]
    LINKED_SENSOR_WIRING_POSITION_ONE_ID_FIELD_NUMBER: _ClassVar[int]
    LINKED_SENSOR_WIRING_POSITION_TWO_ID_FIELD_NUMBER: _ClassVar[int]
    STANDBY_FIELD_NUMBER: _ClassVar[int]
    WATER_HAMMER_FIELD_NUMBER: _ClassVar[int]
    PIN_FIELD_NUMBER: _ClassVar[int]
    HOMEKIT_PIN_FIELD_NUMBER: _ClassVar[int]
    WEATHER_INTELLIGENCE_PLUS_FIELD_NUMBER: _ClassVar[int]
    WELLPUMP_DELAY_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    WIRELESS_FLOW_SENSOR_ID_FIELD_NUMBER: _ClassVar[int]
    USDA_HARDINESS_ZONE_FIELD_NUMBER: _ClassVar[int]
    CLIMATE_REGION_FIELD_NUMBER: _ClassVar[int]
    KOPPEN_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    geo_point: _core_pb2.GeoPoint
    location_id: str
    created: _timestamp_pb2.Timestamp
    updated: _timestamp_pb2.Timestamp
    zone_id: _containers.RepeatedScalarFieldContainer[str]
    mac_address: str
    model: IrrigationControllerModelType
    serial_number: str
    master_valve: bool
    linked_sensor_wiring_position_one_id: str
    linked_sensor_wiring_position_two_id: str
    standby: bool
    water_hammer: bool
    pin: str
    homekit_pin: str
    weather_intelligence_plus: bool
    wellpump_delay_active: bool
    wireless_flow_sensor_id: _containers.RepeatedScalarFieldContainer[str]
    usda_hardiness_zone: _wrappers_pb2.StringValue
    climate_region: _wrappers_pb2.Int32Value
    koppen: _wrappers_pb2.StringValue
    def __init__(
        self,
        id: _Optional[str] = ...,
        name: _Optional[str] = ...,
        geo_point: _Optional[_Union[_core_pb2.GeoPoint, _Mapping]] = ...,
        location_id: _Optional[str] = ...,
        created: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        updated: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        zone_id: _Optional[_Iterable[str]] = ...,
        mac_address: _Optional[str] = ...,
        model: _Optional[_Union[IrrigationControllerModelType, str]] = ...,
        serial_number: _Optional[str] = ...,
        master_valve: bool = ...,
        linked_sensor_wiring_position_one_id: _Optional[str] = ...,
        linked_sensor_wiring_position_two_id: _Optional[str] = ...,
        standby: bool = ...,
        water_hammer: bool = ...,
        pin: _Optional[str] = ...,
        homekit_pin: _Optional[str] = ...,
        weather_intelligence_plus: bool = ...,
        wellpump_delay_active: bool = ...,
        wireless_flow_sensor_id: _Optional[_Iterable[str]] = ...,
        usda_hardiness_zone: _Optional[
            _Union[_wrappers_pb2.StringValue, _Mapping]
        ] = ...,
        climate_region: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...,
        koppen: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...,
    ) -> None: ...

class VirtualIrrigationController(_message.Message):
    __slots__ = (
        "id",
        "name",
        "geo_point",
        "location_id",
        "created",
        "updated",
        "zone_id",
        "model",
        "serial_number",
        "usda_hardiness_zone",
        "climate_region",
        "koppen",
    )
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    GEO_POINT_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    USDA_HARDINESS_ZONE_FIELD_NUMBER: _ClassVar[int]
    CLIMATE_REGION_FIELD_NUMBER: _ClassVar[int]
    KOPPEN_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    geo_point: _core_pb2.GeoPoint
    location_id: str
    created: _timestamp_pb2.Timestamp
    updated: _timestamp_pb2.Timestamp
    zone_id: _containers.RepeatedScalarFieldContainer[str]
    model: IrrigationControllerModelType
    serial_number: str
    usda_hardiness_zone: _wrappers_pb2.StringValue
    climate_region: _wrappers_pb2.Int32Value
    koppen: _wrappers_pb2.StringValue
    def __init__(
        self,
        id: _Optional[str] = ...,
        name: _Optional[str] = ...,
        geo_point: _Optional[_Union[_core_pb2.GeoPoint, _Mapping]] = ...,
        location_id: _Optional[str] = ...,
        created: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        updated: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        zone_id: _Optional[_Iterable[str]] = ...,
        model: _Optional[_Union[IrrigationControllerModelType, str]] = ...,
        serial_number: _Optional[str] = ...,
        usda_hardiness_zone: _Optional[
            _Union[_wrappers_pb2.StringValue, _Mapping]
        ] = ...,
        climate_region: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...,
        koppen: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...,
    ) -> None: ...

class AppMessageBanner(_message.Message):
    __slots__ = ("id", "entity_id", "type", "title", "archived", "created", "updated")
    ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    id: str
    entity_id: str
    type: _alert_pb2.AlertType
    title: str
    archived: bool
    created: _timestamp_pb2.Timestamp
    updated: _timestamp_pb2.Timestamp
    def __init__(
        self,
        id: _Optional[str] = ...,
        entity_id: _Optional[str] = ...,
        type: _Optional[_Union[_alert_pb2.AlertType, str]] = ...,
        title: _Optional[str] = ...,
        archived: bool = ...,
        created: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        updated: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
    ) -> None: ...

class FlowCalibrationResultWrapper(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: FlowCalibrationResult
    def __init__(
        self, value: _Optional[_Union[FlowCalibrationResult, str]] = ...
    ) -> None: ...

class ActivityLevelWrapper(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: ActivityLevel
    def __init__(self, value: _Optional[_Union[ActivityLevel, str]] = ...) -> None: ...

class YardHealthWrapper(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: YardHealth
    def __init__(self, value: _Optional[_Union[YardHealth, str]] = ...) -> None: ...

class SoilTypeWrapper(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: SoilType
    def __init__(self, value: _Optional[_Union[SoilType, str]] = ...) -> None: ...

class CropTypeWrapper(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: CropType
    def __init__(self, value: _Optional[_Union[CropType, str]] = ...) -> None: ...

class NozzleTypeWrapper(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: NozzleType
    def __init__(self, value: _Optional[_Union[NozzleType, str]] = ...) -> None: ...

class ExposureTypeWrapper(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: ExposureType
    def __init__(self, value: _Optional[_Union[ExposureType, str]] = ...) -> None: ...

class SlopeTypeWrapper(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: SlopeType
    def __init__(self, value: _Optional[_Union[SlopeType, str]] = ...) -> None: ...

class IrrigationControllerProperties(_message.Message):
    __slots__ = ("device_id", "model", "name", "features")
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    model: IrrigationControllerModelType
    name: str
    features: _containers.RepeatedCompositeFieldContainer[_feature_pb2.Feature]
    def __init__(
        self,
        device_id: _Optional[str] = ...,
        model: _Optional[_Union[IrrigationControllerModelType, str]] = ...,
        name: _Optional[str] = ...,
        features: _Optional[_Iterable[_Union[_feature_pb2.Feature, _Mapping]]] = ...,
    ) -> None: ...
