"""
SFOS Schedule Rule
"""

from dataclasses import dataclass

from sfos.base import BaseModel


@dataclass(slots=True, kw_only=True)
class ScheduleRule(BaseModel):
    """Defines how an event repeats."""

    rule_type: str

    start_date: object

    end_date: object | None = None

    interval: int = 1

    day_of_month: int | None = None

    day_of_week: int | None = None

    business_day_adjustment: str | None = None

    days_of_month: list[int] | None = None

    anchor_weekday: int | None = None