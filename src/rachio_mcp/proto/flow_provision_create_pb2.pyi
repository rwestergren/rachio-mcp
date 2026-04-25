import flow_provision_model_pb2 as _flow_provision_model_pb2
import provision_pb2 as _provision_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateFlowProvisionRequest(_message.Message):
    __slots__ = ("serial_number", "pin", "mac_address", "key", "model", "status", "pcb_manufacturer", "final_assembly", "mfg_config_bytes", "type", "profile", "preamble_len", "interval", "resp_interval_num_wake", "use_ch_num", "ecpt_cnt_max", "crc_cnt_max", "wake_cnt_max", "hb_interval", "hb_timeout", "status_interval")
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    PIN_FIELD_NUMBER: _ClassVar[int]
    MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PCB_MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
    FINAL_ASSEMBLY_FIELD_NUMBER: _ClassVar[int]
    MFG_CONFIG_BYTES_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PROFILE_FIELD_NUMBER: _ClassVar[int]
    PREAMBLE_LEN_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    RESP_INTERVAL_NUM_WAKE_FIELD_NUMBER: _ClassVar[int]
    USE_CH_NUM_FIELD_NUMBER: _ClassVar[int]
    ECPT_CNT_MAX_FIELD_NUMBER: _ClassVar[int]
    CRC_CNT_MAX_FIELD_NUMBER: _ClassVar[int]
    WAKE_CNT_MAX_FIELD_NUMBER: _ClassVar[int]
    HB_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    HB_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    STATUS_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    serial_number: str
    pin: str
    mac_address: str
    key: str
    model: _flow_provision_model_pb2.FlowModel
    status: _provision_pb2.ProvisionStatus
    pcb_manufacturer: _provision_pb2.Manufacturer
    final_assembly: _flow_provision_model_pb2.FinalAssembly
    mfg_config_bytes: _wrappers_pb2.BytesValue
    type: int
    profile: int
    preamble_len: int
    interval: int
    resp_interval_num_wake: int
    use_ch_num: bool
    ecpt_cnt_max: int
    crc_cnt_max: int
    wake_cnt_max: int
    hb_interval: int
    hb_timeout: int
    status_interval: int
    def __init__(self, serial_number: _Optional[str] = ..., pin: _Optional[str] = ..., mac_address: _Optional[str] = ..., key: _Optional[str] = ..., model: _Optional[_Union[_flow_provision_model_pb2.FlowModel, str]] = ..., status: _Optional[_Union[_provision_pb2.ProvisionStatus, str]] = ..., pcb_manufacturer: _Optional[_Union[_provision_pb2.Manufacturer, str]] = ..., final_assembly: _Optional[_Union[_flow_provision_model_pb2.FinalAssembly, str]] = ..., mfg_config_bytes: _Optional[_Union[_wrappers_pb2.BytesValue, _Mapping]] = ..., type: _Optional[int] = ..., profile: _Optional[int] = ..., preamble_len: _Optional[int] = ..., interval: _Optional[int] = ..., resp_interval_num_wake: _Optional[int] = ..., use_ch_num: bool = ..., ecpt_cnt_max: _Optional[int] = ..., crc_cnt_max: _Optional[int] = ..., wake_cnt_max: _Optional[int] = ..., hb_interval: _Optional[int] = ..., hb_timeout: _Optional[int] = ..., status_interval: _Optional[int] = ...) -> None: ...

class CreateFlowProvisionResponse(_message.Message):
    __slots__ = ("provision",)
    PROVISION_FIELD_NUMBER: _ClassVar[int]
    provision: _flow_provision_model_pb2.FlowProvision
    def __init__(self, provision: _Optional[_Union[_flow_provision_model_pb2.FlowProvision, _Mapping]] = ...) -> None: ...
