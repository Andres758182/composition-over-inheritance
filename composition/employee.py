from dataclasses import dataclass
from typing import Optional

from commission import Commission
from contract import Contract


@dataclass
class Employee:
    """Basic representation of an employee at the company."""

    name: str
    id: int
    contract: Contract
    commission: Optional[Commission] = None

    def compute_pay(self) -> float:
        """Compute how much the employee should be paid."""
        payout = self.contract.get_payment()
        if self.commission is not None:
            payout += self.commission.get_payment()
        return payout
