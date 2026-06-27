"""
Institution domain model.
"""

from dataclasses import dataclass

from sfos.base import BaseModel


@dataclass(slots=True)
class Institution(BaseModel):
    """
    Represents a financial institution.

    Examples:
        - Chase
        - USAA
        - American Express
        - Fidelity
    """

    name: str
    website: str = ""
    routing_number: str = ""

    def __str__(self) -> str:
        return self.name