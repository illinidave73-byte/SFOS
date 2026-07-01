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