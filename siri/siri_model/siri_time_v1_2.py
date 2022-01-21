from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlDateTime, XmlTime

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ClosedTimeRangeStructure:
    """Type for a range of times.

    Both start and end time are required.

    :ivar start_time: The (inclusive) start time.
    :ivar end_time: The (inclusive) end time.
    """

    start_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    end_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "EndTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )


@dataclass
class ClosedTimestampRangeStructure:
    """Type for a range of date and times.

    Both start and end time are required.

    :ivar start_time: The (inclusive) start date and time.
    :ivar end_time: The (inclusive) end date and time.
    """

    start_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    end_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "EndTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )


class DayTypeEnumeration(Enum):
    """
    Values for Day Type TPEG pti_table 34.
    """

    PTI34_0 = "pti34_0"
    UNKNOWN = "unknown"
    PTI34_1 = "pti34_1"
    MONDAY = "monday"
    PTI34_2 = "pti34_2"
    TUESDAY = "tuesday"
    PTI34_3 = "pti34_3"
    WEDNESDAY = "wednesday"
    PTI34_4 = "pti34_4"
    THURSDAY = "thursday"
    PTI34_5 = "pti34_5"
    FRIDAY = "friday"
    PTI34_6 = "pti34_6"
    SATURDAY = "saturday"
    PTI34_7 = "pti34_7"
    SUNDAY = "sunday"
    PTI34_8 = "pti34_8"
    WEEKDAYS = "weekdays"
    PTI34_9 = "pti34_9"
    WEEKENDS = "weekends"
    PTI34_10 = "pti34_10"
    HOLIDAY = "holiday"
    PTI34_11 = "pti34_11"
    PUBLIC_HOLIDAY = "publicHoliday"
    PTI34_12 = "pti34_12"
    RELIGIOUS_HOLIDAY = "religiousHoliday"
    PTI34_13 = "pti34_13"
    FEDERAL_HOLIDAY = "federalHoliday"
    PTI34_14 = "pti34_14"
    REGIONAL_HOLIDAY = "regionalHoliday"
    PTI34_15 = "pti34_15"
    NATIONAL_HOLIDAY = "nationalHoliday"
    PTI34_16 = "pti34_16"
    MONDAY_TO_FRIDAY = "mondayToFriday"
    PTI34_17 = "pti34_17"
    MONDAY_TO_SATURDAY = "mondayToSaturday"
    PTI34_18 = "pti34_18"
    SUNDAYS_AND_PUBLIC_HOLIDAYS = "sundaysAndPublicHolidays"
    PTI34_19 = "pti34_19"
    SCHOOL_DAYS = "schoolDays"
    PTI34_20 = "pti34_20"
    EVERY_DAY = "everyDay"
    PTI34_255 = "pti34_255"
    UNDEFINED_DAY_TYPE = "undefinedDayType"


class DaysOfWeekEnumerationx(Enum):
    """
    Values for Day Type TPEG pti_table 34.
    """

    UNKNOWN = "unknown"
    MONDAY = "monday"
    TUESDAY = "tuesday"
    WEDNESDAY = "wednesday"
    THURSDAY = "thursday"
    FRIDAY = "friday"
    SATURDAY = "saturday"
    SUNDAY = "sunday"
    MONDAY_TO_FRIDAY = "mondayToFriday"
    MONDAY_TO_SATURDAY = "mondayToSaturday"
    WEEKDAYS = "weekdays"
    WEEKENDS = "weekends"


@dataclass
class HalfOpenTimeRangeStructure:
    """Type for a range of times.

    Start time must be specified, end time is optional.

    :ivar start_time: The (inclusive) start time.
    :ivar end_time: The (inclusive) end time. If omitted, the range end
        is open-ended, that is, it should be interpreted as "forever".
    """

    start_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    end_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "EndTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class HalfOpenTimestampRangeStructure:
    """Type for a range of date times.

    Start time must be specified, end time is optional.

    :ivar start_time: The (inclusive) start time stamp.
    :ivar end_time: The (inclusive) end time stamp. If omitted, the
        range end is open-ended, that is, it should be interpreted as
        "forever".
    """

    start_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    end_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "EndTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


class HolidayTypeEnumerationx(Enum):
    """
    Values for Day Type TPEG pti_table 34.
    """

    HOLIDAY = "holiday"
    PUBLIC_HOLIDAY = "publicHoliday"
    RELIGIOUS_HOLIDAY = "religiousHoliday"
    FEDERAL_HOLIDAY = "federalHoliday"
    REGIONAL_HOLIDAY = "regionalHoliday"
    NATIONAL_HOLIDAY = "nationalHoliday"
    SUNDAYS_AND_PUBLIC_HOLIDAYS = "sundaysAndPublicHolidays"
    SCHOOL_DAYS = "schoolDays"
    EVERY_DAY = "everyDay"
    UNDEFINED_DAY_TYPE = "undefinedDayType"


@dataclass
class DayType:
    """
    Tpeg DAY TYPE pti_table 34.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: DayTypeEnumeration = field(
        default=DayTypeEnumeration.EVERY_DAY,
        metadata={
            "required": True,
        },
    )
