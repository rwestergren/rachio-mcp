from google.protobuf import wrappers_pb2 as _wrappers_pb2
import core_pb2 as _core_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ScheduleRestrictionCriteria(_message.Message):
    __slots__ = (
        "day_of_week_constraint",
        "odd_day_constraint",
        "minimum_interval_days",
        "minimum_interval_hours",
    )
    DAY_OF_WEEK_CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    ODD_DAY_CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_INTERVAL_DAYS_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_INTERVAL_HOURS_FIELD_NUMBER: _ClassVar[int]
    day_of_week_constraint: _containers.RepeatedScalarFieldContainer[
        _core_pb2.DayOfWeek
    ]
    odd_day_constraint: _core_pb2.OddDay
    minimum_interval_days: _wrappers_pb2.Int32Value
    minimum_interval_hours: _wrappers_pb2.Int32Value
    def __init__(
        self,
        day_of_week_constraint: _Optional[
            _Iterable[_Union[_core_pb2.DayOfWeek, str]]
        ] = ...,
        odd_day_constraint: _Optional[_Union[_core_pb2.OddDay, str]] = ...,
        minimum_interval_days: _Optional[
            _Union[_wrappers_pb2.Int32Value, _Mapping]
        ] = ...,
        minimum_interval_hours: _Optional[
            _Union[_wrappers_pb2.Int32Value, _Mapping]
        ] = ...,
    ) -> None: ...
