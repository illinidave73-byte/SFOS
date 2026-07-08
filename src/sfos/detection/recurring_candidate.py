"""
SFOS Recurring Candidate
"""

from dataclasses import dataclass

from sfos.transaction import Transaction

from sfos.detection.recurring_pattern_analysis import (
    RecurringPatternAnalysis,
)

@dataclass(slots=True, kw_only=True)
class RecurringCandidate:
    """Represents a detected recurring transaction."""

    merchant: str
    transactions: list[Transaction]

    intervals: list[int] | None = None
    analysis: RecurringPatternAnalysis | None = None
    
    def calculate_intervals(self):

        ordered = sorted(
            self.transactions,
            key=lambda t: t.posting_date,
        )
        intervals = []

        for previous, current in zip(
            ordered,
            ordered[1:],
        ):
            intervals.append(
                (
                    current.posting_date
                    - previous.posting_date
                ).days
            )

        self.intervals = intervals

        return intervals
    
    def average_interval(self):

        if not self.intervals:
            return None
        
        return sum(self.intervals) / len(self.intervals)
    




