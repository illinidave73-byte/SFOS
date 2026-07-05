"""
SFOS Forecast Pipeline
"""


from sfos.recurring_cash_flow_mapper import RecurringCashFlowMapper
from datetime import date, timedelta
from sfos.scheduling_service import SchedulingService
from sfos.recurring_cash_flow_registry import RecurringCashFlowRegistry
from sfos.forecast_engine import ForecastEngine
from sfos.cash_forecast import CashForecast

class ForecastPipeline:
    """Coordinates scheduling and forecasting."""

    

    def generate(
        self,
        registry_path,
        current_balance: float,
    ):

        registry = RecurringCashFlowRegistry(registry_path)

        mapper = RecurringCashFlowMapper()

        valid_events = [
            event
            for event in registry.events
            if (
                event.active
                and event.frequency.upper() != "TBD"
                and event.day_rule.upper() != "TBD"
            )
        ]

        rules = [
            mapper.to_schedule_rule(event)
            for event in valid_events
        ]

        scheduler = SchedulingService()

        occurrences = []

        forecast_start = date.today()
        forecast_end = forecast_start + timedelta(days=30)

        for cash_flow, rule in zip(valid_events, rules):

            occurrences.extend(
                scheduler.generate(
                    rule=rule,
                    event_name=cash_flow.name,
                    flow_type=cash_flow.flow_type,
                    start_date=forecast_start,
                    end_date=forecast_end,
                    amount=cash_flow.amount,
                    priority=cash_flow.priority,
                    category=cash_flow.category,
                    source_account=cash_flow.source_account,
                )
            )

        engine = ForecastEngine(
            current_balance=current_balance,
        )

        return engine.generate(occurrences)