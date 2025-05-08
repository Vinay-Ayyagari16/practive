import matplotlib.pyplot as plt

# Your data
cuts = ['Fair', 'Good', 'Ideal', 'Premium', 'Very Good']
counts = [337, 327, 326, 326, 336]
avg_prices = [18574, 18788, 18806, 18823, 18818]

# Create a line plot
plt.figure(figsize=(10, 6))

# Plotting count
plt.plot(cuts, counts, marker='o', label='Count of Diamonds')

# Plotting average price
plt.plot(cuts, avg_prices, marker='s', label='Average Price')

# Add titles and labels
plt.title('Diamond Cut: Count and Average Price')
plt.xlabel('Cut Type')
plt.ylabel('Value')
plt.legend()
plt.grid(True)

# Show plot
plt.tight_layout()
plt.show()






import matplotlib.pyplot as plt
import pandas as pd

data = {
    'price': [500, 1000, 1500, 2000, 2500, 3000, 4000, 5000, 6000],
    'count': [50, 120, 180, 160, 140, 110, 90, 60, 30]
}

df = pd.DataFrame(data)

plt.figure(figsize=(10, 5))
plt.fill_between(df['price'], df['count'], color='lightblue', alpha=0.7)
plt.plot(df['price'], df['count'], color='blue', linewidth=2, marker='o')

for x, y in zip(df['price'], df['count']):
    plt.text(x, y + 5, str(y), ha='center', va='bottom', fontsize=9, color='black')

plt.title('Area Chart: Count of Diamonds vs Price')
plt.xlabel('Price (USD)')
plt.ylabel('Number of Diamonds')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()