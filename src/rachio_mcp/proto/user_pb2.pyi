import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
import user_preference_pb2 as _user_preference_pb2
import core_pb2 as _core_pb2
import device_pb2 as _device_pb2
import auth_extension_pb2 as _auth_extension_pb2
import media_model_pb2 as _media_model_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EventTokenType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NO_TYPE_SUBMITTED: _ClassVar[EventTokenType]
    WEB: _ClassVar[EventTokenType]
    IOS: _ClassVar[EventTokenType]
    ANDROID: _ClassVar[EventTokenType]
    IOS_MQTT: _ClassVar[EventTokenType]
NO_TYPE_SUBMITTED: EventTokenType
WEB: EventTokenType
IOS: EventTokenType
ANDROID: EventTokenType
IOS_MQTT: EventTokenType

class User(_message.Message):
    __slots__ = ("id", "first_name", "last_name", "email_address", "preference", "created", "updated", "phone_number", "username", "pro", "role", "privacy_constraint", "membership", "photo_summary")
    class PrivacyConstraint(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[User.PrivacyConstraint]
        DO_NOT_USE_PII: _ClassVar[User.PrivacyConstraint]
    NONE: User.PrivacyConstraint
    DO_NOT_USE_PII: User.PrivacyConstraint
    class Membership(_message.Message):
        __slots__ = ("organization_id", "role", "member_id")
        class Role(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            TECH: _ClassVar[User.Membership.Role]
            ADMIN: _ClassVar[User.Membership.Role]
            OWNER: _ClassVar[User.Membership.Role]
        TECH: User.Membership.Role
        ADMIN: User.Membership.Role
        OWNER: User.Membership.Role
        ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
        ROLE_FIELD_NUMBER: _ClassVar[int]
        MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
        organization_id: str
        role: User.Membership.Role
        member_id: str
        def __init__(self, organization_id: _Optional[str] = ..., role: _Optional[_Union[User.Membership.Role, str]] = ..., member_id: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PRO_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    PRIVACY_CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    MEMBERSHIP_FIELD_NUMBER: _ClassVar[int]
    PHOTO_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    id: str
    first_name: str
    last_name: str
    email_address: str
    preference: _containers.RepeatedCompositeFieldContainer[_user_preference_pb2.UserPreference]
    created: _timestamp_pb2.Timestamp
    updated: _timestamp_pb2.Timestamp
    phone_number: str
    username: str
    pro: bool
    role: _containers.RepeatedScalarFieldContainer[_auth_extension_pb2.AuthRole]
    privacy_constraint: User.PrivacyConstraint
    membership: User.Membership
    photo_summary: _media_model_pb2.PhotoSummary
    def __init__(self, id: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., email_address: _Optional[str] = ..., preference: _Optional[_Iterable[_Union[_user_preference_pb2.UserPreference, _Mapping]]] = ..., created: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., phone_number: _Optional[str] = ..., username: _Optional[str] = ..., pro: bool = ..., role: _Optional[_Iterable[_Union[_auth_extension_pb2.AuthRole, str]]] = ..., privacy_constraint: _Optional[_Union[User.PrivacyConstraint, str]] = ..., membership: _Optional[_Union[User.Membership, _Mapping]] = ..., photo_summary: _Optional[_Union[_media_model_pb2.PhotoSummary, _Mapping]] = ...) -> None: ...

class EventToken(_message.Message):
    __slots__ = ("token", "user_id", "type")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    token: str
    user_id: str
    type: EventTokenType
    def __init__(self, token: _Optional[str] = ..., user_id: _Optional[str] = ..., type: _Optional[_Union[EventTokenType, str]] = ...) -> None: ...
