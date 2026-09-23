"""Contract for a freelancer paid by the hour."""

from dataclasses import dataclass

from contract import Contract


@dataclass
class FreelancerContract(Contract):
    """Contract type for a freelancer (paid on an hourly basis)."""

    pay_rate: float
    hours_worked: int = 0
    vat_number: str = ""

    def get_payment(self) -> float:
        return self.pay_rate * self.hours_worked
