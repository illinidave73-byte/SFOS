"""
SFOS Transaction Importer.
"""

from datetime import datetime
from pathlib import Path

import pandas as pd

from sfos.transaction import Transaction


class TransactionImporter:
    """Imports bank transaction CSV files."""

    def __init__(self, csv_path: str | Path):
        self.csv_path = Path(csv_path)

    def load(self) -> list[Transaction]:
        df = pd.read_csv(self.csv_path)
        
        # Keep only posted transactions
        df = df.dropna(subset=["Posting Date", "Balance"])

        transactions = []

        for _, row in df.iterrows():
            transactions.append(
                Transaction(
                    posting_date=pd.to_datetime(
                        row["Posting Date"]
                    ).date(),
                    effective_date=pd.to_datetime(
                        row["Effective Date"]
                    ).date(),
                    description=str(row["Description"]),
                    amount=float(row["Amount"]),
                    balance=float(row["Balance"]),
                    category=str(row.get("Category", "")),
                    transaction_type=str(row.get("Transaction Type", "")),
                )
            )

        return transactions