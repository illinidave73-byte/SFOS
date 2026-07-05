ForecastPipeline is the orchestration layer.
SchedulingService consumes both RecurringCashFlow and ScheduleRule.
ScheduleRule contains recurrence metadata only.
ScheduledOccurrence is the canonical dated financial event.
All future engines consume ScheduledOccurrence objects.