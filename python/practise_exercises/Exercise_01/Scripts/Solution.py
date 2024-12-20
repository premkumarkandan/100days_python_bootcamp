# Exercise: Analyzing Sales Data
# Task 1: Data Cleaning
# Task 2: Data Manipulation
# Task 3: Data Analysis

# Importing pandas library
import pandas as pd

# Reading the data from sales_data.csv into a DataFrame
sales_data = pd.read_csv('/Users/premkumarkandanmeena/Documents/python/100days_python_bootcamp/python/'
                         'practise_exercises/Exercise_01/Data/large_sales_data.csv')

# Display all columns in the terminal (for easier inspection)
pd.set_option('display.max_columns', None)

# ====================== Task 1: Data Cleaning ======================= #

# Step 1: Handle Missing Values
# Fill missing values in 'Quantity' and 'Price' with 0
sales_data[["Quantity", "Price"]] = sales_data[["Quantity", "Price"]].fillna(0)

# Step 2: Remove Rows with Total Sales = 0
# Create a new DataFrame excluding rows where 'Total_Sales' is 0
new_sales_data = sales_data.loc[sales_data["Total_Sales"] != 0]

# Step 3: Correct Data Types
# Convert 'Quantity', 'Price', and 'Total_Sales' to numeric data types
new_sales_data.loc[:, ["Quantity", "Price", "Total_Sales"]] = new_sales_data[["Quantity", "Price", "Total_Sales"]].apply(
    pd.to_numeric, errors="coerce"
)

# Convert the 'Date' column to datetime, replacing invalid entries with NaT
new_sales_data["Date"] = pd.to_datetime(new_sales_data["Date"], errors="coerce")

# ================== Task 2: Data Manipulation ===================== #

# Step 4: Add a New Column Total_Cost
# Calculating Total_Cost as Quantity * Price
new_sales_data["Total_Cost"] = new_sales_data["Quantity"] * new_sales_data["Price"]

# Step 5: Correct Total_Sales Where Needed
# Correcting Total_Sales where it doesn't match Total_Cost
new_sales_data.loc[new_sales_data["Total_Sales"] != new_sales_data["Total_Cost"], "Total_Sales"] = (
    new_sales_data)["Total_Cost"]

# Step 6: Group Data by Customer and Category
# Group by Customer and Category, then sum Total_Sales
total_sales_by_customer_category = new_sales_data.groupby(["Customer", "Category"])["Total_Sales"].sum().reset_index()

# Step 7: Filter Rows Where Total_Sales > 2000
# Filtering for rows where Total_Sales is greater than 2000
filtered_sales_date = new_sales_data.loc[new_sales_data["Total_Sales"] > 2000]

# ==================== Task 3: Data Analysis ===================== #

# Step 8: Find the Top 3 Products by Total Sales
# Group by Product and calculate total sales, sort descending, get top 3
top_3_products = new_sales_data.groupby("Product")["Total_Sales"].sum().sort_values(ascending=False).head(3).reset_index()

# Print top 3 products
print("Top 3 Products by Total Sales:")
print(top_3_products)

# Step 9: Calculate Average Quantity Sold by Category
# Group by Category and calculate average quantity sold
average_quantity_by_category = new_sales_data.groupby("Category")["Quantity"].mean().reset_index()

# Print average quantities
print("\nAverage Quantity Sold by Category:")
print(average_quantity_by_category)

# Step 10: Identify the Month with the Highest Sales
# Extract the month from the Date column
new_sales_data["Month"] = new_sales_data["Date"].dt.month

# Group by month and calculate total sales
monthly_sales = new_sales_data.groupby("Month")["Total_Sales"].sum().reset_index()

# Find the month with the highest sales
highest_sales_month = monthly_sales.loc[monthly_sales["Total_Sales"].idxmax()]

# Print the result
print("\nMonth with the Highest Sales:")
print(highest_sales_month)