"""Abstract payment contract that every employee has."""

from abc import ABC, abstractmethod


class Contract(ABC):
    """Represents a contract and a payment process for a particular employee."""

    @abstractmethod
    def get_payment(self) -> float:
        """Compute how much to pay an employee under this contract."""
