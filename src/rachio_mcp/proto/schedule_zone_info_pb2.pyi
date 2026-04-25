from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ScheduleZoneInfo(_message.Message):
    __slots__ = ("device_id", "zone_id", "order_id", "watering_time", "flex_aggression_coefficient", "flex_runtime_coefficient")
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    WATERING_TIME_FIELD_NUMBER: _ClassVar[int]
    FLEX_AGGRESSION_COEFFICIENT_FIELD_NUMBER: _ClassVar[int]
    FLEX_RUNTIME_COEFFICIENT_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    zone_id: str
    order_id: int
    watering_time: int
    flex_aggression_coefficient: float
    flex_runtime_coefficient: float
    def __init__(self, device_id: _Optional[str] = ..., zone_id: _Optional[str] = ..., order_id: _Optional[int] = ..., watering_time: _Optional[int] = ..., flex_aggression_coefficient: _Optional[float] = ..., flex_runtime_coefficient: _Optional[float] = ...) -> None: ...
