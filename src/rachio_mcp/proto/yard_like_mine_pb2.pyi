import datetime

import schedule_criteria_pb2 as _schedule_criteria_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class YardLikeMine(_message.Message):
    __slots__ = ("device_id", "primary_photo_id", "distance_from_my_yard", "green_score", "water_usage", "city", "state", "zone_photo_id", "updated", "is_updated")
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_PHOTO_ID_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_FROM_MY_YARD_FIELD_NUMBER: _ClassVar[int]
    GREEN_SCORE_FIELD_NUMBER: _ClassVar[int]
    WATER_USAGE_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ZONE_PHOTO_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    IS_UPDATED_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    primary_photo_id: str
    distance_from_my_yard: int
    green_score: float
    water_usage: float
    city: str
    state: str
    zone_photo_id: _containers.RepeatedScalarFieldContainer[str]
    updated: _timestamp_pb2.Timestamp
    is_updated: bool
    def __init__(self, device_id: _Optional[str] = ..., primary_photo_id: _Optional[str] = ..., distance_from_my_yard: _Optional[int] = ..., green_score: _Optional[float] = ..., water_usage: _Optional[float] = ..., city: _Optional[str] = ..., state: _Optional[str] = ..., zone_photo_id: _Optional[_Iterable[str]] = ..., updated: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., is_updated: bool = ...) -> None: ...
