from pathlib import Path

from sfos.forecast_pipeline import ForecastPipeline


def test_pipeline_loads_registry():

    pipeline = ForecastPipeline()

    forecast = pipeline.generate(
        registry_path=Path("data") / "recurring_cash_flow.csv",
        current_balance=8069.52,
    )

    assert forecast.opening_balance == 8069.52
    assert forecast.ending_balance >= 0
    assert len(forecast.daily_balances) == 30