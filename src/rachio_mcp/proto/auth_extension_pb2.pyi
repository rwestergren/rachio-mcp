from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class AuthRole(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NONE: _ClassVar[AuthRole]
    MANUFACTURER: _ClassVar[AuthRole]
    ADMIN: _ClassVar[AuthRole]
    MUNI_ADMIN: _ClassVar[AuthRole]
    USER: _ClassVar[AuthRole]
    PRO: _ClassVar[AuthRole]
    PRO_ADMIN: _ClassVar[AuthRole]
    PORTAL_ADMIN: _ClassVar[AuthRole]
    PORTAL_USER: _ClassVar[AuthRole]
    AUDITOR: _ClassVar[AuthRole]

NONE: AuthRole
MANUFACTURER: AuthRole
ADMIN: AuthRole
MUNI_ADMIN: AuthRole
USER: AuthRole
PRO: AuthRole
PRO_ADMIN: AuthRole
PORTAL_ADMIN: AuthRole
PORTAL_USER: AuthRole
AUDITOR: AuthRole
