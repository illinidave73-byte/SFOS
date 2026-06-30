"""
SFOS Configuration Service
"""

from pathlib import Path

import yaml


class Configuration:

    def __init__(self, path: str | Path = "config/settings.yaml"):
        self.path = Path(path)

        with open(self.path, "r") as stream:
            self.settings = yaml.safe_load(stream)

    @property
    def low_cash_threshold(self):

        return float(
            self.settings["treasury"]["low_cash_threshold"]
        )

    @property
    def forecast_days(self):

        return int(
            self.settings["treasury"]["forecast_days"]
        )