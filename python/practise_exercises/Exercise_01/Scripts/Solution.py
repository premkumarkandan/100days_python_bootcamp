# Exercise: Analyzing Sales Data
# Task 1: Data Cleaning
# Task 2: Data Manipulation
# Task 3: Data Analysis

# Reading the data from sales_data.csv into a Pandas DataFrame (pd).
import pandas as pd

sales_data = pd.read_csv('/Users/premkumarkandanmeena/Documents/python/100days_python_bootcamp/python/'
                         'practise_exercises/Exercise_01/Data/Sales_data.csv')

# Displaying all columns in the python terminal
pd.set_option('display.max_columns', None)

# Check for missing values and Fill missing values
sales_data[["Quantity", "Price"]] = sales_data[["Quantity", "Price"]].fillna(0)
sales_data.loc[sales_data["Total_Sales"] != 0, "Total_Sales"] = sales_data["Total_Sales"].fillna(100)

# Remove any rows where Total_Sales is 0
new_sales_data = sales_data.loc[sales_data["Total_Sales"] != 0]

new_sales_data[["Quantity", "Price", "Total_Sales"]] = (new_sales_data[["Quantity", "Price", "Total_Sales"]]
                                                        .apply(pd.to_numeric, errors="coerce"))
print(new_sales_data[["Quantity", "Price", "Total_Sales"]])
(new_sales_data["Date"]) = pd.to_datetime(new_sales_data["Date"], errors="coerce")

