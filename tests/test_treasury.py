from pathlib import Path

from sfos.treasury import TreasuryEngine


def test_engine_loads():

    engine = TreasuryEngine(
        Path("data") / "master_account_registry.csv"
    )

    assert engine.config.low_cash_threshold == 1000.0


def test_summary():

    engine = TreasuryEngine(
        Path("data") / "master_account_registry.csv"
    )

    summary = engine.summary()

    assert summary["accounts"] > 0
    assert summary["institutions"] > 0