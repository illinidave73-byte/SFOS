"""
SFOS Recurring Cash Flow Mapper
"""

from sfos.recurring_cash_flow import RecurringCashFlow
from sfos.schedule_rule import ScheduleRule


class RecurringCashFlowMapper:
    """Converts recurring cash flows into scheduling rules."""

    def to_schedule_rule(
        self,
        cash_flow: RecurringCashFlow,
    ) -> ScheduleRule:
        return ScheduleRule(
            rule_type=cash_flow.frequency,
            start_date=cash_flow.next_date,
        )