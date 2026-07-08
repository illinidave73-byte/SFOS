"""
SFOS Recurring Detection Report
"""


class RecurringDetectionReport:
    """Formats recurring transaction detection results."""

    def generate(self, candidates):

        lines = []

        lines.append("=" * 50)
        lines.append("Recurring Transaction Detection")
        lines.append("=" * 50)
        lines.append("")

        for candidate in candidates:

            lines.append(candidate.merchant)
            lines.append("-" * 40)
            lines.append(
                f"Occurrences: {len(candidate.transactions)}"
            )

            if candidate.analysis is not None:

                lines.append(
                    f"Average Interval: "
                    f"{candidate.analysis.average_interval:.1f}"
                )

                lines.append(
                    f"Frequency: "
                    f"{candidate.analysis.inferred_frequency}"
                )

            lines.append("")

        return "\n".join(lines)