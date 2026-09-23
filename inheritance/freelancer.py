"""Freelancer paid by the hour."""

from dataclasses import dataclass

from employee import Employee


@dataclass
class Freelancer(Employee):
    """Freelancer that's paid based on number of worked hours."""

    pay_rate: float
    hours_worked: int = 0
    vat_number: str = ""

    def compute_pay(self) -> float:
        return self.pay_rate * self.hours_worked
