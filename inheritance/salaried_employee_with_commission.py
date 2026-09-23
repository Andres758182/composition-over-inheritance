"""Salaried employee that also earns a commission."""

from dataclasses import dataclass

from salaried_employee import SalariedEmployee


@dataclass
class SalariedEmployeeWithCommission(SalariedEmployee):
    """Employee that's paid based on a fixed monthly salary and that gets a commission."""

    commission: float = 100
    contracts_landed: int = 0

    def compute_pay(self) -> float:
        return super().compute_pay() + self.commission * self.contracts_landed
