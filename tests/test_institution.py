from sfos.institution import Institution


def test_create_institution():
    institution = Institution(name="Chase")

    assert institution.name == "Chase"
    assert str(institution) == "Chase"
    assert institution.id is not None