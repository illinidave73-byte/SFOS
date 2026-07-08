from pathlib import Path

from sfos.transaction_importer import TransactionImporter
from sfos.detection.recurring_transaction_detector import (
    RecurringTransactionDetector,
)
from sfos.detection.recurring_detection_report import (
    RecurringDetectionReport,
)


def main():

    importer = TransactionImporter(
        Path("data") / "firstmid_transactions.csv",
    )

    transactions = importer.load()

    detector = RecurringTransactionDetector()
    detector.load_transactions(transactions)

    candidates = detector.detect()

    report = RecurringDetectionReport()

    print(report.generate(candidates))


if __name__ == "__main__":
    main()