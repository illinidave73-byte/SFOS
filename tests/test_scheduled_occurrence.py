from datetime import date

from sfos.scheduled_occurrence import ScheduledOccurrence


def test_occurrence():

    occurrence = ScheduledOccurrence(
        occurrence_date=date.today(),
        event_name="Payroll",
        amount=1000,
    )

    assert occurrence.amount == 1000