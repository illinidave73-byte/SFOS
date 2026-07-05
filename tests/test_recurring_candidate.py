from sfos.detection.recurring_candidate import RecurringCandidate


def test_candidate_creation():

    candidate = RecurringCandidate(
        merchant="Netflix",
        transactions=[],
    )

    assert candidate.merchant == "Netflix"
    assert candidate.transactions == []