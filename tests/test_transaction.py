from datetime import date

from sfos.transaction import Transaction


def test_transaction_creation():

    txn = Transaction(
        posting_date=date.today(),
        effective_date=date.today(),
        description="Test",
        amount=100.0,
        balance=1000.0,
    )

    assert txn.amount == 100.0
    assert txn.balance == 1000.0