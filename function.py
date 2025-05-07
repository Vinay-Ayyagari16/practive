import pandas as pd

# Load the Excel file
df = pd.read_excel("nba.xlsx")

# Display the first few rows
print(df.head())
#Purpose: View the first or last few rows of the dataset.
print(df.tail())


#display the information of dataset
print(df.info())
#purpose: Get a concise summary (column types, non-null counts).

#display the numeric column 
print(df.describe())
#purpose:summary statistics for numeric column

# display the single and multiple column
print(df['Name'])                  # Single column
print(df[['Name', 'Team']])        # Multiple columns
#Purpose: Access specific column(s)

#tell us the rows based on condition 
print(df[df['Age'] > 30])         # Players older than 30
#purpose:filter rows based on a condition

#display the group by 
print(df.groupby('Team')['Salary'].mean())   
#purpose:Group data and perform aggregate functions

#  display missing value 
print(df.isnull().sum())          # Count missing values per column
print(df.dropna())                # Remove rows with missing data
print(df.fillna(0))               # Replace missing values with 0
#purpose: Handle missing values

# display the dataset in sort order  
print(df.sort_values(by='Salary', ascending=False))   # Highest-paid players
#purpose:sort the DataFrame by column values

#display the unique value and nunique value
print(df['Position'].value_counts())  # Count players per position
print(df.nunique())
#Purpose: Count unique values (great for categorical columns)
#purpose: Count unique values per column.

#display the df.apply
print( df['Weight'].apply(lambda x: x * 0.4536))  # Convert lbs to kg
#purpose: Apply a function to each row or column.







