import pandas as pd

# Step 1: Create a dummy Excel file with sample data
data = {
    "Employee ID": [101, 102, 103, 104, 105],
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Department": ["HR", "Finance", "IT", "Marketing", "HR"],
    "Salary": [50000, 60000, 70000, 55000, 52000],
    "Join Date": pd.to_datetime(["2020-01-10", "2019-03-15", "2021-06-20", "2018-07-30", "2022-02-01"])
}

df = pd.DataFrame(data)

# Step 2: Insert new data
new_data = {
    "Employee ID": [106],
    "Name": ["Frank"],
    "Department": ["IT"],
    "Salary": [58000],
    "Join Date": pd.to_datetime(["2023-05-10"])
}
df = pd.concat([df, pd.DataFrame(new_data)], ignore_index=True)

# Step 3: Manipulate data
# Add a new column: Years of Service
current_date = pd.to_datetime("2025-06-10")
df["Years of Service"] = ((current_date - df["Join Date"]).dt.days / 365).round(1)

# Sort by Salary descending
df_sorted = df.sort_values(by="Salary", ascending=False)

# Save to Excel
output_path = "/home/thrymr/modified_employee_data.xlsx"
df_sorted.to_excel(output_path, index=False)

print(output_path)
