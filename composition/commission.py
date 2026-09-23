from abc import ABC, abstractmethod


class Commission(ABC):
    """Represents a commission payment process."""

    @abstractmethod
    def get_payment(self) -> float:
        """Return the commission to be paid out."""
