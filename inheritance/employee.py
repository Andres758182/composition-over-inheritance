"""Abstract base class for every employee in the inheritance design."""

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Employee(ABC):
    """Basic representation of an employee at the company."""

    name: str
    id: int

    @abstractmethod
    def compute_pay(self) -> float:
        """Compute how much the employee should be paid."""
