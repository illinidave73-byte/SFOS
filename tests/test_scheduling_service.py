from datetime import date

from sfos.schedule_rule import ScheduleRule
from sfos.scheduling_service import SchedulingService


def test_one_time():

    service = SchedulingService()

    rule = ScheduleRule(
        rule_type="One-Time",
        start_date=date(2026, 1, 10),
    )

    events = service.generate(
        rule,
        "Test",
        "Expense",
        date(2026, 1, 1),
        date(2026, 1, 31),
    )

    assert len(events) == 1


def test_weekly():

    service = SchedulingService()

    rule = ScheduleRule(
        rule_type="Weekly",
        start_date=date(2026, 1, 1),
    )

    events = service.generate(
        rule,
        "Payroll",
        "Income",
        date(2026, 1, 1),
        date(2026, 1, 31),
    )

    assert len(events) == 5


def test_monthly():

    service = SchedulingService()

    rule = ScheduleRule(
        rule_type="Monthly",
        start_date=date(2026, 1, 15),
    )

    events = service.generate(
        rule,
        "Mortgage",
        "Expense",
        date(2026, 1, 1),
        date(2026, 3, 31),
    )

    assert len(events) == 3

from datetime import date


def test_generate_uses_forecast_start_when_rule_start_is_none():

    rule = ScheduleRule(
        rule_type="Monthly",
        start_date=None,
        interval=1,
    )

    service = SchedulingService()

    occurrences = service.generate(
        rule=rule,
        event_name="Test Event",
        flow_type="Expense",
        start_date=date(2026, 1, 1),
        end_date=date(2026, 1, 31),
        amount=100,
    )

    assert len(occurrences) > 0
    assert occurrences[0].occurrence_date == date(2026, 1, 1)

def test_semi_monthly():

    service = SchedulingService()

    rule = ScheduleRule(
        rule_type="SemiMonthly",
        start_date=date(2026, 1, 15),
        days_of_month=[15, 30],
    )

    events = service.generate(
        rule,
        "Jana Payroll",
        "Income",
        date(2026, 1, 1),
        date(2026, 2, 28),
    )

    assert len(events) == 4

    assert events[0].occurrence_date == date(2026, 1, 15)
    assert events[1].occurrence_date == date(2026, 1, 30)
    assert events[2].occurrence_date == date(2026, 2, 15)
    assert events[3].occurrence_date == date(2026, 2, 28)