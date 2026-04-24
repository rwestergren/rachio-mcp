import core_pb2 as _core_pb2
import irrigation_controller_pb2 as _irrigation_controller_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WateringEfficiency(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HIGH: _ClassVar[WateringEfficiency]
    OPTIMIZED: _ClassVar[WateringEfficiency]
    LOW: _ClassVar[WateringEfficiency]

HIGH: WateringEfficiency
OPTIMIZED: WateringEfficiency
LOW: WateringEfficiency

class KoppenClimate(_message.Message):
    __slots__ = ("koppen", "reduction_factor")
    KOPPEN_FIELD_NUMBER: _ClassVar[int]
    REDUCTION_FACTOR_FIELD_NUMBER: _ClassVar[int]
    koppen: str
    reduction_factor: float
    def __init__(
        self, koppen: _Optional[str] = ..., reduction_factor: _Optional[float] = ...
    ) -> None: ...

class MicroalgaeMeasurement(_message.Message):
    __slots__ = ("date", "level")
    DATE_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    date: _core_pb2.Date
    level: _wrappers_pb2.DoubleValue
    def __init__(
        self,
        date: _Optional[_Union[_core_pb2.Date, _Mapping]] = ...,
        level: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ...,
    ) -> None: ...

class VigorMeasurement(_message.Message):
    __slots__ = ("crop_type", "soil_temperature", "level", "description", "date")
    class DESCRIPTION(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DORMANT: _ClassVar[VigorMeasurement.DESCRIPTION]
        EMERGENT: _ClassVar[VigorMeasurement.DESCRIPTION]
        STRESSED: _ClassVar[VigorMeasurement.DESCRIPTION]
        SLOWING: _ClassVar[VigorMeasurement.DESCRIPTION]
        DECLINING: _ClassVar[VigorMeasurement.DESCRIPTION]
        HEALTHY: _ClassVar[VigorMeasurement.DESCRIPTION]
        THRIVING: _ClassVar[VigorMeasurement.DESCRIPTION]
        GROWING: _ClassVar[VigorMeasurement.DESCRIPTION]

    DORMANT: VigorMeasurement.DESCRIPTION
    EMERGENT: VigorMeasurement.DESCRIPTION
    STRESSED: VigorMeasurement.DESCRIPTION
    SLOWING: VigorMeasurement.DESCRIPTION
    DECLINING: VigorMeasurement.DESCRIPTION
    HEALTHY: VigorMeasurement.DESCRIPTION
    THRIVING: VigorMeasurement.DESCRIPTION
    GROWING: VigorMeasurement.DESCRIPTION
    CROP_TYPE_FIELD_NUMBER: _ClassVar[int]
    SOIL_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    crop_type: _irrigation_controller_pb2.CropType
    soil_temperature: _wrappers_pb2.DoubleValue
    level: _wrappers_pb2.DoubleValue
    description: VigorMeasurement.DESCRIPTION
    date: _core_pb2.Date
    def __init__(
        self,
        crop_type: _Optional[_Union[_irrigation_controller_pb2.CropType, str]] = ...,
        soil_temperature: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ...,
        level: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ...,
        description: _Optional[_Union[VigorMeasurement.DESCRIPTION, str]] = ...,
        date: _Optional[_Union[_core_pb2.Date, _Mapping]] = ...,
    ) -> None: ...

class SeasonNormals(_message.Message):
    __slots__ = (
        "mowing_start_day",
        "mowing_start_month",
        "mowing_end_day",
        "mowing_end_month",
        "planting_start_day",
        "planting_start_month",
        "freeze_start_day",
        "freeze_start_month",
        "freeze_end_day",
        "freeze_end_month",
        "irrigation_start_day",
        "irrigation_start_month",
        "irrigation_end_day",
        "irrigation_end_month",
        "microalgae_start_day",
        "microalgae_start_month",
        "winter_start_day",
        "winter_start_month",
        "winter_end_day",
        "winter_end_month",
        "spring_start_day",
        "spring_start_month",
        "spring_end_day",
        "spring_end_month",
        "summer_start_day",
        "summer_start_month",
        "summer_end_day",
        "summer_end_month",
        "fall_start_day",
        "fall_start_month",
        "fall_end_day",
        "fall_end_month",
    )
    MOWING_START_DAY_FIELD_NUMBER: _ClassVar[int]
    MOWING_START_MONTH_FIELD_NUMBER: _ClassVar[int]
    MOWING_END_DAY_FIELD_NUMBER: _ClassVar[int]
    MOWING_END_MONTH_FIELD_NUMBER: _ClassVar[int]
    PLANTING_START_DAY_FIELD_NUMBER: _ClassVar[int]
    PLANTING_START_MONTH_FIELD_NUMBER: _ClassVar[int]
    FREEZE_START_DAY_FIELD_NUMBER: _ClassVar[int]
    FREEZE_START_MONTH_FIELD_NUMBER: _ClassVar[int]
    FREEZE_END_DAY_FIELD_NUMBER: _ClassVar[int]
    FREEZE_END_MONTH_FIELD_NUMBER: _ClassVar[int]
    IRRIGATION_START_DAY_FIELD_NUMBER: _ClassVar[int]
    IRRIGATION_START_MONTH_FIELD_NUMBER: _ClassVar[int]
    IRRIGATION_END_DAY_FIELD_NUMBER: _ClassVar[int]
    IRRIGATION_END_MONTH_FIELD_NUMBER: _ClassVar[int]
    MICROALGAE_START_DAY_FIELD_NUMBER: _ClassVar[int]
    MICROALGAE_START_MONTH_FIELD_NUMBER: _ClassVar[int]
    WINTER_START_DAY_FIELD_NUMBER: _ClassVar[int]
    WINTER_START_MONTH_FIELD_NUMBER: _ClassVar[int]
    WINTER_END_DAY_FIELD_NUMBER: _ClassVar[int]
    WINTER_END_MONTH_FIELD_NUMBER: _ClassVar[int]
    SPRING_START_DAY_FIELD_NUMBER: _ClassVar[int]
    SPRING_START_MONTH_FIELD_NUMBER: _ClassVar[int]
    SPRING_END_DAY_FIELD_NUMBER: _ClassVar[int]
    SPRING_END_MONTH_FIELD_NUMBER: _ClassVar[int]
    SUMMER_START_DAY_FIELD_NUMBER: _ClassVar[int]
    SUMMER_START_MONTH_FIELD_NUMBER: _ClassVar[int]
    SUMMER_END_DAY_FIELD_NUMBER: _ClassVar[int]
    SUMMER_END_MONTH_FIELD_NUMBER: _ClassVar[int]
    FALL_START_DAY_FIELD_NUMBER: _ClassVar[int]
    FALL_START_MONTH_FIELD_NUMBER: _ClassVar[int]
    FALL_END_DAY_FIELD_NUMBER: _ClassVar[int]
    FALL_END_MONTH_FIELD_NUMBER: _ClassVar[int]
    mowing_start_day: _wrappers_pb2.Int32Value
    mowing_start_month: _wrappers_pb2.Int32Value
    mowing_end_day: _wrappers_pb2.Int32Value
    mowing_end_month: _wrappers_pb2.Int32Value
    planting_start_day: _wrappers_pb2.Int32Value
    planting_start_month: _wrappers_pb2.Int32Value
    freeze_start_day: _wrappers_pb2.Int32Value
    freeze_start_month: _wrappers_pb2.Int32Value
    freeze_end_day: _wrappers_pb2.Int32Value
    freeze_end_month: _wrappers_pb2.Int32Value
    irrigation_start_day: _wrappers_pb2.Int32Value
    irrigation_start_month: _wrappers_pb2.Int32Value
    irrigation_end_day: _wrappers_pb2.Int32Value
    irrigation_end_month: _wrappers_pb2.Int32Value
    microalgae_start_day: _wrappers_pb2.Int32Value
    microalgae_start_month: _wrappers_pb2.Int32Value
    winter_start_day: _wrappers_pb2.Int32Value
    winter_start_month: _wrappers_pb2.Int32Value
    winter_end_day: _wrappers_pb2.Int32Value
    winter_end_month: _wrappers_pb2.Int32Value
    spring_start_day: _wrappers_pb2.Int32Value
    spring_start_month: _wrappers_pb2.Int32Value
    spring_end_day: _wrappers_pb2.Int32Value
    spring_end_month: _wrappers_pb2.Int32Value
    summer_start_day: _wrappers_pb2.Int32Value
    summer_start_month: _wrappers_pb2.Int32Value
    summer_end_day: _wrappers_pb2.Int32Value
    summer_end_month: _wrappers_pb2.Int32Value
    fall_start_day: _wrappers_pb2.Int32Value
    fall_start_month: _wrappers_pb2.Int32Value
    fall_end_day: _wrappers_pb2.Int32Value
    fall_end_month: _wrappers_pb2.Int32Value
    def __init__(
        self,
        mowing_start_day: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...,
        mowing_start_month: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...,
        mowing_end_day: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...,
        mowing_end_month: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...,
        planting_start_day: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...,
        planting_start_month: _Optional[
            _Union[_wrappers_pb2.Int32Value, _Mapping]
        ] = ...,
        freeze_start_day: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...,
        freeze_start_month: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...,
        freeze_end_day: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...,
        freeze_end_month: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...,
        irrigation_start_day: _Optional[
            _Union[_wrappers_pb2.Int32Value, _Mapping]
        ] = ...,
        irrigation_start_month: _Optional[
            _Union[_wrappers_pb2.Int32Value, _Mapping]
        ] = ...,
        irrigation_end_day: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...,
        irrigation_end_month: _Optional[
            _Union[_wrappers_pb2.Int32Value, _Mapping]
        ] = ...,
        microalgae_start_day: _Optional[
            _Union[_wrappers_pb2.Int32Value, _Mapping]
        ] = ...,
        microalgae_start_month: _Optional[
            _Union[_wrappers_pb2.Int32Value, _Mapping]
        ] = ...,
        winter_start_day: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...,
        winter_start_month: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...,
        winter_end_day: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...,
        winter_end_month: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...,
        spring_start_day: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...,
        spring_start_month: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...,
        spring_end_day: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...,
        spring_end_month: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...,
        summer_start_day: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...,
        summer_start_month: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...,
        summer_end_day: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...,
        summer_end_month: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...,
        fall_start_day: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...,
        fall_start_month: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...,
        fall_end_day: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...,
        fall_end_month: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...,
    ) -> None: ...

class MowingMeasurement(_message.Message):
    __slots__ = ("interval_in_weeks", "height", "mowing_interval")
    class MowingInterval(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EVERY_WEEK: _ClassVar[MowingMeasurement.MowingInterval]
        EVERY_TWO_WEEKS: _ClassVar[MowingMeasurement.MowingInterval]
        EVERY_THREE_WEEKS: _ClassVar[MowingMeasurement.MowingInterval]
        INFREQUENTLY: _ClassVar[MowingMeasurement.MowingInterval]

    EVERY_WEEK: MowingMeasurement.MowingInterval
    EVERY_TWO_WEEKS: MowingMeasurement.MowingInterval
    EVERY_THREE_WEEKS: MowingMeasurement.MowingInterval
    INFREQUENTLY: MowingMeasurement.MowingInterval
    INTERVAL_IN_WEEKS_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    MOWING_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    interval_in_weeks: int
    height: _wrappers_pb2.DoubleValue
    mowing_interval: MowingMeasurement.MowingInterval
    def __init__(
        self,
        interval_in_weeks: _Optional[int] = ...,
        height: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ...,
        mowing_interval: _Optional[_Union[MowingMeasurement.MowingInterval, str]] = ...,
    ) -> None: ...

class WeeklyMeasurement(_message.Message):
    __slots__ = (
        "week_of_year",
        "recommended_average_watering_days",
        "recommended_watering_interval",
        "actual_average_watering_days",
        "actual_watering_interval",
    )
    class WateringInterval(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[WeeklyMeasurement.WateringInterval]
        BIWEEKLY: _ClassVar[WeeklyMeasurement.WateringInterval]
        UNDER_ONE_PER_WEEK: _ClassVar[WeeklyMeasurement.WateringInterval]
        ONE_PER_WEEK: _ClassVar[WeeklyMeasurement.WateringInterval]
        TWO_PER_WEEK: _ClassVar[WeeklyMeasurement.WateringInterval]
        THREE_PER_WEEK: _ClassVar[WeeklyMeasurement.WateringInterval]
        FOUR_PER_WEEK: _ClassVar[WeeklyMeasurement.WateringInterval]
        FIVE_PER_WEEK: _ClassVar[WeeklyMeasurement.WateringInterval]
        EVERY_DAY: _ClassVar[WeeklyMeasurement.WateringInterval]

    NONE: WeeklyMeasurement.WateringInterval
    BIWEEKLY: WeeklyMeasurement.WateringInterval
    UNDER_ONE_PER_WEEK: WeeklyMeasurement.WateringInterval
    ONE_PER_WEEK: WeeklyMeasurement.WateringInterval
    TWO_PER_WEEK: WeeklyMeasurement.WateringInterval
    THREE_PER_WEEK: WeeklyMeasurement.WateringInterval
    FOUR_PER_WEEK: WeeklyMeasurement.WateringInterval
    FIVE_PER_WEEK: WeeklyMeasurement.WateringInterval
    EVERY_DAY: WeeklyMeasurement.WateringInterval
    WEEK_OF_YEAR_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDED_AVERAGE_WATERING_DAYS_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDED_WATERING_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_AVERAGE_WATERING_DAYS_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_WATERING_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    week_of_year: int
    recommended_average_watering_days: float
    recommended_watering_interval: WeeklyMeasurement.WateringInterval
    actual_average_watering_days: float
    actual_watering_interval: WeeklyMeasurement.WateringInterval
    def __init__(
        self,
        week_of_year: _Optional[int] = ...,
        recommended_average_watering_days: _Optional[float] = ...,
        recommended_watering_interval: _Optional[
            _Union[WeeklyMeasurement.WateringInterval, str]
        ] = ...,
        actual_average_watering_days: _Optional[float] = ...,
        actual_watering_interval: _Optional[
            _Union[WeeklyMeasurement.WateringInterval, str]
        ] = ...,
    ) -> None: ...

class WateringEfficiencyWrapper(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: WateringEfficiency
    def __init__(
        self, value: _Optional[_Union[WateringEfficiency, str]] = ...
    ) -> None: ...

class WateringEfficiencyMeasurement(_message.Message):
    __slots__ = (
        "date",
        "delta_mm",
        "delta_mm_smoothed",
        "upper_threshold_mm",
        "lower_threshold_mm",
        "watering_efficiency",
    )
    DATE_FIELD_NUMBER: _ClassVar[int]
    DELTA_MM_FIELD_NUMBER: _ClassVar[int]
    DELTA_MM_SMOOTHED_FIELD_NUMBER: _ClassVar[int]
    UPPER_THRESHOLD_MM_FIELD_NUMBER: _ClassVar[int]
    LOWER_THRESHOLD_MM_FIELD_NUMBER: _ClassVar[int]
    WATERING_EFFICIENCY_FIELD_NUMBER: _ClassVar[int]
    date: _core_pb2.Date
    delta_mm: float
    delta_mm_smoothed: float
    upper_threshold_mm: float
    lower_threshold_mm: float
    watering_efficiency: WateringEfficiency
    def __init__(
        self,
        date: _Optional[_Union[_core_pb2.Date, _Mapping]] = ...,
        delta_mm: _Optional[float] = ...,
        delta_mm_smoothed: _Optional[float] = ...,
        upper_threshold_mm: _Optional[float] = ...,
        lower_threshold_mm: _Optional[float] = ...,
        watering_efficiency: _Optional[_Union[WateringEfficiency, str]] = ...,
    ) -> None: ...
