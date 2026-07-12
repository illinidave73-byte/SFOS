from datetime import date

from sfos.transaction import Transaction

from sfos.detection.schedule_rule_generator import (
    ScheduleRuleGenerator,
)
from sfos.detection.recurring_candidate import (
    RecurringCandidate,
)
from sfos.detection.recurring_pattern_analysis import (
    RecurringPatternAnalysis,
)


def test_generator_can_be_created():

    generator = ScheduleRuleGenerator()

    assert generator is not None

def test_generator_creates_biweekly_rule():

    candidate = RecurringCandidate(
        merchant="Payroll",
        transactions=[],
    )

    candidate.analysis = RecurringPatternAnalysis(
        inferred_frequency="Biweekly",
        confidence=99,
    )

    generator = ScheduleRuleGenerator()

    rule = generator.generate(candidate)

    assert rule.rule_type == "Biweekly"

def test_generator_sets_monthly_day_of_month():

    transactions = [
        Transaction(
            posting_date=date(2026, 1, 5),
            effective_date=date(2026, 1, 5),
            description="Netflix",
            amount=-19.99,
            balance=1000,
        ),
        Transaction(
            posting_date=date(2026, 2, 5),
            effective_date=date(2026, 2, 5),
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

    assert rule.day_of_month == 5

def test_generator_sets_biweekly_start_date():

    transactions = [
        Transaction(
            posting_date=date(2026, 1, 2),
            effective_date=date(2026, 1, 2),
            description="Payroll",
            amount=5000.00,
            balance=10000,
        ),
        Transaction(
            posting_date=date(2026, 1, 16),
            effective_date=date(2026, 1, 16),
            description="Payroll",
            amount=5000.00,
            balance=15000,
        ),
        Transaction(
            posting_date=date(2026, 1, 30),
            effective_date=date(2026, 1, 30),
            description="Payroll",
            amount=5000.00,
            balance=20000,
        ),
    ]

    candidate = RecurringCandidate(
        merchant="Payroll",
        transactions=transactions,
    )

    candidate.analysis = RecurringPatternAnalysis(
        inferred_frequency="Biweekly",
        confidence=99,
    )

    generator = ScheduleRuleGenerator()

    rule = generator.generate(candidate)

    assert rule.start_date == date(2026, 1, 2)

def test_generator_rejects_low_confidence_candidate():

    candidate = RecurringCandidate(
        merchant="Culver's",
        transactions=[],
    )

    candidate.analysis = RecurringPatternAnalysis(
        inferred_frequency="Weekly",
        confidence=25,
    )

    generator = ScheduleRuleGenerator()

    rule = generator.generate(candidate)

    assert rule is None

def test_generator_rejects_irregular_frequency():

    candidate = RecurringCandidate(
        merchant="Amazon",
        transactions=[],
    )

    candidate.analysis = RecurringPatternAnalysis(
        inferred_frequency="Irregular",
        confidence=99,
    )

    generator = ScheduleRuleGenerator()

    rule = generator.generate(candidate)

    assert rule is None

def test_generator_sets_monthly_day_from_unsorted_transactions():

    transactions = [
        Transaction(
            posting_date=date(2026, 3, 5),
            effective_date=date(2026, 3, 5),
            description="Netflix",
            amount=-19.99,
            balance=960,
        ),
        Transaction(
            posting_date=date(2026, 1, 5),
            effective_date=date(2026, 1, 5),
            description="Netflix",
            amount=-19.99,
            balance=1000,
        ),
        Transaction(
            posting_date=date(2026, 2, 5),
            effective_date=date(2026, 2, 5),
            description="Netflix",
            amount=-19.99,
            balance=980,
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

    assert rule.day_of_month == 5

def test_generator_infers_representative_monthly_day():

    transactions = [
        Transaction(
            posting_date=date(2026, 4, 6),
            effective_date=date(2026, 4, 6),
            description="Netflix",
            amount=-19.99,
            balance=940,
        ),
        Transaction(
            posting_date=date(2026, 1, 5),
            effective_date=date(2026, 1, 5),
            description="Netflix",
            amount=-19.99,
            balance=1000,
        ),
        Transaction(
            posting_date=date(2026, 3, 5),
            effective_date=date(2026, 3, 5),
            description="Netflix",
            amount=-19.99,
            balance=960,
        ),
        Transaction(
            posting_date=date(2026, 2, 4),
            effective_date=date(2026, 2, 4),
            description="Netflix",
            amount=-19.99,
            balance=980,
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

    assert rule.day_of_month == 5

