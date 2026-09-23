"""Runnable example for the inheritance-based design.

Every pay/commission combination needs its own subclass, so the kind of
employee is chosen by picking the right class.
"""

from employee import Employee
from freelancer import Freelancer
from freelancer_with_commission import FreelancerWithCommission
from hourly_employee import HourlyEmployee
from hourly_employee_with_commission import HourlyEmployeeWithCommission
from salaried_employee import SalariedEmployee
from salaried_employee_with_commission import SalariedEmployeeWithCommission


def build_payroll() -> list[tuple[str, Employee]]:
    """Create one employee of every pay/commission combination."""
    return [
        ("Hourly", HourlyEmployee(name="Henry", id=12346, pay_rate=50, hours_worked=100)),
        (
            "Salaried + commission",
            SalariedEmployeeWithCommission(
                name="Sarah", id=47832, monthly_salary=5000, contracts_landed=10
            ),
        ),
        ("Salaried", SalariedEmployee(name="Maria", id=51234, monthly_salary=4000, percentage=0.5)),
        (
            "Freelancer",
            Freelancer(name="Tom", id=60987, pay_rate=60, hours_worked=40, vat_number="MX-60987"),
        ),
        (
            "Hourly + commission",
            HourlyEmployeeWithCommission(
                name="Lucia", id=73456, pay_rate=40, hours_worked=80, contracts_landed=3
            ),
        ),
        (
            "Freelancer + commission",
            FreelancerWithCommission(
                name="Diego",
                id=88901,
                pay_rate=70,
                hours_worked=20,
                vat_number="MX-88901",
                contracts_landed=5,
            ),
        ),
    ]


def main() -> None:
    """Print the pay of every employee using compute_pay()."""
    payroll = build_payroll()
    print("Payroll - inheritance design")
    print("-" * 52)
    for kind, employee in payroll:
        print(f"{employee.name:<6} #{employee.id}  {kind:<24} ${employee.compute_pay():>10,.2f}")
    print("-" * 52)
    total = sum(employee.compute_pay() for _, employee in payroll)
    print(f"{'Total':<39} ${total:>10,.2f}")


if __name__ == "__main__":
    main()
