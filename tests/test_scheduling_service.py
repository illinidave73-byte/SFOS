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