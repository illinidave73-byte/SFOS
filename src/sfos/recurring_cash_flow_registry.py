"""
SFOS Recurring Cash Flow Registry.
"""

from pathlib import Path

import pandas as pd

from sfos.recurring_cash_flow import RecurringCashFlow


REQUIRED_COLUMNS = [
    "ID",
    "Name",
    "Type",
    "Amount",
    "Frequency",
    "Day Rule",
    "Next Date",
    "Source Account",
    "Category",
    "Priority",
    "Variable",
    "Active",
    "Auto Detect",
    "Tolerance Days",
]


class RecurringCashFlowRegistry:
    """Loads recurring cash flow events."""

    def __init__(self, csv_path: str | Path):
        self.csv_path = Path(csv_path)
        self.events = self._load()

    def _load(self) -> list[RecurringCashFlow]:

        df = pd.read_csv(self.csv_path)

        missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]

        if missing:
            raise ValueError(f"Missing columns: {missing}")

        events = []

        for _, row in df.iterrows():

            events.append(
                RecurringCashFlow(
                    event_id=row["ID"],
                    name=row["Name"],
                    flow_type=row["Type"],
                    amount=float(row["Amount"]),
                    frequency=row["Frequency"],
                    day_rule=row["Day Rule"],
                    next_date=None,
                    source_account=row["Source Account"],
                    category=row["Category"],
                    priority=row["Priority"],
                    variable=str(row["Variable"]).lower() == "yes",
                    active=str(row["Active"]).lower() == "yes",
                    auto_detect=str(row["Auto Detect"]).lower() == "yes",
                    tolerance_days=int(row["Tolerance Days"]),
                    notes=str(row.get("Notes", "")),
                )
            )

        return events