from sfos.detection.recurring_pattern_analysis import (
    RecurringPatternAnalysis,
)


def test_pattern_analysis_creation():

    analysis = RecurringPatternAnalysis()

    assert analysis.average_interval is None
    assert analysis.minimum_interval is None
    assert analysis.maximum_interval is None
    assert analysis.inferred_frequency == "Unknown"
    assert analysis.confidence == 0.0