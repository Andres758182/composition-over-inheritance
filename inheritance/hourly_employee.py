from dataclasses import dataclass

from employee import Employee


@dataclass
class HourlyEmployee(Employee):
    """Employee that's paid based on number of worked hours."""

    pay_rate: float
    hours_worked: int = 0
    employer_cost: float = 1000

    def compute_pay(self) -> float:
        return self.pay_rate * self.hours_worked + self.employer_cost
