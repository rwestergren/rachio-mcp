import feature_pb2 as _feature_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetFeaturesRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetFeaturesResponse(_message.Message):
    __slots__ = ("features",)
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    features: _containers.RepeatedCompositeFieldContainer[_feature_pb2.Feature]
    def __init__(
        self,
        features: _Optional[_Iterable[_Union[_feature_pb2.Feature, _Mapping]]] = ...,
    ) -> None: ...

class GetAllFeaturesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetAllFeaturesResponse(_message.Message):
    __slots__ = ("feature",)
    FEATURE_FIELD_NUMBER: _ClassVar[int]
    feature: _containers.RepeatedCompositeFieldContainer[_feature_pb2.Feature]
    def __init__(
        self,
        feature: _Optional[_Iterable[_Union[_feature_pb2.Feature, _Mapping]]] = ...,
    ) -> None: ...
