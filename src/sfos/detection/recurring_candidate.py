"""
SFOS Recurring Candidate
"""

from dataclasses import dataclass

from sfos.transaction import Transaction


@dataclass(slots=True, kw_only=True)
class RecurringCandidate:
    """Represents a detected recurring transaction."""

    merchant: str
    transactions: list[Transaction]