from pathlib import Path

from sfos.transaction_importer import TransactionImporter


def test_transaction_import():

    importer = TransactionImporter(
        Path("data") / "firstmid_transactions.csv"
    )

    transactions = importer.load()

    assert len(transactions) > 0


def test_balance_loaded():

    importer = TransactionImporter(
        Path("data") / "firstmid_transactions.csv"
    )

    transactions = importer.load()

    assert transactions[-1].balance > 0