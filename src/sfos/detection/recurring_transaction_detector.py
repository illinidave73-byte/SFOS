"""
SFOS Recurring Transaction Detector
"""


class RecurringTransactionDetector:
    """Identifies recurring transactions from transaction history."""
    def __init__(self):
        self.transactions = []

    def load_transactions(self, transactions):
        self.transactions = transactions

    def detect(self):

        groups = self.group_by_description()

        candidates = []

        for description, transactions in groups.items():

            if len(transactions) >= 3:
                candidates.append(description)

        return candidates
    
    def group_by_description(self):

        groups = {}

        for transaction in self.transactions:

            groups.setdefault(
                transaction.description,
                [],
            ).append(transaction)

        return groups