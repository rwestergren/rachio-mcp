import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WebhookEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ZONE_STATUS: _ClassVar[WebhookEventType]
    SCHEDULE_STATUS: _ClassVar[WebhookEventType]
    DEVICE_STATUS: _ClassVar[WebhookEventType]
    RAIN_DELAY: _ClassVar[WebhookEventType]
    RAIN_SENSOR_DETECTION: _ClassVar[WebhookEventType]
    WEATHER_INTELLIGENCE: _ClassVar[WebhookEventType]
    ZONE_DELTA: _ClassVar[WebhookEventType]
    DELTA: _ClassVar[WebhookEventType]
ZONE_STATUS: WebhookEventType
SCHEDULE_STATUS: WebhookEventType
DEVICE_STATUS: WebhookEventType
RAIN_DELAY: WebhookEventType
RAIN_SENSOR_DETECTION: WebhookEventType
WEATHER_INTELLIGENCE: WebhookEventType
ZONE_DELTA: WebhookEventType
DELTA: WebhookEventType

class CreateWebhookRequest(_message.Message):
    __slots__ = ("id", "device_id", "url", "external_id", "event")
    ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    id: _wrappers_pb2.StringValue
    device_id: str
    url: str
    external_id: str
    event: _containers.RepeatedCompositeFieldContainer[WebhookEvent]
    def __init__(self, id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., device_id: _Optional[str] = ..., url: _Optional[str] = ..., external_id: _Optional[str] = ..., event: _Optional[_Iterable[_Union[WebhookEvent, _Mapping]]] = ...) -> None: ...

class CreateWebhookResponse(_message.Message):
    __slots__ = ("webhook",)
    WEBHOOK_FIELD_NUMBER: _ClassVar[int]
    webhook: Webhook
    def __init__(self, webhook: _Optional[_Union[Webhook, _Mapping]] = ...) -> None: ...

class UpdateWebhookRequest(_message.Message):
    __slots__ = ("id", "url", "external_id", "event")
    ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    id: str
    url: _wrappers_pb2.StringValue
    external_id: _wrappers_pb2.StringValue
    event: _containers.RepeatedCompositeFieldContainer[WebhookEvent]
    def __init__(self, id: _Optional[str] = ..., url: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., external_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., event: _Optional[_Iterable[_Union[WebhookEvent, _Mapping]]] = ...) -> None: ...

class UpdateWebhookResponse(_message.Message):
    __slots__ = ("webhook",)
    WEBHOOK_FIELD_NUMBER: _ClassVar[int]
    webhook: Webhook
    def __init__(self, webhook: _Optional[_Union[Webhook, _Mapping]] = ...) -> None: ...

class GetWebhookRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetWebhookResponse(_message.Message):
    __slots__ = ("webhook",)
    WEBHOOK_FIELD_NUMBER: _ClassVar[int]
    webhook: Webhook
    def __init__(self, webhook: _Optional[_Union[Webhook, _Mapping]] = ...) -> None: ...

class DeleteWebhookRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DeleteWebhookResponse(_message.Message):
    __slots__ = ("deleted",)
    DELETED_FIELD_NUMBER: _ClassVar[int]
    deleted: bool
    def __init__(self, deleted: bool = ...) -> None: ...

class Webhook(_message.Message):
    __slots__ = ("id", "device_id", "url", "external_id", "event", "created", "updated")
    ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    id: str
    device_id: str
    url: str
    external_id: str
    event: _containers.RepeatedCompositeFieldContainer[WebhookEvent]
    created: _timestamp_pb2.Timestamp
    updated: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., device_id: _Optional[str] = ..., url: _Optional[str] = ..., external_id: _Optional[str] = ..., event: _Optional[_Iterable[_Union[WebhookEvent, _Mapping]]] = ..., created: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class WebhookEvent(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: WebhookEventType
    def __init__(self, type: _Optional[_Union[WebhookEventType, str]] = ...) -> None: ...

class GetWebhooksForDeviceRequest(_message.Message):
    __slots__ = ("device_id",)
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    def __init__(self, device_id: _Optional[str] = ...) -> None: ...

class GetWebhooksForDeviceResponse(_message.Message):
    __slots__ = ("webhook",)
    WEBHOOK_FIELD_NUMBER: _ClassVar[int]
    webhook: _containers.RepeatedCompositeFieldContainer[Webhook]
    def __init__(self, webhook: _Optional[_Iterable[_Union[Webhook, _Mapping]]] = ...) -> None: ...
