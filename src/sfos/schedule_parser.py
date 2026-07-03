"""
SFOS Schedule Parser
"""

from sfos.schedule_rule import ScheduleRule


class ScheduleParser:
    """Parses SFOS scheduling language into ScheduleRule objects."""

    def parse(
        self,
        frequency: str,
        day_rule: str,
    ) -> ScheduleRule:

        if frequency.lower() == "monthly":

            day_rule = day_rule.lower().strip()

            day_map = {
                "first": 1,
                "second": 2,
                "third": 3,
                "fourth": 4,
                "fifth": 5,
            }

            first_word = day_rule.split()[0]

            if first_word in day_map:
                day = day_map[first_word]
            else:
                day = int(
                    first_word
                    .replace("st", "")
                    .replace("nd", "")
                    .replace("rd", "")
                    .replace("th", "")
                )

            return ScheduleRule(
                rule_type="Monthly",
                start_date=None,
                day_of_month=day,
            )

        raise NotImplementedError(
            f"Unsupported schedule: {frequency} / {day_rule}"
        )