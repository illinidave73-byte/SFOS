from datetime import date

from sfos.recurring_cash_flow import RecurringCashFlow
from sfos.recurring_cash_flow_mapper import RecurringCashFlowMapper


def test_to_schedule_rule():

    cash_flow = RecurringCashFlow(
        event_id="I001",
        name="Payroll",
        flow_type="Income",
        amount=1000,
        frequency="Biweekly",
        day_rule="Every Other Thursday",
        next_date=date(2026, 1, 1),
        source_account="Checking",
        category="Income",
        priority="Critical",
        variable=False,
        active=True,
        auto_detect=True,
        tolerance_days=2,
    )

    mapper = RecurringCashFlowMapper()

    rule = mapper.to_schedule_rule(cash_flow)

    assert rule.rule_type == "Biweekly"
    assert rule.start_date is None