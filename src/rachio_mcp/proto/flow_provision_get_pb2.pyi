import flow_provision_model_pb2 as _flow_provision_model_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetFlowProvisionRequest(_message.Message):
    __slots__ = ("serial_number",)
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    serial_number: str
    def __init__(self, serial_number: _Optional[str] = ...) -> None: ...

class GetFlowProvisionResponse(_message.Message):
    __slots__ = ("provision",)
    PROVISION_FIELD_NUMBER: _ClassVar[int]
    provision: _flow_provision_model_pb2.FlowProvision
    def __init__(self, provision: _Optional[_Union[_flow_provision_model_pb2.FlowProvision, _Mapping]] = ...) -> None: ...

class GetFlowProvisionBinaryRequest(_message.Message):
    __slots__ = ("serial_number",)
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    serial_number: str
    def __init__(self, serial_number: _Optional[str] = ...) -> None: ...

class GetFlowProvisionBinaryResponse(_message.Message):
    __slots__ = ("mfg_config_bytes",)
    MFG_CONFIG_BYTES_FIELD_NUMBER: _ClassVar[int]
    mfg_config_bytes: _wrappers_pb2.BytesValue
    def __init__(self, mfg_config_bytes: _Optional[_Union[_wrappers_pb2.BytesValue, _Mapping]] = ...) -> None: ...

class AssignFlowProvisionRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AssignFlowProvisionResponse(_message.Message):
    __slots__ = ("provision",)
    PROVISION_FIELD_NUMBER: _ClassVar[int]
    provision: _flow_provision_model_pb2.FlowProvision
    def __init__(self, provision: _Optional[_Union[_flow_provision_model_pb2.FlowProvision, _Mapping]] = ...) -> None: ...
