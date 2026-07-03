"""
SFOS Cash Forecast Engine
"""

from datetime import timedelta

from sfos.cash_forecast import CashForecast



class ForecastEngine:
    """Generates a simple cash forecast."""

    def __init__(self, current_balance, days=30):
        self.current_balance = current_balance
        self.days = days

    def generate(self,occurrences):

        events = sorted(
            occurrences,
            key=lambda o: o.occurrence_date,
        )

        balance = self.current_balance

        opening = balance
        lowest = balance

        daily = []

        current_day = min(
            (e.occurrence_date for e in events),
            default=None
        )

        if current_day is None:
            current_day = None

        for _ in range(self.days):

            if current_day is not None:

                for event in events:

                    if event.occurrence_date == current_day:

                        if event.flow_type == "Income":
                            balance += event.amount
                        else:
                            balance -= event.amount # TODO(Issue #16): Restore flow_type handling after
                                                    # ScheduledOccurrence is extended with financial attributes.

            daily.append(balance)

            lowest = min(lowest, balance)

            if current_day is not None:
                current_day += timedelta(days=1)

        return CashForecast(
            forecast_date=current_day,
            opening_balance=opening,
            closing_balance=balance,
            lowest_balance=lowest,
            ending_balance=balance,
            low_cash_warning=lowest < 1000,
            daily_balances=daily,
        )