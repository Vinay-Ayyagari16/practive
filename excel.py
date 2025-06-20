import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("/home/thrymr/Downloads/employees.csv")  # auto-detects sheet


# Create PostgreSQL connection engine
engine = create_engine('postgresql://postgres:test@localhost:5432/sample')

# Automatically creates the table and inserts data
df.to_sql('dummy', engine, if_exists='replace', index=False)

print("Table created and data inserted successfully.")


import sqlite3
import pandas as pd

# Load CSV
df = pd.read_csv("/home/thrymr/Downloads/employees.csv")

# Connect to SQLite in-memory database
conn = sqlite3.connect(":memory:")
df.to_sql("employees", conn, index=False, if_exists="replace")

# Create a cursor
cur = conn.cursor()

#Select All Employees
cur.execute("SELECT * FROM employees")
print(cur.fetchall())

#Employees with Salary > 60,000
cur.execute("SELECT name, salary FROM employees WHERE salary > 60000")
print(cur.fetchall())

#Group by Department and Get Average Salary
cur.execute("""
    SELECT department, AVG(salary) as avg_salary
    FROM employees
    GROUP BY department
""")
print(cur.fetchall())

#Count of Employees per Department
cur.execute("""
    SELECT department, COUNT(*) as num_employees
    FROM employees
    GROUP BY department
""")
print(cur.fetchall())

#Employees Joined After 2021-01-01
cur.execute("""
    SELECT name, joining_date 
    FROM employees 
    WHERE joining_date > '2021-01-01'
""")
print(cur.fetchall())


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print(f"{self.brand} {self.model}")
car1 = Car("Toyota", "Camry")
car1.display()  