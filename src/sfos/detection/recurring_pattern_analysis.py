"""
SFOS Recurring Pattern Analysis
"""

from dataclasses import dataclass


@dataclass(slots=True, kw_only=True)
class RecurringPatternAnalysis:
    """Statistical analysis of a recurring transaction pattern."""

    average_interval: float | None = None
    minimum_interval: int | None = None
    maximum_interval: int | None = None
    standard_deviation: float | None = None

    inferred_frequency: str = "Unknown"

    confidence: float = 0.0