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
            return self._parse_monthly(day_rule)

        if (
            frequency.lower() == "biweekly"
            and day_rule.lower().strip() == "15th and 30th of every month"
        ):

            return ScheduleRule(
                rule_type="SemiMonthly",
                start_date=None,
                days_of_month=[15, 30],
            )

        if frequency.lower() == "biweekly":

            if day_rule.lower().strip() == "every other thursday":

                return ScheduleRule(
                    rule_type="Biweekly",
                    start_date=None,
                    interval=1,
                    day_of_week=3,
                ) 

        if (
            frequency.lower() == "every other month"
            and day_rule.lower().strip() == "every two months on first of month"
        ):

            return ScheduleRule(
                rule_type="Monthly",
                start_date=None,
                interval=2,
                day_of_month=1,
            )

        if frequency.lower() == "annual":

            if day_rule.lower().strip() == "first day of july":

                return ScheduleRule(
                    rule_type="Annual",
                    start_date=None,
                    day_of_month=1,
                    month_of_year=7,
                )   
        
        raise NotImplementedError(
            f"Unsupported schedule: {frequency} / {day_rule}"
        )
    
    def _parse_monthly(
        self,
        day_rule: str,
    ) -> ScheduleRule:

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