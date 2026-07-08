"""
SFOS Recurring Pattern Analyzer
"""
import statistics

from sfos.detection.recurring_pattern_analysis import (
    RecurringPatternAnalysis,
)


class RecurringPatternAnalyzer:
    """Calculates statistics for recurring candidates."""

    def analyze(self, candidate):

        analysis = RecurringPatternAnalysis()

        if candidate.intervals:
            analysis.average_interval = (
                sum(candidate.intervals)
                / len(candidate.intervals)
            )
            analysis.minimum_interval = min(candidate.intervals)
            analysis.maximum_interval = max(candidate.intervals)
            if len(candidate.intervals) > 1:
                analysis.standard_deviation = statistics.stdev(
                    candidate.intervals
                )
            else:
                analysis.standard_deviation = 0.0
        avg = analysis.average_interval

        if avg is None:
            return analysis

        if 6 <= avg <= 8:
            analysis.inferred_frequency = "Weekly"

        elif 13 <= avg <= 15:
            analysis.inferred_frequency = "Biweekly"

        elif 27 <= avg <= 33:
            analysis.inferred_frequency = "Monthly"

        elif 85 <= avg <= 95:
            analysis.inferred_frequency = "Quarterly"

        elif 350 <= avg <= 380:
            analysis.inferred_frequency = "Annual"

        else:
            analysis.inferred_frequency = "Irregular"
    
        if analysis.inferred_frequency == "Irregular":
            analysis.confidence = 25.0

        elif (
            analysis.standard_deviation is not None
            and analysis.standard_deviation <= 1.0
        ):
            analysis.confidence = 99.0

        elif (
            analysis.standard_deviation is not None
            and analysis.standard_deviation <= 3.0
        ):
            analysis.confidence = 80.0

        else:
            analysis.confidence = 50.0

        return analysis