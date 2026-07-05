from sfos.detection.recurring_transaction_detector import (
    RecurringTransactionDetector,
)


def test_detector_can_be_created():

    detector = RecurringTransactionDetector()

    assert detector is not None