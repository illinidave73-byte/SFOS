"""
Common enumerations used throughout SFOS.
"""

from enum import Enum


class AccountType(str, Enum):
    """Supported financial account types."""

    CHECKING = "checking"
    SAVINGS = "savings"
    CREDIT_CARD = "credit_card"
    MORTGAGE = "mortgage"
    AUTO_LOAN = "auto_loan"
    INVESTMENT = "investment"
    RETIREMENT = "retirement"
    OTHER = "other"


class TransactionType(str, Enum):
    """Supported transaction types."""

    DEBIT = "debit"
    CREDIT = "credit"
    TRANSFER = "transfer"