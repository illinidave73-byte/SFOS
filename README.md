# Stone Family Operating System (SFOS)

SFOS is a Household Financial Operating System designed to help families make better financial decisions.

Unlike traditional budgeting software, SFOS focuses on forecasting, recommendations, and long-term financial planning.

## Current Capabilities

- Master Account Registry
- Financial Ledger
- Transaction Import
- Treasury Engine
- Mission Control
- Live Checking Balance
- Recurring Cash Flow Registry
- Configuration System

## Project Structure

```
config/
data/
docs/
src/
tests/
```

## Development

Create a virtual environment:

```bash
python -m venv .venv
```

Activate:

macOS/Linux

```bash
source .venv/bin/activate
```

Install:

```bash
pip install -e .
pip install -r requirements.txt
```

Run tests:

```bash
python -m pytest
```

Run SFOS:

```bash
python -m sfos
```

## Status

Current Engineering Build:

**EB-0.3**

Current Test Status:

**23 Passing Tests**

License

MIT
