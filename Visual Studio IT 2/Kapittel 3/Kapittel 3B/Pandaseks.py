import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
filnavn = "CSV files\\ecommerce_sales(CSV).csv"
df = pd.read_csv(filnavn, delimiter=";", encoding="utf-8")
print(df.head())

# Total revenue
# Group by Product and sum the Total sales og vis de 5 mest solgte
# Orders by payment method
# Average order value
# City with highest revenue
# Check for missing values
# Drop duplicates
# Most popular product category
# Group by Month and sum Total revenue
# Top 5 products by revenue
# Monthly revenue bar chart
# Payment method pie chart

# Print the total number of unique orders
print("Total Orders:", df['OrderID'].nunique())

# Calculate the total revenue
total_revenue = df['Total'].sum()

# Group by Product and sum the Total sales, then get the top 5 products by revenue
top_products = df.groupby('Product')['Total'].sum().sort_values(ascending=False).head(5)

# Print the most popular product category
print("Most popular product category:", df['ProductCategory'].value_counts().idxmax())

# Group by ProductCategory and sum the Total sales, then print the category with the highest revenue
category_revenue = df.groupby('ProductCategory')['Total'].sum()
print("Category with highest revenue:", category_revenue.idxmax(), ":", category_revenue.max())

# Print the count of each payment method
print(df['PaymentMethod'].value_counts())

# Group by City and sum the Total sales
city_revenue = df.groupby('City')['Total'].sum()

# Check for missing values in each column
print(df.isnull().sum())

# Drop duplicate rows
df = df.drop_duplicates()

# Calculate the average order value
aov = df['Total'].mean()

# Ensure OrderDate is in datetime format
df['OrderDate'] = pd.to_datetime(df['OrderDate'])

# Extract the month from OrderDate
df['Month'] = df['OrderDate'].dt.month

# Group by Month and sum the Total sales
monthly_revenue = df.groupby('Month')['Total'].sum()

# Print the monthly revenue
print(monthly_revenue)

# Group by Product and sum the Total sales, then sort by revenue in descending order
product_revenue = df.groupby('Product')['Total'].sum().sort_values(ascending=False)

# Plot a bar chart of monthly revenue
monthly_revenue.plot(kind='bar', title='Monthly Revenue')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.show()

# Plot a pie chart of payment methods
df['PaymentMethod'].value_counts().plot(kind='pie', autopct='%1.1f%%', title='Payment Methods')
plt.show()

# Plot a pie chart of all products
df['Product'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('All Products')
plt.show()