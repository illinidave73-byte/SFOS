# ADR-001: Centralized Scheduling Service

## Status

Accepted

## Context

Multiple SFOS modules require recurring date calculations.

Without a shared service, recurrence logic would be duplicated across the application.

## Decision

Introduce a centralized SchedulingService responsible for generating recurring dates.

Business engines consume scheduled dates rather than implementing recurrence logic.

## Consequences

Positive

- Single implementation
- Easier testing
- Consistent scheduling

Negative

- Additional abstraction

## Rule Design

Scheduling rules are intentionally data-driven.

Rather than creating dozens of rule types (e.g. Every Other Thursday, Last Business Day), rules are composed from reusable properties such as:

- frequency
- interval
- weekday
- day-of-month
- business-day adjustment

This minimizes the number of rule types while maximizing flexibility.