#Employee Management System
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        return f"{self.name} earns ${self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def show_details(self):
        return f"{self.name} manages {self.department} and earns ${self.salary}"

# Usage
emp1 = Employee("Alice", 50000)
mgr1 = Manager("Bob", 90000, "Sales")

print(emp1.show_details())
print(mgr1.show_details())


# bank Account Class Example 
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")

    def __str__(self):
        return f"BankAccount(owner={self.owner}, balance=${self.balance})"

# Usage
account = BankAccount("Alice", 100)
print(account)

account.deposit(50)
account.withdraw(30)
account.withdraw(150)  # Should print "Insufficient funds"


text = """
Database Schema
create these 3 tables first in the database names practice-database using terminal and postgres
employees table
employee_id	name	department_id
1	Alice	10
2	Bob	20
3	Charlie	30
4	David	NULL
departments table 
department_id	department_name
10	HR
20	Finance
30	IT
40	Marketing
salaries table
employee_id	salary
1	5000
2	6000
4	4500
"""

# Count capital letters
capital_count = sum(1 for char in text if char.isupper())
print("Number of capital letters:", capital_count)

from collections import Counter

text = """
Your multiline text goes here...
"""

# Count each character
char_counts = Counter(text)

# Print each character and its count
for char, count in char_counts.items():
    print(f"{char} - {count}")
text = "aabBBBAA"
