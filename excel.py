import pandas as pd
from sqlalchemy import create_engine

df = pd.read_excel("/home/thrymr/Downloads/dummy.xlsx")  # auto-detects sheet


# Create PostgreSQL connection engine
engine = create_engine('postgresql://postgres:test@localhost:5432/portfolio project')

# Automatically creates the table and inserts data
df.to_sql('dummy', engine, if_exists='replace', index=False)

print("Table created and data inserted successfully.")

