from datetime import date

from sfos.scheduled_occurrence import ScheduledOccurrence


def test_occurrence_metadata():

    event = ScheduledOccurrence(
        occurrence_date=date.today(),
        event_name="Payroll",
        amount=100,
        priority="Critical",
        category="Income",
        source_account="Checking",
    )

    assert event.priority == "Critical"
    assert event.category == "Income"
    assert event.source_account == "Checking"