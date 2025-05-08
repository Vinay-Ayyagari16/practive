import pandas as pd
df = pd.read_excel("/home/thrymr/Downloads/diamond.xlsx")

# 1. Average price of all diamonds
average_price = df['price'].mean()
print("Average price of all diamonds:", average_price)

# 2. Count of diamonds for each type of cut
cut_counts = df['cut'].value_counts()
print("\nCount of diamonds for each cut:\n", cut_counts)

# 3. Average carat for each combination of cut and color
avg_carat_cut_color = df.groupby(['cut', 'color'])['carat'].mean()
print("\nAverage carat for each combination of cut and color:\n", avg_carat_cut_color)

# 4. Clarity with the highest average price
highest_avg_price_clarity = df.groupby('clarity')['price'].mean().idxmax()
print("\nClarity with highest average price:", highest_avg_price_clarity)

# 5. Diamonds with price greater than 10000
diamonds_above_10000 = df[df['price'] > 10000]
print("\nDiamonds with price greater than 10000:\n", diamonds_above_10000)

# 6. Add volume column and find top 5 diamonds by volume
df['volume'] = df['x'] * df['y'] * df['z']
top_5_by_volume = df.sort_values(by='volume', ascending=False).head(5)
print("\nTop 5 diamonds by volume:\n", top_5_by_volume)

# 7. Price range (min and max) for each cut type
price_range_by_cut = df.groupby('cut')['price'].agg(['min', 'max'])
print("\nPrice range for each cut:\n", price_range_by_cut)

# 8. Most common combination of color and clarity
most_common_color_clarity = df.groupby(['color', 'clarity']).size().idxmax()
print("\nMost common combination of color and clarity:", most_common_color_clarity)

# 9. Correlation between carat and price
correlation = df['carat'].corr(df['price'])
print("\nCorrelation between carat and price:", correlation)

# 10. Percentage of diamonds with Ideal cut, D color, and VS1 clarity
ideal_d_vs1 = df[
    (df['cut'] == 'Ideal') & 
    (df['color'] == 'D') & 
    (df['clarity'] == 'VS1')
]
percentage_ideal_d_vs1 = (len(ideal_d_vs1) / len(df)) * 100
print("\nPercentage of diamonds with Ideal cut, D color, and VS1 clarity:", percentage_ideal_d_vs1, "%")

