from freelancer import Freelancer
from freelancer_with_commission import FreelancerWithCommission
from hourly_employee import HourlyEmployee
from hourly_employee_with_commission import HourlyEmployeeWithCommission
from salaried_employee import SalariedEmployee
from salaried_employee_with_commission import SalariedEmployeeWithCommission


def main() -> None:
    employees = [
        HourlyEmployee(name="Henry", id=12346, pay_rate=50, hours_worked=100),
        SalariedEmployee(name="Maria", id=51234, monthly_salary=4000),
        Freelancer(name="Tom", id=60987, pay_rate=60, hours_worked=40),
        HourlyEmployeeWithCommission(
            name="Lucia", id=73456, pay_rate=40, hours_worked=80, contracts_landed=3
        ),
        SalariedEmployeeWithCommission(
            name="Sarah", id=47832, monthly_salary=5000, contracts_landed=10
        ),
        FreelancerWithCommission(
            name="Diego", id=88901, pay_rate=70, hours_worked=20, contracts_landed=5
        ),
    ]

    for employee in employees:
        print(f"{employee.name} earned ${employee.compute_pay():.2f}")


if __name__ == "__main__":
    main()
