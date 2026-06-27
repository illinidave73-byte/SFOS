from sfos.base import BaseModel


def test_base_model_creation():
    model = BaseModel()

    assert model.id is not None
    assert model.created_at is not None
    assert model.updated_at is not None


def test_touch_updates_timestamp():
    model = BaseModel()

    original = model.updated_at

    model.touch()

    assert model.updated_at >= original