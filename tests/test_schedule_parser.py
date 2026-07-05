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

def test_parse_biweekly_thursday():

    parser = ScheduleParser()

    rule = parser.parse(
        frequency="Biweekly",
        day_rule="Every Other Thursday",
    )

    assert rule.rule_type == "Biweekly"
    assert rule.interval == 1
    assert rule.day_of_week == 3

def test_parse_semi_monthly():

    parser = ScheduleParser()

    rule = parser.parse(
        frequency="Biweekly",
        day_rule="15th and 30th of every month",
    )

    assert rule.rule_type == "SemiMonthly"
    assert rule.days_of_month == [15, 30]

def test_parse_annual_first_day_of_july():

    parser = ScheduleParser()

    rule = parser.parse(
        frequency="Annual",
        day_rule="First Day of July",
    )

    assert rule.rule_type == "Annual"
    assert rule.day_of_month == 1
    assert rule.start_date is None
    assert rule.month_of_year==7

def test_parse_every_other_month():

    parser = ScheduleParser()

    rule = parser.parse(
        frequency="every other month",
        day_rule="every two months on first of month",
    )

    assert rule.rule_type == "Monthly"
    assert rule.interval == 2
    assert rule.day_of_month == 1