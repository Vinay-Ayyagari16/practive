import pandas as pd 
import matplotlib.pyplot as plt

data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Sales': [1500, 1800, 1700, 2100, 1900, 2200]
}

df = pd.DataFrame(data)

#pie chart
plt.figure(figsize=(6,6))
plt.pie(df['Sales'], labels=df['Month'], autopct='%1.1f%%', startangle=140)
plt.title('Monthly Sales Distribution - Pie Chart')
plt.show()

