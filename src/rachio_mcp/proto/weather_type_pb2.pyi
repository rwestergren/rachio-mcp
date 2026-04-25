from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class WeatherType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CLEAR: _ClassVar[WeatherType]
    MOSTLY_SUNNY: _ClassVar[WeatherType]
    PARTLY_CLOUDY: _ClassVar[WeatherType]
    MOSTLY_CLOUDY: _ClassVar[WeatherType]
    OVERCAST: _ClassVar[WeatherType]
    RAIN: _ClassVar[WeatherType]
    SNOW: _ClassVar[WeatherType]
    SLEET: _ClassVar[WeatherType]
    WIND: _ClassVar[WeatherType]
    FOG: _ClassVar[WeatherType]
    THUNDER_STORM: _ClassVar[WeatherType]
CLEAR: WeatherType
MOSTLY_SUNNY: WeatherType
PARTLY_CLOUDY: WeatherType
MOSTLY_CLOUDY: WeatherType
OVERCAST: WeatherType
RAIN: WeatherType
SNOW: WeatherType
SLEET: WeatherType
WIND: WeatherType
FOG: WeatherType
THUNDER_STORM: WeatherType
