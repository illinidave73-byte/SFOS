from datetime import date

from sfos.schedule_parser import ScheduleParser


def test_parse_monthly_first():

    parser = ScheduleParser()

    rule = parser.parse(
        frequency="Monthly",
        day_rule="first of every month",
    )

    assert rule.rule_type == "Monthly"
    assert rule.day_of_month == 1

def test_parse_monthly_numeric_day():

    parser = ScheduleParser()

    rule = parser.parse(
        frequency="Monthly",
        day_rule="24th of every month",
    )

    assert rule.rule_type == "Monthly"
    assert rule.day_of_month == 24