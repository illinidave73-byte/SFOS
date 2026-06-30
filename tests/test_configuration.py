from sfos.config import Configuration


def test_configuration_loads():

    config = Configuration()

    assert config.low_cash_threshold == 1000.0


def test_forecast_days():

    config = Configuration()

    assert config.forecast_days == 30