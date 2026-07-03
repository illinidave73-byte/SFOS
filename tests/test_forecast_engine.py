from datetime import date

from sfos.scheduled_occurrence import ScheduledOccurrence

from sfos.forecast_engine import ForecastEngine


def test_forecast_runs():

    engine = ForecastEngine(
        current_balance=10000,
    )
    occurrences = [
        ScheduledOccurrence(
            occurrence_date=date(2026, 1, 1),
            event_name="Payroll",
            flow_type="Income",
            amount=1000,
        )
    ]
    forecast = engine.generate(occurrences)

    assert forecast.ending_balance >= 0


def test_daily_balances():

    engine = ForecastEngine(
        current_balance=10000,
    )

    occurrences = [
        ScheduledOccurrence(
            occurrence_date=date(2026, 1, 1),
            event_name="Payroll",
            flow_type="Income",
            amount=1000,
        )
    ]
    forecast = engine.generate(occurrences)

    assert len(forecast.daily_balances) == 30