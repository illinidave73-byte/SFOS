"""
SFOS Cash Forecast domain model.
"""

from dataclasses import dataclass, field
from datetime import date

from sfos.base import BaseModel


@dataclass(slots=True, kw_only=True)
class CashForecast(BaseModel):
    """Represents a cash forecast."""

    forecast_date: date

    opening_balance: float

    closing_balance: float

    lowest_balance: float

    ending_balance: float

    low_cash_warning: bool

    daily_balances: list[float] = field(default_factory=list)

    warnings: list[str] = field(default_factory=list)