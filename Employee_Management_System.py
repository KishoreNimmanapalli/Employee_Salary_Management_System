class Employee:

    def __init__(self,name,employee_id,salary):
        self.__name=name
        self.__employee_id=employee_id
        self.__salary=salary

    def get_name(self):
        return self.__name

    def get_employee_id(self):
        return self.__employee_id

    def get_salary(self):
        return self.__salary

    def update_salary(self,new_salary):
        if new_salary>0:
            self.__salary=new_salary
        
        else:
            print("Error: Salary cannot be negative")

    def add_bonus(self,bonus):
        if bonus > 0:
            self.__salary +=bonus
        
        else:
            print("Bonus must be positive amount")

    def display_details(self):
        print(f"Employee Name: {self.__name}")
        print(f"Employee ID: {self.__employee_id}")
        print(f"Employee Salary: ₹{self.__salary}")

    def annual_salary(self):
        return self.__salary*12

emp_name=input("Enter Employee Name:")
emp_id=input("Enter Employee ID:")
emp_salary=int(input("Enter Employee Salary:"))
emp_bonus=int(input("Enter Bonus:"))
emp_new_salary=int(input("Enter New Salary:"))
print()
print("=== Employee Details ===")

emp=Employee(emp_name,emp_id,emp_salary)

emp.display_details()

emp.add_bonus(emp_bonus)
print(f"After Bonus: ₹{emp.get_salary()}")

emp.update_salary(emp_new_salary)
print(f"After Salary Update: ₹{emp.get_salary()}")

print(f"Annual Salary: ₹{emp.annual_salary()}")



