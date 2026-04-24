import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
import device_pb2 as _device_pb2
import flow_provision_model_pb2 as _flow_provision_model_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LinkedSensor(_message.Message):
    __slots__ = (
        "id",
        "wiring_position",
        "make",
        "model",
        "kfactor",
        "offset",
        "enabled",
        "sensor_type",
        "created",
        "updated",
    )
    class LinkedSensorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RAIN: _ClassVar[LinkedSensor.LinkedSensorType]
        FLOW: _ClassVar[LinkedSensor.LinkedSensorType]

    RAIN: LinkedSensor.LinkedSensorType
    FLOW: LinkedSensor.LinkedSensorType
    ID_FIELD_NUMBER: _ClassVar[int]
    WIRING_POSITION_FIELD_NUMBER: _ClassVar[int]
    MAKE_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    KFACTOR_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    SENSOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    id: str
    wiring_position: _device_pb2.WiringPosition
    make: _wrappers_pb2.StringValue
    model: _wrappers_pb2.StringValue
    kfactor: _wrappers_pb2.DoubleValue
    offset: _wrappers_pb2.DoubleValue
    enabled: bool
    sensor_type: LinkedSensor.LinkedSensorType
    created: _timestamp_pb2.Timestamp
    updated: _timestamp_pb2.Timestamp
    def __init__(
        self,
        id: _Optional[str] = ...,
        wiring_position: _Optional[_Union[_device_pb2.WiringPosition, str]] = ...,
        make: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...,
        model: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...,
        kfactor: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ...,
        offset: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ...,
        enabled: bool = ...,
        sensor_type: _Optional[_Union[LinkedSensor.LinkedSensorType, str]] = ...,
        created: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        updated: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
    ) -> None: ...

class FlowSensor(_message.Message):
    __slots__ = ("id", "make", "model", "kfactor", "offset")
    ID_FIELD_NUMBER: _ClassVar[int]
    MAKE_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    KFACTOR_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    id: int
    make: str
    model: str
    kfactor: float
    offset: float
    def __init__(
        self,
        id: _Optional[int] = ...,
        make: _Optional[str] = ...,
        model: _Optional[str] = ...,
        kfactor: _Optional[float] = ...,
        offset: _Optional[float] = ...,
    ) -> None: ...

class NascentWirelessFlowSensor(_message.Message):
    __slots__ = ("serial_number", "mac_address", "model", "activated")
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    ACTIVATED_FIELD_NUMBER: _ClassVar[int]
    serial_number: str
    mac_address: str
    model: _flow_provision_model_pb2.FlowModel
    activated: bool
    def __init__(
        self,
        serial_number: _Optional[str] = ...,
        mac_address: _Optional[str] = ...,
        model: _Optional[_Union[_flow_provision_model_pb2.FlowModel, str]] = ...,
        activated: bool = ...,
    ) -> None: ...

class WirelessFlowSensor(_message.Message):
    __slots__ = (
        "id",
        "name",
        "mac_address",
        "serial_number",
        "pin",
        "location_id",
        "controller_id",
        "created",
        "updated",
    )
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    PIN_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    mac_address: str
    serial_number: str
    pin: str
    location_id: str
    controller_id: str
    created: _timestamp_pb2.Timestamp
    updated: _timestamp_pb2.Timestamp
    def __init__(
        self,
        id: _Optional[str] = ...,
        name: _Optional[str] = ...,
        mac_address: _Optional[str] = ...,
        serial_number: _Optional[str] = ...,
        pin: _Optional[str] = ...,
        location_id: _Optional[str] = ...,
        controller_id: _Optional[str] = ...,
        created: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        updated: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
    ) -> None: ...
