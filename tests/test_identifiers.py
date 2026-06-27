from sfos.identifiers import generate_id


def test_generate_id():
    identifier = generate_id()

    assert isinstance(identifier, str)
    assert len(identifier) > 20