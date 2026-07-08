from sfos.detection.recurring_transaction_detector import (
    RecurringTransactionDetector,
)


def test_detector_can_be_created():

    detector = RecurringTransactionDetector()

    assert detector is not None

from datetime import date

from sfos.transaction import Transaction
from sfos.detection.recurring_transaction_detector import (
    RecurringTransactionDetector,
)


def test_detector_accepts_transactions():

    detector = RecurringTransactionDetector()

    transactions = [
        Transaction(
            posting_date=date(2026, 1, 1),
            effective_date=date(2026, 1, 1),
            description="Netflix",
            amount=-19.99,
            balance=1000.00,
        )
    ]

    detector.load_transactions(transactions)

    assert len(detector.transactions) == 1

def test_detector_returns_no_candidates_initially():

    detector = RecurringTransactionDetector()

    detector.load_transactions([])

    candidates = detector.detect()

    assert candidates == []

from datetime import date

from sfos.transaction import Transaction


def test_detector_groups_transactions_by_description():

    detector = RecurringTransactionDetector()

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
            posting_date=date(2026, 1, 5),
            effective_date=date(2026, 1, 5),
            description="Spotify",
            amount=-11.99,
            balance=900,
        ),
    ]

    detector.load_transactions(transactions)

    groups = detector.group_by_description()

    assert len(groups) == 2
    assert len(groups["Netflix"]) == 2
    assert len(groups["Spotify"]) == 1

def test_detect_returns_recurring_descriptions():

    detector = RecurringTransactionDetector()

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
            posting_date=date(2026, 3, 1),
            effective_date=date(2026, 3, 1),
            description="Netflix",
            amount=-19.99,
            balance=960,
        ),
        Transaction(
            posting_date=date(2026, 1, 5),
            effective_date=date(2026, 1, 5),
            description="Spotify",
            amount=-11.99,
            balance=900,
        ),
    ]

    detector.load_transactions(transactions)

    candidates = detector.detect()

    assert len(candidates) == 1
    
    candidate = candidates[0]

    assert candidate.merchant == "Netflix"
    assert len(candidate.transactions) == 3

def test_normalize_description():

    detector = RecurringTransactionDetector()

    assert detector._normalize_description(
        "NETFLIX.COM"
    ) == "NETFLIX"

def test_grouping_uses_normalized_description():

    detector = RecurringTransactionDetector()

    transactions = [
        Transaction(
            posting_date=date(2026, 1, 1),
            effective_date=date(2026, 1, 1),
            description="NETFLIX",
            amount=-19.99,
            balance=1000,
        ),
        Transaction(
            posting_date=date(2026, 2, 1),
            effective_date=date(2026, 2, 1),
            description="NETFLIX.COM",
            amount=-19.99,
            balance=980,
        ),
    ]

    detector.load_transactions(transactions)

    groups = detector.group_by_description()

    assert len(groups) == 1
    assert len(groups["NETFLIX"]) == 2