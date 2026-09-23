from dataclasses import dataclass

from commission import Commission


@dataclass
class ContractCommission(Commission):
    """Represents a commission payment process based on the number of contracts landed."""

    commission: float = 100
    contracts_landed: int = 0

    def get_payment(self) -> float:
        return self.commission * self.contracts_landed
