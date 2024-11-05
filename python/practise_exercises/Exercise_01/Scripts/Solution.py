# Exercise: Analyzing Sales Data
# Task 1: Data Cleaning
# Task 2: Data Manipulation
# Task 3: Data Analysis

# Importing pandas library
import pandas as pd

# Reading the data from sales_data.csv into a DataFrame
sales_data = pd.read_csv('/Users/premkumarkandanmeena/Documents/python/100days_python_bootcamp/python/'
                         'practise_exercises/Exercise_01/Data/Sales_data.csv')

# Display all columns in the terminal (for easier inspection)
pd.set_option('display.max_columns', None)

# Step 1: Handle Missing Values
# Fill missing values in 'Quantity' and 'Price' with 0
sales_data[["Quantity", "Price"]] = sales_data[["Quantity", "Price"]].fillna(0)

# Step 2: Remove Rows with Total Sales = 0
# Create a new DataFrame excluding rows where 'Total_Sales' is 0
new_sales_data = sales_data.loc[sales_data["Total_Sales"] != 0]

# Step 3: Correct Data Types
# Convert 'Quantity', 'Price', and 'Total_Sales' to numeric data types
new_sales_data.loc[:, ["Quantity", "Price", "Total_Sales"]] = (new_sales_data[["Quantity", "Price", "Total_Sales"]]
                                                               .apply(pd.to_numeric, errors="coerce"))

# Convert the 'Date' column to datetime, replacing invalid entries with NaT
new_sales_data["Date"] = pd.to_datetime(new_sales_data["Date"], errors="coerce")

# Display the cleaned DataFrame to verify the results
print(new_sales_data.head())

# Adding a new column Total_Cost that calculates Quantity * Price.
new_sales_data["Total_Cost"] = new_sales_data["Quantity"] * new_sales_data["Price"]
print(new_sales_data)

# Correcting discrepancies between Total_Sales and Total_Cost where Total_Sales may not match Quantity * Price.
new_sales_data.loc[new_sales_data["Total_Sales"] != new_sales_data["Total_Cost"], "Total_Sales"] = new_sales_data["Total_Cost"]
print(new_sales_data)

# Grouping by Customer and Category, then summing Total_Sales for each group.
total_sales_by_customer_category = new_sales_data.groupby(["Customer", "Category"])["Total_Sales"].sum().reset_index()
print(total_sales_by_customer_category)

# Filtering for rows where Total_Sales is greater than 200.
filtered_sales_date = new_sales_data.loc[new_sales_data["Total_Sales"] > 200]
print(filtered_sales_date)

