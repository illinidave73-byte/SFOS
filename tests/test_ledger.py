from pathlib import Path

from sfos.ledger import FinancialLedger


def test_ledger_loads():

    ledger = FinancialLedger(
        Path("data") / "master_account_registry.csv"
    )

    assert ledger.account_count() > 0


def test_has_accounts():

    ledger = FinancialLedger(
        Path("data") / "master_account_registry.csv"
    )

    assert ledger.active_account_count() > 0


def test_has_fidelity():

    ledger = FinancialLedger(
        Path("data") / "master_account_registry.csv"
    )

    assert "Fidelity" in ledger.institutions