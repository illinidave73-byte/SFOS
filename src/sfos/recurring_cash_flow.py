"""
SFOS Recurring Cash Flow domain model.
"""

from dataclasses import dataclass
from datetime import date

from sfos.base import BaseModel


@dataclass(slots=True, kw_only=True)
class RecurringCashFlow(BaseModel):
    """Represents a recurring income or expense."""

    event_id: str
    name: str

    flow_type: str

    amount: float

    frequency: str

    day_rule: str

    next_date: date | None

    source_account: str

    category: str

    priority: str

    variable: bool

    active: bool

    auto_detect: bool

    tolerance_days: int

    notes: str = ""