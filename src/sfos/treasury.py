"""
SFOS Treasury Engine

Provides a high-level view of household cash.
"""

from pathlib import Path

from sfos.ledger import FinancialLedger


class TreasuryEngine:
    """Treasury Engine."""

    LOW_CASH_WARNING = 1000.00

    def __init__(self, registry_path: str | Path):
        self.ledger = FinancialLedger(registry_path)

    def current_cash(self) -> float:
        """
        Placeholder until live balances are connected.

        Future versions will calculate this from checking and savings
        account balances.
        """
        return 0.0

    def low_cash_threshold(self) -> float:
        return self.LOW_CASH_WARNING

    def is_low_cash(self) -> bool:
        return self.current_cash() < self.LOW_CASH_WARNING

    def summary(self) -> dict:
        return {
            "accounts": self.ledger.account_count(),
            "active_accounts": self.ledger.active_account_count(),
            "institutions": len(self.ledger.institutions),
            "cash": self.current_cash(),
            "low_cash": self.is_low_cash(),
        }