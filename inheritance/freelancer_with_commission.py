from dataclasses import dataclass

from freelancer import Freelancer


@dataclass
class FreelancerWithCommission(Freelancer):
    """Freelancer that's paid based on number of worked hours and that gets a commission."""

    commission: float = 100
    contracts_landed: int = 0

    def compute_pay(self) -> float:
        return super().compute_pay() + self.commission * self.contracts_landed
