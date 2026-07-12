"""
SFOS Schedule Rule Generator
"""

import statistics

from sfos.schedule_rule import ScheduleRule


class ScheduleRuleGenerator:
    """Generates ScheduleRule objects from recurring candidates."""

    def generate(self, candidate):

        if (
            candidate.analysis is None
            or candidate.analysis.confidence < 80
        ):
            return None

        frequency = candidate.analysis.inferred_frequency

        supported_frequencies = {
            "Weekly",
            "Biweekly",
            "Monthly",
            "Quarterly",
            "Annual",
        }

        if frequency not in supported_frequencies:
            return None

        start_date = None
        day_of_month = None

        if (
            frequency == "Monthly"
            and candidate.transactions
        ):
            posting_days = [
                transaction.posting_date.day
                for transaction in candidate.transactions
            ]

            day_of_month = round(
                statistics.median(posting_days)
            )

        if (
            frequency == "Biweekly"
            and candidate.transactions
        ):
            start_date = min(
                transaction.posting_date
                for transaction in candidate.transactions
            )

        return ScheduleRule(
            rule_type=frequency,
            start_date=start_date,
            day_of_month=day_of_month,
        )