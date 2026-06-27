"""
SFOS Financial Ledger

The Financial Ledger is the central repository of all financial
accounts used by the Stone Financial Operating System.
"""

from collections import defaultdict

from sfos.account_registry import AccountRegistry


class FinancialLedger:
    """Central ledger for all household financial accounts."""

    def __init__(self, registry_path: str):
        self.registry = AccountRegistry(registry_path)
        self.accounts = self.registry.accounts

    @property
    def active_accounts(self):
        """Return only active accounts."""
        return self.registry.active_accounts()

    @property
    def institutions(self):
        """Return all institutions."""
        return self.registry.institutions()

    def account_count(self) -> int:
        """Total number of accounts."""
        return len(self.accounts)

    def active_account_count(self) -> int:
        """Total number of active accounts."""
        return len(self.active_accounts)

    def accounts_by_institution(self):
        """Group accounts by institution."""
        groups = defaultdict(list)

        for _, row in self.accounts.iterrows():
            groups[row["Institution"]].append(row["Account"])

        return dict(groups)