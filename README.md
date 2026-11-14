# Employee Salary Management System (Python Encapsulation)

A Python project demonstrating Object-Oriented Programming (OOP) principles—specifically **Encapsulation** and **Data Hiding**—by securely managing employee details and salary updates.

## 📌 Overview
This program models an `Employee` class where sensitive data (name, employee ID, and salary) is kept private. Instead of allowing direct access or modification of internal variables, the class provides controlled getter and setter-style methods with built-in validation rules.

## ✨ Features & Concepts Covered
* **Data Hiding (Private Variables):** Uses double underscores (`__name`, `__employee_id`, `__salary`) to restrict direct external access.
* **Getter Methods:** Safely retrieves private employee data (`get_name()`, `get_employee_id()`, `get_salary()`).
* **Controlled Modification:** Enforces validation rules through `update_salary()` (prevents negative values) and `add_bonus()`.
* **Annual Salary Calculation:** Computes the yearly salary (`Monthly Salary × 12`) via `annual_salary()`.

## 🚀 Getting Started

### Prerequisites
* Python 3.x installed on your machine.

### Running the Code
1. Clone this repository or download the `employee_management.py` file:
   ```bash
   git clone https://github.com
   ```
2. Navigate to the project directory:
   ```bash
   cd Employee_Salary_Management_System
   ```
3. Run the Python script:
   ```bash
   python Employee_Management_System.py
   ```

## 💻 Sample Output
```text
Employee Name: Rahul
Employee ID: EMP101
Salary: ₹30000
After Bonus:
Salary: ₹35000
Salary Updated Successfully
After Salary Update:
Salary: ₹40000
Annual Salary: ₹480000
```

## 🛡️ Encapsulation Rule Enforced
Direct modification of attributes is restricted:
```python
# ❌ Avoid doing this:
employee.__salary = 40000

# ✅ Use controlled methods instead:
employee.update_salary(40000)
employee.add_bonus(5000)
```
