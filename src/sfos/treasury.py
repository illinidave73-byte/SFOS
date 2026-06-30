"""
SFOS Treasury Engine
"""

from pathlib import Path

from sfos.ledger import FinancialLedger
from sfos.transaction_importer import TransactionImporter
from sfos.config import Configuration

class TreasuryEngine:

    LOW_CASH_WARNING = None

    def __init__(
        self,
        registry_path: str | Path,
        transaction_path: str | Path | None = None,
    ):
        self.ledger = FinancialLedger(registry_path)
        self.config = Configuration()

        self.transactions = []

        if transaction_path:
            importer = TransactionImporter(transaction_path)
            self.transactions = importer.load()

    def checking_balance(self) -> float:
        """
        Return the latest posted checking balance.
        """

        if not self.transactions:
            return 0.0

        return self.transactions[-1].balance

    def cash_position(self) -> float:
        """
        Current household cash.

        Today:
            Checking only

        Future:
            Checking + Savings + Money Market
        """
        return self.checking_balance()

    def is_low_cash(self) -> bool:
        return (
            self.cash_position()
            < self.config.low_cash_threshold
        )

    def summary(self):

        return {
            "accounts": self.ledger.account_count(),
            "active_accounts": self.ledger.active_account_count(),
            "institutions": len(self.ledger.institutions),
            "cash": self.cash_position(),
            "low_cash": self.is_low_cash(),
        }