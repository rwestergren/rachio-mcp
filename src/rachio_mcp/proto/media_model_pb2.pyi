import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Photo(_message.Message):
    __slots__ = (
        "id",
        "photo_type",
        "parent_id",
        "created",
        "updated",
        "share_permission_granted",
        "shared_primary",
        "stock",
    )
    class PhotoType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEVICE: _ClassVar[Photo.PhotoType]
        ZONE: _ClassVar[Photo.PhotoType]
        LOCATION: _ClassVar[Photo.PhotoType]
        USER: _ClassVar[Photo.PhotoType]
        YARD_JOURNAL: _ClassVar[Photo.PhotoType]
        VALVE: _ClassVar[Photo.PhotoType]
        LIGHTING_ZONE: _ClassVar[Photo.PhotoType]
        LIGHTING_ZONE_GROUP: _ClassVar[Photo.PhotoType]
        ORGANIZATION: _ClassVar[Photo.PhotoType]

    DEVICE: Photo.PhotoType
    ZONE: Photo.PhotoType
    LOCATION: Photo.PhotoType
    USER: Photo.PhotoType
    YARD_JOURNAL: Photo.PhotoType
    VALVE: Photo.PhotoType
    LIGHTING_ZONE: Photo.PhotoType
    LIGHTING_ZONE_GROUP: Photo.PhotoType
    ORGANIZATION: Photo.PhotoType
    ID_FIELD_NUMBER: _ClassVar[int]
    PHOTO_TYPE_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    SHARE_PERMISSION_GRANTED_FIELD_NUMBER: _ClassVar[int]
    SHARED_PRIMARY_FIELD_NUMBER: _ClassVar[int]
    STOCK_FIELD_NUMBER: _ClassVar[int]
    id: str
    photo_type: Photo.PhotoType
    parent_id: str
    created: _timestamp_pb2.Timestamp
    updated: _timestamp_pb2.Timestamp
    share_permission_granted: bool
    shared_primary: bool
    stock: bool
    def __init__(
        self,
        id: _Optional[str] = ...,
        photo_type: _Optional[_Union[Photo.PhotoType, str]] = ...,
        parent_id: _Optional[str] = ...,
        created: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        updated: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        share_permission_granted: bool = ...,
        shared_primary: bool = ...,
        stock: bool = ...,
    ) -> None: ...

class PhotoSummary(_message.Message):
    __slots__ = ("id", "default")
    ID_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_FIELD_NUMBER: _ClassVar[int]
    id: str
    default: bool
    def __init__(self, id: _Optional[str] = ..., default: bool = ...) -> None: ...
