from sfos.recurring_cash_flow import RecurringCashFlow


def test_recurring_cash_flow_creation():

    event = RecurringCashFlow(
        event_id="I001",
        name="Boeing Payroll",
        flow_type="Income",
        amount=5386.07,
        frequency="Biweekly",
        day_rule="Every Other Thursday",
        next_date=None,
        source_account="First Mid Checking",
        category="Income",
        priority="Critical",
        variable=False,
        active=True,
        auto_detect=True,
        tolerance_days=2,
    )

    assert event.amount == 5386.07
    assert event.active