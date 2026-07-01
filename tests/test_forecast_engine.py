from pathlib import Path

from sfos.forecast_engine import ForecastEngine


def test_forecast_runs():

    engine = ForecastEngine(
        current_balance=10000,
        registry_path=Path("data") / "recurring_cash_flow.csv",
    )

    forecast = engine.generate()

    assert forecast.ending_balance >= 0


def test_daily_balances():

    engine = ForecastEngine(
        current_balance=10000,
        registry_path=Path("data") / "recurring_cash_flow.csv",
    )

    forecast = engine.generate()

    assert len(forecast.daily_balances) == 30