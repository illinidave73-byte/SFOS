"""
SFOS Scheduling Service
"""

from calendar import monthrange
from datetime import timedelta

from sfos.schedule_rule import ScheduleRule
from sfos.scheduled_occurrence import ScheduledOccurrence


class SchedulingService:
    """Generates scheduled occurrences from scheduling rules."""

    def generate(
        self,
        rule: ScheduleRule,
        event_name: str,
        start_date,
        end_date,
        amount: float | None = None,
    ) -> list[ScheduledOccurrence]:

        occurrences: list[ScheduledOccurrence] = []

        current = max(rule.start_date, start_date)

        while current <= end_date:

            occurrences.append(
                ScheduledOccurrence(
                    occurrence_date=current,
                    event_name=event_name,
                    amount=amount,
                )
            )

            current = self._next_occurrence(current, rule)

            if current is None:
                break

        return occurrences

    def _next_occurrence(self, current, rule):

        rule_type = rule.rule_type.lower()

        if rule_type == "one-time":
            return None

        if rule_type == "weekly":
            return current + timedelta(weeks=rule.interval)

        if rule_type == "biweekly":
            return current + timedelta(weeks=2 * rule.interval)

        if rule_type == "monthly":
            return self._add_months(current, rule.interval)

        if rule_type == "quarterly":
            return self._add_months(current, 3 * rule.interval)

        if rule_type == "annual":
            return self._add_months(current, 12 * rule.interval)

        raise ValueError(f"Unsupported rule type: {rule.rule_type}")

    @staticmethod
    def _add_months(current, months):

        month = current.month - 1 + months
        year = current.year + month // 12
        month = month % 12 + 1

        day = min(
            current.day,
            monthrange(year, month)[1],
        )

        return current.replace(
            year=year,
            month=month,
            day=day,
        )