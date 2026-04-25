import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
import core_pb2 as _core_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProvisionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AVAILABLE: _ClassVar[ProvisionStatus]
    ASSIGNED: _ClassVar[ProvisionStatus]
    FAILED: _ClassVar[ProvisionStatus]
    CONSUMED: _ClassVar[ProvisionStatus]
    REMOVED: _ClassVar[ProvisionStatus]
    RETURN_STOCK: _ClassVar[ProvisionStatus]
    REFURB_STOCK: _ClassVar[ProvisionStatus]
    RECYCLED: _ClassVar[ProvisionStatus]
    PCBA_TESTED_FAILED: _ClassVar[ProvisionStatus]
    PCBA_TESTED_PASSED: _ClassVar[ProvisionStatus]

class Manufacturer(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CREATION: _ClassVar[Manufacturer]
    VERGENT: _ClassVar[Manufacturer]
    ASTEELFLASH: _ClassVar[Manufacturer]
    COMPUTIME_CN: _ClassVar[Manufacturer]
    COMPUTIME_MY: _ClassVar[Manufacturer]
AVAILABLE: ProvisionStatus
ASSIGNED: ProvisionStatus
FAILED: ProvisionStatus
CONSUMED: ProvisionStatus
REMOVED: ProvisionStatus
RETURN_STOCK: ProvisionStatus
REFURB_STOCK: ProvisionStatus
RECYCLED: ProvisionStatus
PCBA_TESTED_FAILED: ProvisionStatus
PCBA_TESTED_PASSED: ProvisionStatus
CREATION: Manufacturer
VERGENT: Manufacturer
ASTEELFLASH: Manufacturer
COMPUTIME_CN: Manufacturer
COMPUTIME_MY: Manufacturer

class Provision(_message.Message):
    __slots__ = ("serial_number", "pin", "status", "manufacturer", "mac", "model", "firmware_version", "pro", "weather_intelligence_plus", "homekit_pin", "test_status", "test_result", "manufacturing_date", "created", "updated", "qr_code_payload", "last_known_firmware_version", "refurbished_date")
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    PIN_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
    MAC_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    PRO_FIELD_NUMBER: _ClassVar[int]
    WEATHER_INTELLIGENCE_PLUS_FIELD_NUMBER: _ClassVar[int]
    HOMEKIT_PIN_FIELD_NUMBER: _ClassVar[int]
    TEST_STATUS_FIELD_NUMBER: _ClassVar[int]
    TEST_RESULT_FIELD_NUMBER: _ClassVar[int]
    MANUFACTURING_DATE_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    QR_CODE_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    LAST_KNOWN_FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    REFURBISHED_DATE_FIELD_NUMBER: _ClassVar[int]
    serial_number: str
    pin: str
    status: ProvisionStatus
    manufacturer: Manufacturer
    mac: _wrappers_pb2.StringValue
    model: str
    firmware_version: _wrappers_pb2.StringValue
    pro: bool
    weather_intelligence_plus: bool
    homekit_pin: str
    test_status: _wrappers_pb2.StringValue
    test_result: _wrappers_pb2.StringValue
    manufacturing_date: _timestamp_pb2.Timestamp
    created: _timestamp_pb2.Timestamp
    updated: _timestamp_pb2.Timestamp
    qr_code_payload: _wrappers_pb2.StringValue
    last_known_firmware_version: _wrappers_pb2.StringValue
    refurbished_date: _timestamp_pb2.Timestamp
    def __init__(self, serial_number: _Optional[str] = ..., pin: _Optional[str] = ..., status: _Optional[_Union[ProvisionStatus, str]] = ..., manufacturer: _Optional[_Union[Manufacturer, str]] = ..., mac: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., model: _Optional[str] = ..., firmware_version: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., pro: bool = ..., weather_intelligence_plus: bool = ..., homekit_pin: _Optional[str] = ..., test_status: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., test_result: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., manufacturing_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., qr_code_payload: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., last_known_firmware_version: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., refurbished_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
