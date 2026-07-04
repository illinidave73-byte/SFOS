from pathlib import Path

from sfos.forecast_pipeline import ForecastPipeline
from sfos.schedule_rule import ScheduleRule


def test_pipeline_loads_registry():

    pipeline = ForecastPipeline()

    rules = pipeline.generate(
        registry_path=Path("data") / "recurring_cash_flow.csv",
    )

    assert len(rules) > 0
    assert isinstance(rules[0], ScheduleRule)