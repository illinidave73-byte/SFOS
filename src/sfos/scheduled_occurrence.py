"""
SFOS Scheduled Occurrence
"""

from dataclasses import dataclass
from datetime import date

from sfos.base import BaseModel


@dataclass(slots=True, kw_only=True)
class ScheduledOccurrence(BaseModel):
    """Represents one generated occurrence."""

    occurrence_date: date

    event_name: str

    amount: float | None = None

    priority: str = "Normal"

    category: str = ""

    source_account: str = ""

    metadata: dict | None = None

    def __post_init__(self):

        if self.metadata is None:
            self.metadata = {}