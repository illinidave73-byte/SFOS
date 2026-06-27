"""
SFOS Account Registry

Loads the Master Account Registry CSV.
"""

from pathlib import Path

import pandas as pd


REQUIRED_COLUMNS = [
    "ID",
    "Institution",
    "Account",
    "Type",
    "Category",
    "Owner",
    "Include in Net Worth",
    "Active",
]


class AccountRegistry:
    """Loads and validates the Master Account Registry."""

    def __init__(self, csv_path: str | Path):
        self.csv_path = Path(csv_path)
        self.accounts = self._load()

    def _load(self) -> pd.DataFrame:
        df = pd.read_csv(self.csv_path, header=1)

        # Remove blank Excel columns
        df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

        missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]

        if missing:
            raise ValueError(f"Missing required columns: {missing}")

        return df

    def active_accounts(self) -> pd.DataFrame:
        return self.accounts[self.accounts["Active"] == "Yes"]

    def institutions(self) -> list[str]:
        return sorted(self.accounts["Institution"].unique())