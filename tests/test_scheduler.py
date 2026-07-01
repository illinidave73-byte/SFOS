from datetime import date

from sfos.scheduler import SchedulingService


def test_weekly():

    scheduler = SchedulingService()

    dates = scheduler.occurrences(
        date(2026, 1, 1),
        date(2026, 1, 31),
        "Weekly",
    )

    assert len(dates) == 5


def test_biweekly():

    scheduler = SchedulingService()

    dates = scheduler.occurrences(
        date(2026, 1, 1),
        date(2026, 1, 31),
        "Biweekly",
    )

    assert len(dates) == 3


def test_one_time():

    scheduler = SchedulingService()

    dates = scheduler.occurrences(
        date(2026, 5, 10),
        date(2026, 5, 31),
        "One-Time",
    )

    assert len(dates) == 1