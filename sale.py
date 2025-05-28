import pandas as pd

# Load Excel file
file_path = "/home/thrymr/Downloads/pandas_practice_dataset.xlsx"  # Use your actual path
excel_file = pd.ExcelFile(file_path)

# Load sheets
sales_df = excel_file.parse('Sales')
products_df = excel_file.parse('Products')
customers_df = excel_file.parse('Customers')
inventory_df = excel_file.parse('Inventory')
returns_df = excel_file.parse('Returns')

#Q1.Merge Sales and Products on ProductID
sales_products_df = pd.merge(sales_df, products_df, on='ProductID')
print(sales_products_df )

# Q2.Merge Sales and Customers on CustomerID
sales_customers_df = pd.merge(sales_df, customers_df, on='CustomerID')
print(sales_customers_df)


#Q3. Join Sales-Product-Customer with Returns on SaleID
sales_prod_cust_df = pd.merge(sales_products_df, customers_df, on='CustomerID')
full_sales_df = pd.merge(sales_prod_cust_df, returns_df, on='SaleID', how='left')
print(sales_prod_cust_df)

#04 Total SaleAmount for each ProductID
total_sales_by_product = sales_df.groupby('ProductID')['SaleAmount'].sum()
print(total_sales_by_product)

#Q5. Average SaleAmount by Category
avg_sale_by_category = sales_products_df.groupby('Category')['SaleAmount'].mean()
print(avg_sale_by_category)

#Q6. Group by City and find total quantity sold
total_quantity_by_city = pd.merge(sales_df, customers_df, on='CustomerID').groupby('City')['Quantity'].sum()
print(total_quantity_by_city)

#Q7. Group by Age groups and find mean sale amount
sales_customers_df['AgeGroup'] = pd.cut(sales_customers_df['Age'], bins=[20, 30, 40, 50], labels=['20-30', '31-40', '41-50'])
mean_sale_by_age_group = sales_customers_df.groupby('AgeGroup')['SaleAmount'].mean()
print(sales_customers_df)
print(mean_sale_by_age_group)

#Q8. Add column TotalPrice = Quantity * Price
sales_with_price = pd.merge(sales_df, products_df[['ProductID', 'Price']], on='ProductID')
sales_with_price['TotalPrice'] = sales_with_price['Quantity'] * sales_with_price['Price']
print(sales_with_price )
print(sales_with_price['TotalPrice'] )

#Q9.Remove duplicate customers (add some manually for testing)
customers_df_duplicates = pd.concat([customers_df, customers_df.iloc[[0]]], ignore_index=True)
customers_deduped = customers_df_duplicates.drop_duplicates()
print(customers_df_duplicates)
print(customers_deduped)

#Q10. Products returned and total refund amount
returned_products = pd.merge(returns_df, sales_df[['SaleID', 'ProductID']], on='SaleID')
refund_by_product = returned_products.groupby('ProductID')['RefundAmount'].sum()
print(returned_products)
print(refund_by_product)

#Q11. Concatenate Sales and Returns (common columns only)
common_cols = sales_df.columns.intersection(returns_df.columns)
transaction_log = pd.concat([sales_df[common_cols], returns_df[common_cols]], ignore_index=True)
print(common_cols)
print(transaction_log)

#Q12 Most common ReturnReason
most_common_reason = returns_df['ReturnReason'].mode()[0]
print(most_common_reason)

#Q13. Sort Inventory by Stock and get top 3 products with lowest stock
lowest_stock_products = inventory_df.sort_values(by='Stock').head(3)
print(lowest_stock_products)

#Q14 Filter NY customers and get their total sales
ny_customers_sales = pd.merge(customers_df, sales_df, on='CustomerID')
ny_total_sales = ny_customers_sales[ny_customers_sales['City'] == 'NY'].groupby('CustomerID')['SaleAmount'].sum()
print(ny_customers_sales)
print(ny_total_sales)

#Q15 Fill missing values in SaleAmount with mean

sales_df_missing = sales_df.copy()
sales_df_missing.loc[0, 'SaleAmount'] = None  # manually add a missing value
sales_df_missing['SaleAmount'] = sales_df_missing['SaleAmount'].fillna(sales_df_missing['SaleAmount'].mean())
print(sales_df_missing)

#Q16. Drop customers who have no sales
customers_with_sales = pd.merge(customers_df, sales_df, on='CustomerID', how='left')
active_customers = customers_with_sales.dropna(subset=['SaleID'])
print(customers_with_sales)
print(active_customers)

#Q17. Find median refund amount
median_refund = returns_df['RefundAmount'].median()
print(median_refund)

#Q18 Add column in Inventory for low stock (Stock < 20)
inventory_df['LowStock'] = inventory_df['Stock'] < 20
print(inventory_df)

#Q19 merge all datasets to create master view
master_view = full_sales_df.merge(inventory_df, on='ProductID', how='left')
print(master_view)

#Q20 Pivot sale data to show total SaleAmount by ProductName and City
pivot_table = sales_prod_cust_df.pivot_table(index='ProductName', columns='City', values='SaleAmount', aggfunc='sum', fill_value=0)
print(pivot_table)