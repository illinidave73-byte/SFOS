"""
Stone Family Operating System

Application entry point.
"""

from pathlib import Path

from sfos.treasury import TreasuryEngine


def main():

    registry = Path("data") / "master_account_registry.csv"

    treasury = TreasuryEngine(
    registry,
    Path("data") / "firstmid_transactions.csv",
)

    summary = treasury.summary()

    print()
    print("=" * 50)
    print(" Stone Family Operating System")
    print(" Mission Control v0.1")
    print("=" * 50)
    print()

    print(f"Accounts        : {summary['accounts']}")
    print(f"Active Accounts : {summary['active_accounts']}")
    print(f"Institutions    : {summary['institutions']}")
    print()

    print(f"Cash            : ${summary['cash']:,.2f}")

    status = "LOW CASH" if summary["low_cash"] else "HEALTHY"

    print(f"Status          : {status}")

    print()
    print("=" * 50)
    print()


if __name__ == "__main__":
    main()