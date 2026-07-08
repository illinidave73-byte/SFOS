from sfos.detection.recurring_candidate import RecurringCandidate


def test_candidate_creation():

    candidate = RecurringCandidate(
        merchant="Netflix",
        transactions=[],
    )

    assert candidate.merchant == "Netflix"
    assert candidate.transactions == []

from datetime import date

from sfos.detection.recurring_candidate import RecurringCandidate
from sfos.transaction import Transaction


def test_candidate_can_store_intervals():

    transactions = [
        Transaction(
            posting_date=date(2026, 1, 1),
            effective_date=date(2026, 1, 1),
            description="Netflix",
            amount=-19.99,
            balance=1000,
        )
    ]

    candidate = RecurringCandidate(
        merchant="Netflix",
        transactions=transactions,
        intervals=[31, 28, 31],
    )

    assert candidate.intervals == [31, 28, 31]

from datetime import date

from sfos.detection.recurring_candidate import RecurringCandidate
from sfos.transaction import Transaction


def test_candidate_calculates_intervals():

    transactions = [
        Transaction(
            posting_date=date(2026, 1, 1),
            effective_date=date(2026, 1, 1),
            description="Netflix",
            amount=-19.99,
            balance=1000,
        ),
        Transaction(
            posting_date=date(2026, 2, 1),
            effective_date=date(2026, 2, 1),
            description="Netflix",
            amount=-19.99,
            balance=980,
        ),
        Transaction(
            posting_date=date(2026, 3, 3),
            effective_date=date(2026, 3, 3),
            description="Netflix",
            amount=-19.99,
            balance=960,
        ),
    ]

    candidate = RecurringCandidate(
        merchant="Netflix",
        transactions=transactions,
    )

    assert candidate.calculate_intervals() == [31, 30]

def test_candidate_average_interval():

    transactions = [
        Transaction(
            posting_date=date(2026, 1, 1),
            effective_date=date(2026, 1, 1),
            description="Netflix",
            amount=-19.99,
            balance=1000,
        ),
        Transaction(
            posting_date=date(2026, 2, 1),
            effective_date=date(2026, 2, 1),
            description="Netflix",
            amount=-19.99,
            balance=980,
        ),
        Transaction(
            posting_date=date(2026, 3, 3),
            effective_date=date(2026, 3, 3),
            description="Netflix",
            amount=-19.99,
            balance=960,
        ),
    ]

    candidate = RecurringCandidate(
        merchant="Netflix",
        transactions=transactions,
    )

    candidate.calculate_intervals()

    assert candidate.average_interval() == 30.5