"""
SFOS Scheduling Service
"""

from calendar import monthrange
from datetime import date, timedelta

from sfos.schedule_rule import ScheduleRule
from sfos.scheduled_occurrence import ScheduledOccurrence


class SchedulingService:
    """Generates scheduled occurrences from scheduling rules."""

    def generate(
        self,
        rule: ScheduleRule,
        event_name: str,
        flow_type: str, 
        start_date,
        end_date,
        amount: float | None = None,
        priority: str = "Normal",
        category: str = "",
        source_account: str = "",
    ) -> list[ScheduledOccurrence]:

        occurrences: list[ScheduledOccurrence] = []

        current = self._first_occurrence(
            rule=rule,
            forecast_start=start_date,
        )

        while current <= end_date:

            occurrences.append(
                ScheduledOccurrence(
                    occurrence_date=current,
                    event_name=event_name,
                    flow_type=flow_type, 
                    amount=amount,
                    priority=priority,
                    category=category,
                    source_account=source_account,
                )
            )

            current = self._next_occurrence(current, rule)

            if current is None:
                break

        return occurrences

    def _first_occurrence(
        self,
        rule: ScheduleRule,
        forecast_start: date,
    ):

        if (
            rule.start_date is not None
            and rule.rule_type.lower() == "biweekly"
        ):

            current = rule.start_date

            while current < forecast_start:
                current += timedelta(weeks=2 * rule.interval)

            return current

        if rule.start_date is not None:
            return max(rule.start_date, forecast_start)

        if rule.rule_type.lower() == "monthly":

            day = min(
                rule.day_of_month,
                monthrange(
                    forecast_start.year,
                    forecast_start.month,
                )[1],
            )

            candidate = forecast_start.replace(day=day)

            if candidate < forecast_start:
                candidate = self._add_months(candidate, rule.interval)

            return candidate

        if rule.rule_type.lower() == "semimonthly":

            days = sorted(rule.days_of_month)

            # Try every configured day in the current month.
            for day in days:

                if day >= forecast_start.day:

                    return forecast_start.replace(
                        day=min(
                            day,
                            monthrange(
                                forecast_start.year,
                                forecast_start.month,
                            )[1],
                        )
                    )

            # Otherwise use the first configured day next month.
            next_month = self._add_months(forecast_start, 1)

            return next_month.replace(
                day=min(
                    days[0],
                    monthrange(
                        next_month.year,
                        next_month.month,
                    )[1],
                )
            )

        if rule.rule_type.lower() == "annual":

            candidate = forecast_start.replace(
                month=rule.month_of_year,
                day=rule.day_of_month,
            )

            if candidate < forecast_start:
                candidate = candidate.replace(
                    year=candidate.year + rule.interval,
                )

            return candidate

        return forecast_start
    
    def _next_occurrence(self, current, rule):

        rule_type = rule.rule_type.lower()

        if rule_type == "one-time":
            return None

        if rule_type == "weekly":
            return current + timedelta(weeks=rule.interval)

        if rule_type == "biweekly":
            return current + timedelta(weeks=2 * rule.interval)

        if rule_type == "semimonthly":
            return self._next_semi_monthly(current, rule)

        if rule_type == "monthly":
            return self._add_months(current, rule.interval)

        if rule_type == "quarterly":
            return self._add_months(current, 3 * rule.interval)

        if rule_type == "annual":
            return self._add_months(current, 12 * rule.interval)

        raise ValueError(f"Unsupported rule type: {rule.rule_type}")

    def _next_semi_monthly(self, current, rule):

        first_day, second_day = sorted(rule.days_of_month)

        if current.day == first_day:

            next_day = min(
                second_day,
                monthrange(current.year, current.month)[1],
            )

            return current.replace(day=next_day)

        next_month = self._add_months(current, 1)

        next_day = min(
            first_day,
            monthrange(next_month.year, next_month.month)[1],
        )

        return next_month.replace(day=next_day)

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