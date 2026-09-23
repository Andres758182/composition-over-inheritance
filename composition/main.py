"""Runnable example for the composition-based design.

There is a single Employee class; the kind of employee is chosen by
plugging in a Contract and, optionally, a Commission.
"""

from contract_commission import ContractCommission
from employee import Employee
from freelancer_contract import FreelancerContract
from hourly_contract import HourlyContract
from salaried_contract import SalariedContract


def build_payroll() -> list[tuple[str, Employee]]:
    """Create one employee of every contract/commission combination."""
    return [
        (
            "Hourly",
            Employee(
                name="Henry", id=12346, contract=HourlyContract(pay_rate=50, hours_worked=100)
            ),
        ),
        (
            "Salaried + commission",
            Employee(
                name="Sarah",
                id=47832,
                contract=SalariedContract(monthly_salary=5000),
                commission=ContractCommission(contracts_landed=10),
            ),
        ),
        (
            "Salaried",
            Employee(
                name="Maria",
                id=51234,
                contract=SalariedContract(monthly_salary=4000, percentage=0.5),
            ),
        ),
        (
            "Freelancer",
            Employee(
                name="Tom",
                id=60987,
                contract=FreelancerContract(pay_rate=60, hours_worked=40, vat_number="MX-60987"),
            ),
        ),
        (
            "Hourly + commission",
            Employee(
                name="Lucia",
                id=73456,
                contract=HourlyContract(pay_rate=40, hours_worked=80),
                commission=ContractCommission(contracts_landed=3),
            ),
        ),
        (
            "Freelancer + commission",
            Employee(
                name="Diego",
                id=88901,
                contract=FreelancerContract(pay_rate=70, hours_worked=20, vat_number="MX-88901"),
                commission=ContractCommission(contracts_landed=5),
            ),
        ),
    ]


def main() -> None:
    """Print the pay of every employee using compute_pay()."""
    payroll = build_payroll()
    print("Payroll - composition design")
    print("-" * 52)
    for kind, employee in payroll:
        print(f"{employee.name:<6} #{employee.id}  {kind:<24} ${employee.compute_pay():>10,.2f}")
    print("-" * 52)
    total = sum(employee.compute_pay() for _, employee in payroll)
    print(f"{'Total':<39} ${total:>10,.2f}")


if __name__ == "__main__":
    main()
