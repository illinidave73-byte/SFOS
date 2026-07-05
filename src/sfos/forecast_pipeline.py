"""
SFOS Forecast Pipeline
"""


from sfos.recurring_cash_flow_mapper import RecurringCashFlowMapper


from sfos.recurring_cash_flow_registry import RecurringCashFlowRegistry

class ForecastPipeline:
    """Coordinates scheduling and forecasting."""

    

    def generate(
        self,
        registry_path,
    ):

        registry = RecurringCashFlowRegistry(registry_path)

        mapper = RecurringCashFlowMapper()

        rules = [
            mapper.to_schedule_rule(event)
            for event in registry.events
        ]

        return rules