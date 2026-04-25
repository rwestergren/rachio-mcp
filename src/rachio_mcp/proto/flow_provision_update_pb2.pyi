import flow_provision_model_pb2 as _flow_provision_model_pb2
import provision_pb2 as _provision_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdatePcbManufacturingFlowProvisionRequest(_message.Message):
    __slots__ = ("serial_number", "firmware_version")
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    serial_number: str
    firmware_version: str
    def __init__(self, serial_number: _Optional[str] = ..., firmware_version: _Optional[str] = ...) -> None: ...

class UpdateFlowAssemblyFlowProvisionRequest(_message.Message):
    __slots__ = ("serial_number",)
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    serial_number: str
    def __init__(self, serial_number: _Optional[str] = ...) -> None: ...

class UpdatePcbManufacturingFlowProvisionResponse(_message.Message):
    __slots__ = ("provision",)
    PROVISION_FIELD_NUMBER: _ClassVar[int]
    provision: _flow_provision_model_pb2.FlowProvision
    def __init__(self, provision: _Optional[_Union[_flow_provision_model_pb2.FlowProvision, _Mapping]] = ...) -> None: ...

class UpdateFlowAssemblyFlowProvisionResponse(_message.Message):
    __slots__ = ("provision",)
    PROVISION_FIELD_NUMBER: _ClassVar[int]
    provision: _flow_provision_model_pb2.FlowProvision
    def __init__(self, provision: _Optional[_Union[_flow_provision_model_pb2.FlowProvision, _Mapping]] = ...) -> None: ...
