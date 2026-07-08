from pathlib import Path

from sfos.transaction_importer import TransactionImporter
from sfos.detection.recurring_transaction_detector import (
    RecurringTransactionDetector,
)


def test_detector_runs_on_real_transactions():

    importer = TransactionImporter(
        Path("data") / "firstmid_transactions.csv",
    )

    transactions = importer.load()

    detector = RecurringTransactionDetector()

    detector.load_transactions(transactions)

    candidates = detector.detect()

    assert isinstance(candidates, list)

    for candidate in candidates:
        print(candidate.merchant, len(candidate.transactions))