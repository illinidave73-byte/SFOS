# SFOS Architecture

## Design Principles

1. Registry First
2. Real Financial Data
3. Cash Flow First
4. Recommendations over Reports
5. Strong Test Coverage

## Major Components

```
Mission Control
        │
Treasury Engine
        │
Cash Forecast Engine
        │
Financial Ledger
        │
Registries
```

## Registries

- Master Account Registry
- Transaction History
- Recurring Cash Flow Registry

## Domain Models

- Account
- Transaction
- RecurringCashFlow
- CashForecast

## Configuration

All application settings originate from:

config/settings.yaml

through

Configuration()

## Testing

pytest

Current coverage:

23 passing tests