"===== Employee Management System ====="

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return  self.salary
class Manager(Employee):
    def __init__(self,name,salary,bonus):
        super().__init__(name,salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.salary + self.bonus

class Developer(Employee):
    def __init__(self, name, salary, overtime_pay):
        super().__init__(name, salary)
        self.overtime_pay = overtime_pay

    def calculate_salary(self):
        return self.salary + self.overtime_pay

# === Example Usage ===

# Create a Manager and a Developer
manager = Manager("Alice", 5000, 1200)         # Base salary: 5000, Bonus: 1200
developer = Developer("Bob", 4000, 800)        # Base salary: 4000, Overtime Pay: 800

# Calculate and display salaries
print("=== Salary Details ===")
print(f"{manager.name}'s Total Salary: ${manager.calculate_salary()}")
print(f"{developer.name}'s Total Salary: ${developer.calculate_salary()}")
