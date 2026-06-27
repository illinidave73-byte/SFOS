"""
SFOS Transaction domain model.
"""

from dataclasses import dataclass
from datetime import date

from sfos.base import BaseModel


@dataclass(slots=True, kw_only=True)
class Transaction(BaseModel):
    """Represents a financial transaction."""

    posting_date: date
    effective_date: date

    description: str

    amount: float
    balance: float

    category: str = ""
    transaction_type: str = ""
    memo: str = ""