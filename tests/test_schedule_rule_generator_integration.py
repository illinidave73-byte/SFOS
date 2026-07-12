from datetime import date

from sfos.detection.recurring_candidate import (
    RecurringCandidate,
)
from sfos.detection.recurring_pattern_analysis import (
    RecurringPatternAnalysis,
)
from sfos.detection.schedule_rule_generator import (
    ScheduleRuleGenerator,
)
from sfos.scheduling_service import SchedulingService
from sfos.transaction import Transaction


def test_generated_monthly_rule_creates_forecast_occurrences():

    transactions = [
        Transaction(
            posting_date=date(2026, 1, 5),
            effective_date=date(2026, 1, 5),
            description="Netflix",
            amount=-19.99,
            balance=1000,
        ),
        Transaction(
            posting_date=date(2026, 2, 4),
            effective_date=date(2026, 2, 4),
            description="Netflix",
            amount=-19.99,
            balance=980,
        ),
        Transaction(
            posting_date=date(2026, 3, 5),
            effective_date=date(2026, 3, 5),
            description="Netflix",
            amount=-19.99,
            balance=960,
        ),
    ]

    candidate = RecurringCandidate(
        merchant="Netflix",
        transactions=transactions,
    )

    candidate.analysis = RecurringPatternAnalysis(
        inferred_frequency="Monthly",
        confidence=99,
    )

    generator = ScheduleRuleGenerator()

    rule = generator.generate(candidate)

    service = SchedulingService()

    events = service.generate(
        rule,
        "Netflix",
        "Expense",
        date(2026, 7, 1),
        date(2026, 7, 31),
    )

    assert len(events) == 1
    assert events[0].occurrence_date == date(2026, 7, 5)

def test_generated_biweekly_rule_creates_forecast_occurrences():

    transactions = [
        Transaction(
            posting_date=date(2026, 1, 2),
            effective_date=date(2026, 1, 2),
            description="Boeing Payroll",
            amount=5386.07,
            balance=10000,
        ),
        Transaction(
            posting_date=date(2026, 1, 16),
            effective_date=date(2026, 1, 16),
            description="Boeing Payroll",
            amount=5386.07,
            balance=15000,
        ),
        Transaction(
            posting_date=date(2026, 1, 30),
            effective_date=date(2026, 1, 30),
            description="Boeing Payroll",
            amount=5386.07,
            balance=20000,
        ),
    ]

    candidate = RecurringCandidate(
        merchant="Boeing Payroll",
        transactions=transactions,
    )

    candidate.analysis = RecurringPatternAnalysis(
        inferred_frequency="Biweekly",
        confidence=99,
    )

    generator = ScheduleRuleGenerator()

    rule = generator.generate(candidate)

    service = SchedulingService()

    events = service.generate(
        rule,
        "Boeing Payroll",
        "Income",
        date(2026, 7, 1),
        date(2026, 7, 31),
    )

    assert len(events) == 3

    assert events[0].occurrence_date == date(
        2026,
        7,
        3,
    )

    assert events[1].occurrence_date == date(
        2026,
        7,
        17,
    )

    assert events[2].occurrence_date == date(
        2026,
        7,
        31,
    )