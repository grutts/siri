from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime, XmlTime

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


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
            "namespace": "http://www.ifopt.org.uk/ifopt",
            "required": True,
        },
    )
    end_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "EndTime",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )


@dataclass
class TimebandStructure(HalfOpenTimeRangeStructure):
    """
    Type for a timeband.
    """


@dataclass
class ValidityConditionStructure:
    """
    Type for a validity condition.

    :ivar from_date_time: The (inclusive) start date and time.
    :ivar to_date_time: The (inclusive) end time. If omitted, the range
        end is open-ended, that is, it should be interpreted as
        "forever".
    :ivar day_type: Day type for which timeband applies. If absent all
        day types in context.
    :ivar timebands: Any timebands which further qualify the validity
        condition.
    """

    from_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "FromDateTime",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
    to_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ToDateTime",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
    day_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "DayType",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
    timebands: List["ValidityConditionStructure.Timebands"] = field(
        default_factory=list,
        metadata={
            "name": "Timebands",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )

    @dataclass
    class Timebands:
        """
        :ivar timeband: Timeband during which element is available or in
            effect.
        """

        timeband: Optional[TimebandStructure] = field(
            default=None,
            metadata={
                "name": "Timeband",
                "type": "Element",
                "namespace": "http://www.ifopt.org.uk/ifopt",
                "required": True,
            },
        )


@dataclass
class ValidityConditionsStructure:
    """
    A collection of one or more validity conditions.

    :ivar validity_condition: Reference to the identifier of an
        administrative area.
    """

    validity_condition: List[ValidityConditionStructure] = field(
        default_factory=list,
        metadata={
            "name": "ValidityCondition",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
            "min_occurs": 1,
        },
    )
