"""
Account domain model.
"""

from dataclasses import dataclass
from enum import Enum

from sfos.base import BaseModel
from sfos.enums import AccountType
from sfos.institution import Institution


class Ownership(str, Enum):
    """Ownership of an account."""

    DAVE = "Dave"
    JANA = "Jana"
    JOINT = "Joint"


@dataclass(slots=True, kw_only=True)
class Account(BaseModel):
    """
    Represents a financial account.
    """

    institution: Institution
    account_type: AccountType

    official_name: str
    nickname: str

    ownership: Ownership

    balance: float = 0.0
    credit_limit: float = 0.0
    interest_rate: float = 0.0
    is_active: bool = True