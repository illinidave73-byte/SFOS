"""
SFOS Scheduling Service
"""

from datetime import date, timedelta


class SchedulingService:
    """Generates recurring event dates."""

    def occurrences(
        self,
        start: date,
        end: date,
        frequency: str,
    ) -> list[date]:

        dates = []

        current = start

        frequency = frequency.lower()

        if frequency == "one-time":
            return [start]

        if frequency == "weekly":

            while current <= end:
                dates.append(current)
                current += timedelta(days=7)

            return dates

        if frequency == "biweekly":

            while current <= end:
                dates.append(current)
                current += timedelta(days=14)

            return dates

        if frequency == "monthly":

            while current <= end:

                dates.append(current)

                month = current.month + 1
                year = current.year

                if month > 12:
                    month = 1
                    year += 1

                current = current.replace(
                    year=year,
                    month=month,
                )

            return dates

        raise ValueError(
            f"Unsupported frequency: {frequency}"
        )