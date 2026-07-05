from datetime import date

from sfos.schedule_rule import ScheduleRule


def test_extended_schedule_rule():

    rule = ScheduleRule(
        rule_type="Semi-Monthly",
        start_date=date(2026, 1, 1),
        days_of_month=[15, 30],
        business_day_adjustment="previous",
    )

    assert rule.days_of_month == [15, 30]
    assert rule.business_day_adjustment == "previous"

from sfos.schedule_rule import ScheduleRule


def test_schedule_rule_supports_month_of_year():

    rule = ScheduleRule(
        rule_type="Annual",
        start_date=None,
        day_of_month=1,
        month_of_year=7,
    )

    assert rule.month_of_year == 7