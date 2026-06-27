"""
Base model for all SFOS domain objects.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, UTC
from uuid import uuid4


@dataclass(slots=True, kw_only=True)
class BaseModel:
    """
    Base class for all SFOS domain objects.

    Every business object receives:
    - unique identifier
    - creation timestamp
    - update timestamp
    """

    id: str = field(default_factory=lambda: str(uuid4()))
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime = field(default_factory=lambda: datetime.now(UTC))

    def touch(self) -> None:
        """Update the modified timestamp."""
        self.updated_at = datetime.now(UTC)