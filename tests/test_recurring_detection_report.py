from sfos.detection.recurring_detection_report import (
    RecurringDetectionReport,
)


def test_report_can_be_created():

    report = RecurringDetectionReport()

    assert report is not None