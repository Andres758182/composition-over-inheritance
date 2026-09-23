"""Hourly employee that also earns a commission."""

from dataclasses import dataclass

from hourly_employee import HourlyEmployee


@dataclass
class HourlyEmployeeWithCommission(HourlyEmployee):
    """Employee that's paid based on number of worked hours and that gets a commission."""

    commission: float = 100
    contracts_landed: int = 0

    def compute_pay(self) -> float:
        return super().compute_pay() + self.commission * self.contracts_landed
