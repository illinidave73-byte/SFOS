from datetime import date

from sfos.schedule_rule import ScheduleRule


def test_schedule_rule():

    rule = ScheduleRule(
        rule_type="Biweekly",
        start_date=date(2026, 1, 1),
    )

    assert rule.interval == 1