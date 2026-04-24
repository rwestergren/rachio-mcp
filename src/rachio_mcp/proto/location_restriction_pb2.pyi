import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
import schedule_restriction_criteria_pb2 as _schedule_restriction_criteria_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LocationRestriction(_message.Message):
    __slots__ = ("location_id", "schedule_restriction_criteria", "created", "updated")
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_RESTRICTION_CRITERIA_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    location_id: str
    schedule_restriction_criteria: (
        _schedule_restriction_criteria_pb2.ScheduleRestrictionCriteria
    )
    created: _timestamp_pb2.Timestamp
    updated: _timestamp_pb2.Timestamp
    def __init__(
        self,
        location_id: _Optional[str] = ...,
        schedule_restriction_criteria: _Optional[
            _Union[
                _schedule_restriction_criteria_pb2.ScheduleRestrictionCriteria, _Mapping
            ]
        ] = ...,
        created: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        updated: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
    ) -> None: ...
