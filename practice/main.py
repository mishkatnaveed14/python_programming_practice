class Employee:
    def __init__(self, emp_id, emp_name, department, basic_salary, private_balance):
        if (basic_salary < 0):
            print("Invalid Input salary can not be negative")
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.department = department
        self.basic_salary = basic_salary
        self.private_balance = private_balance

    def display_info(self):
        print(f"Employee Id: {self.emp_id}")
        print(f"Employee Name: {self.emp_name}")
        print(f"Department: {self.department}")
        print(f"Basic Salary: {self.basic_salary}")
        print(f"Private Balance: {self.private_balance}")

class fulltime_Employee(Employee):
    def __init__(self, emp_id, emp_name, department, basic_salary, private_balance, bonus, tax_percentage):
        super().__init__(emp_id, emp_name, department, basic_salary, private_balance)
        self.bonus = bonus
        self.tax_percentage = tax_percentage

    def calculate_salary(self):
        gross_salary = self.basic_salary + self.bonus
        tax_amount = gross_salary * (self.tax_percentage / 100)
        net_salary = gross_salary - tax_amount
        return gross_salary, tax_amount, net_salary

class freelance_Employee(Employee):
    def __init__(self, emp_id, emp_name, department, basic_salary, private_balance, hours_worked, hourly_rate, service_fee_percentage):
        super().__init__(emp_id, emp_name, department, basic_salary, private_balance)
        if hours_worked < 0:
            print("Invalid Input hours worked can not be negative")
        if hourly_rate < 0:
            print("Invalid Input hourly rate can not be negative")
        if service_fee_percentage < 0:
            print("Invalid Input service fee percentage can not be negative")
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
        self.service_fee_percentage = service_fee_percentage

    def calculate_salary(self):
        gross_salary = self.hours_worked * self.hourly_rate
        service_fee = gross_salary * (self.service_fee_percentage / 100)
        net_salary = gross_salary - service_fee
        return gross_salary, service_fee, net_salary

# employee 1
print("\nEnter Employee 1 Details")
emp_id = input("Enter Employee Id: ")
emp_name = input("Enter Employee Name: ")
department = input("Enter Department: ")
salary = float(input("Enter Salary: "))
private_balance = float(input("Enter Private Salary Balance: "))
bonus = float(input("Enter Bonus: "))
tax_percentage = float(input("Enter Tax Percentage: "))
emp1 = fulltime_Employee(emp_id, emp_name, department, salary, private_balance, bonus, tax_percentage)

# employee 2
print("\nEnter Employee 2 Details")
emp_id = input("Enter Employee Id: ")
emp_name = input("Enter Employee Name: ")
department = input("Enter Department: ")
salary = float(input("Enter Salary: "))
private_balance = float(input("Enter Private Salary Balance: "))
bonus = float(input("Enter Bonus: "))
tax_percentage = float(input("Enter Tax Percentage: "))
emp2 = fulltime_Employee(emp_id, emp_name, department, salary, private_balance, bonus, tax_percentage)

# employee 3
print("\nEnter Employee 3 Details")
emp_id = input("Enter Employee Id: ")
emp_name = input("Enter Employee Name: ")
department = input("Enter Department: ")
salary = float(input("Enter Salary: "))
private_balance = float(input("Enter Private Salary Balance: "))
hours_worked = float(input("Enter Hours Worked: "))
hourly_rate = float(input("Enter Hourly Rate: "))
service_fee_percentage = float(input("Enter Service Fee Percentage: "))
emp3 = freelance_Employee(emp_id, emp_name, department, salary, private_balance, hours_worked, hourly_rate, service_fee_percentage)

gross1, tax1, net1 = emp1.calculate_salary()
gross2, tax2, net2 = emp2.calculate_salary()
gross3, fee3, net3 = emp3.calculate_salary()

total_payroll = net1 + net2 + net3
highest_salary = max(net1, net2, net3)

if highest_salary == net1:
    highest_employee = emp1
elif highest_salary == net2:
    highest_employee = emp2
else:
    highest_employee = emp3

print("\n========== PAYROLL SUMMARY ==========")
print("Company : TechNova Solutions")
print("Total Employees : 3")
print(f"Total Payroll : Rs. {total_payroll:,.2f}")
print(f"Highest Paid : {highest_employee.emp_name}")
print(f"Highest Salary : Rs. {highest_salary:,.2f}")
