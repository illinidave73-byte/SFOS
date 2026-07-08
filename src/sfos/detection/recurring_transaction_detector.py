"""
SFOS Recurring Transaction Detector
"""
from sfos.detection.recurring_candidate import RecurringCandidate
from sfos.detection.recurring_pattern_analyzer import RecurringPatternAnalyzer
from sfos.detection.recurring_pattern_analyzer import (
    RecurringPatternAnalyzer,
)

class RecurringTransactionDetector:
    """Identifies recurring transactions from transaction history."""
    def __init__(self):
        self.transactions = []

    def load_transactions(self, transactions):
        self.transactions = transactions

    def detect(self):

        groups = self.group_by_description()

        analyzer = RecurringPatternAnalyzer()

        candidates = []

        for description, transactions in groups.items():

            if len(transactions) >= 3:

                candidate = RecurringCandidate(
                    merchant=description,
                    transactions=transactions,
                )

                candidate.calculate_intervals()

                candidate.analysis = analyzer.analyze(candidate)

                candidates.append(candidate)

        return candidates
    
    def group_by_description(self):

        groups = {}

        for transaction in self.transactions:

            merchant = self._normalize_description(
                    transaction.description
            )

            groups.setdefault(
                merchant,
                [],
            ).append(transaction)

        return groups
    
    def _normalize_description(self, description: str):

        return description.replace(".COM", "")