from pathlib import Path

from sfos.account_registry import AccountRegistry


def test_registry_loads():
    registry = AccountRegistry(
        Path("data") / "master_account_registry.csv"
    )

    assert len(registry.accounts) > 0


def test_has_fidelity():
    registry = AccountRegistry(
        Path("data") / "master_account_registry.csv"
    )

    assert "Fidelity" in registry.institutions()