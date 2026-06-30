from datetime import date

from sfos.cash_forecast import CashForecast


def test_cash_forecast_creation():

    forecast = CashForecast(
        forecast_date=date.today(),
        opening_balance=1000.0,
        closing_balance=1200.0,
        lowest_balance=900.0,
        ending_balance=1200.0,
        low_cash_warning=False,
    )

    assert forecast.ending_balance == 1200.0