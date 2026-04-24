from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ThresholdName(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IRRIGATION_CONTROLLER_PRECIPITATION: _ClassVar[ThresholdName]
    IRRIGATION_CONTROLLER_TEMPERATURE: _ClassVar[ThresholdName]
    IRRIGATION_CONTROLLER_WIND: _ClassVar[ThresholdName]

IRRIGATION_CONTROLLER_PRECIPITATION: ThresholdName
IRRIGATION_CONTROLLER_TEMPERATURE: ThresholdName
IRRIGATION_CONTROLLER_WIND: ThresholdName

class LocationThreshold(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: ThresholdName
    value: float
    def __init__(
        self,
        name: _Optional[_Union[ThresholdName, str]] = ...,
        value: _Optional[float] = ...,
    ) -> None: ...
