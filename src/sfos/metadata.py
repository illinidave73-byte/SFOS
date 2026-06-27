"""
Metadata definitions for SFOS domain objects.
"""

from dataclasses import dataclass, field
from datetime import UTC, datetime


@dataclass(slots=True)
class Metadata:
    """Common metadata shared by domain objects."""

    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime = field(default_factory=lambda: datetime.now(UTC))