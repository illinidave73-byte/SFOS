"""
SFOS Recurring Cash Flow Mapper
"""

from email import parser

from sfos.recurring_cash_flow import RecurringCashFlow
from sfos.schedule_rule import ScheduleRule
from sfos.schedule_parser import ScheduleParser

class RecurringCashFlowMapper:
    """Converts recurring cash flows into scheduling rules."""

    def to_schedule_rule(
        self,
        cash_flow: RecurringCashFlow,
    ) -> ScheduleRule:
        parser = ScheduleParser()

        return parser.parse(
            frequency=cash_flow.frequency,
            day_rule=cash_flow.day_rule,
        )