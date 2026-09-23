from dataclasses import dataclass

from employee import Employee


@dataclass
class SalariedEmployee(Employee):
    """Employee that's paid based on a fixed monthly salary."""

    monthly_salary: float
    percentage: float = 1

    def compute_pay(self) -> float:
        return self.monthly_salary * self.percentage
