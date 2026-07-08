from datetime import date

from sfos.detection.recurring_candidate import (
    RecurringCandidate,
)
from sfos.detection.recurring_pattern_analyzer import (
    RecurringPatternAnalyzer,
)
from sfos.transaction import Transaction


def test_analyzer_calculates_average_interval():

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
        intervals=[31, 30],
    )

    analyzer = RecurringPatternAnalyzer()

    analysis = analyzer.analyze(candidate)

    assert analysis.average_interval == 30.5

def test_analyzer_infers_monthly():

    candidate = RecurringCandidate(
        merchant="Netflix",
        transactions=[],
        intervals=[31, 30, 30, 31],
    )

    analyzer = RecurringPatternAnalyzer()

    analysis = analyzer.analyze(candidate)

    assert analysis.inferred_frequency == "Monthly"

def test_analyzer_calculates_minimum_and_maximum():

    candidate = RecurringCandidate(
        merchant="Netflix",
        transactions=[],
        intervals=[31, 30, 29, 31],
    )

    analyzer = RecurringPatternAnalyzer()

    analysis = analyzer.analyze(candidate)

    assert analysis.minimum_interval == 29
    assert analysis.maximum_interval == 31

def test_analyzer_calculates_standard_deviation():

    candidate = RecurringCandidate(
        merchant="Netflix",
        transactions=[],
        intervals=[31, 30, 29, 30],
    )

    analyzer = RecurringPatternAnalyzer()

    analysis = analyzer.analyze(candidate)

    assert analysis.standard_deviation is not None
    assert analysis.standard_deviation < 1.0

def test_highly_consistent_pattern_has_high_confidence():

    candidate = RecurringCandidate(
        merchant="Netflix",
        transactions=[],
        intervals=[30, 30, 31, 30],
    )

    analyzer = RecurringPatternAnalyzer()

    analysis = analyzer.analyze(candidate)

    assert analysis.confidence > 90

def test_irregular_pattern_has_low_confidence():

    candidate = RecurringCandidate(
        merchant="Starbucks",
        transactions=[],
        intervals=[1, 12, 4, 19],
    )

    analyzer = RecurringPatternAnalyzer()

    analysis = analyzer.analyze(candidate)

    assert analysis.confidence < 40