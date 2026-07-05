from pathlib import Path

from sfos.forecast_pipeline import ForecastPipeline


def main():

    pipeline = ForecastPipeline()

    forecast = pipeline.generate(
        registry_path=Path("data") / "recurring_cash_flow.csv",
        current_balance=8069.52,
    )

    print("=" * 50)
    print("STONE FAMILY OPERATING SYSTEM")
    print("=" * 50)
    print()

    print(f"Opening Balance : ${forecast.opening_balance:,.2f}")
    print(f"Lowest Balance  : ${forecast.lowest_balance:,.2f}")
    print(f"Ending Balance  : ${forecast.ending_balance:,.2f}")
    print()
    print("Forecast Events")
    print("-" * 60)

    for occurrence in forecast.occurrences:

        sign = "+" if occurrence.flow_type == "Income" else "-"

        print(
            f"{occurrence.occurrence_date:%Y-%m-%d}  "
            f"{occurrence.event_name:<30}  "
            f"{sign}${occurrence.amount:>9,.2f}"
        )

    print()
    if forecast.low_cash_warning:
        print("⚠ LOW CASH WARNING")
    else:
        print("✓ No Low Cash Warning")


if __name__ == "__main__":
    main()