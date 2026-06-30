from pathlib import Path

from sfos.recurring_cash_flow_registry import RecurringCashFlowRegistry


def test_registry_loads():

    registry = RecurringCashFlowRegistry(
        Path("data") / "recurring_cash_flow.csv"
    )

    assert len(registry.events) > 0


def test_has_income():

    registry = RecurringCashFlowRegistry(
        Path("data") / "recurring_cash_flow.csv"
    )

    assert any(e.flow_type == "Income" for e in registry.events)