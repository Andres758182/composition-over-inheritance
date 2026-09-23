from contract_commission import ContractCommission
from employee import Employee
from freelancer_contract import FreelancerContract
from hourly_contract import HourlyContract
from salaried_contract import SalariedContract


def main() -> None:
    employees = [
        Employee(name="Henry", id=12346, contract=HourlyContract(pay_rate=50, hours_worked=100)),
        Employee(name="Maria", id=51234, contract=SalariedContract(monthly_salary=4000)),
        Employee(name="Tom", id=60987, contract=FreelancerContract(pay_rate=60, hours_worked=40)),
        Employee(
            name="Lucia",
            id=73456,
            contract=HourlyContract(pay_rate=40, hours_worked=80),
            commission=ContractCommission(contracts_landed=3),
        ),
        Employee(
            name="Sarah",
            id=47832,
            contract=SalariedContract(monthly_salary=5000),
            commission=ContractCommission(contracts_landed=10),
        ),
        Employee(
            name="Diego",
            id=88901,
            contract=FreelancerContract(pay_rate=70, hours_worked=20),
            commission=ContractCommission(contracts_landed=5),
        ),
    ]

    for employee in employees:
        print(f"{employee.name} earned ${employee.compute_pay():.2f}")


if __name__ == "__main__":
    main()
