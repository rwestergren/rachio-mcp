import core_pb2 as _core_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Interval(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MINUTE: _ClassVar[Interval]
    HOUR: _ClassVar[Interval]
    DAY: _ClassVar[Interval]
    WEEK: _ClassVar[Interval]
    MONTH: _ClassVar[Interval]
    YEAR: _ClassVar[Interval]

class Aggregation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SUM: _ClassVar[Aggregation]
    AVERAGE: _ClassVar[Aggregation]
    COUNT: _ClassVar[Aggregation]
    MINIMUM: _ClassVar[Aggregation]
    MAXIMUM: _ClassVar[Aggregation]

MINUTE: Interval
HOUR: Interval
DAY: Interval
WEEK: Interval
MONTH: Interval
YEAR: Interval
SUM: Aggregation
AVERAGE: Aggregation
COUNT: Aggregation
MINIMUM: Aggregation
MAXIMUM: Aggregation

class AggregationCriteria(_message.Message):
    __slots__ = ("time_frame", "interval", "aggregation")
    TIME_FRAME_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    AGGREGATION_FIELD_NUMBER: _ClassVar[int]
    time_frame: _core_pb2.TimestampInterval
    interval: Interval
    aggregation: Aggregation
    def __init__(
        self,
        time_frame: _Optional[_Union[_core_pb2.TimestampInterval, _Mapping]] = ...,
        interval: _Optional[_Union[Interval, str]] = ...,
        aggregation: _Optional[_Union[Aggregation, str]] = ...,
    ) -> None: ...

class Aggregate(_message.Message):
    __slots__ = ("time_frame", "value", "group")
    TIME_FRAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    time_frame: _core_pb2.TimestampInterval
    value: float
    group: str
    def __init__(
        self,
        time_frame: _Optional[_Union[_core_pb2.TimestampInterval, _Mapping]] = ...,
        value: _Optional[float] = ...,
        group: _Optional[str] = ...,
    ) -> None: ...
