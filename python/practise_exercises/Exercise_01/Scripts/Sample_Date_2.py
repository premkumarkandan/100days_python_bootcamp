import pandas as pd
import numpy as np
from random import choice, randint, uniform
from datetime import datetime, timedelta

# Set parameters for the data
num_rows = 10000  # Define the number of rows for a large dataset
categories = ["Electronics", "Apparel", "Home Goods", "Toys", "Automotive"]
products = {
    "Electronics": ["Laptop", "Smartphone", "Tablet", "Headphones"],
    "Apparel": ["Shirt", "Jacket", "Pants", "Shoes"],
    "Home Goods": ["Blender", "Toaster", "Vacuum Cleaner", "Microwave"],
    "Toys": ["Action Figure", "Puzzle", "Board Game", "Toy Car"],
    "Automotive": ["Car Battery", "Tire", "Oil Filter", "Spark Plug"]
}
customers = ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Hannah"]


# Function to generate random dates
def random_date(start, end):
    delta = end - start
    random_days = randint(0, delta.days)
    return start + timedelta(days=random_days)


# Define the date range
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

# Generate data
data = {
    "Customer": [choice(customers) for _ in range(num_rows)],
    "Category": [choice(categories) for _ in range(num_rows)],
    "Product": [],
    "Quantity": [randint(1, 10) for _ in range(num_rows)],
    "Price": [round(uniform(5.0, 500.0), 2) for _ in range(num_rows)],
    "Total_Sales": [],
    "Date": [random_date(start_date, end_date) for _ in range(num_rows)]
}

# Generate Product based on Category
for i in range(num_rows):
    category = data["Category"][i]
    product = choice(products[category])
    data["Product"].append(product)

# Introduce NaN values in 5% of the Quantity and Price columns
nan_indices_quantity = np.random.choice(num_rows, size=int(num_rows * 0.05), replace=False)
nan_indices_price = np.random.choice(num_rows, size=int(num_rows * 0.05), replace=False)

for idx in nan_indices_quantity:
    data["Quantity"][idx] = np.nan
for idx in nan_indices_price:
    data["Price"][idx] = np.nan

# Calculate Total Sales, setting it to 0 with a 10% chance
for i in range(num_rows):
    quantity = data["Quantity"][i] if not pd.isna(data["Quantity"][i]) else 0
    price = data["Price"][i] if not pd.isna(data["Price"][i]) else 0
    total_sales = round(quantity * price, 2)
    data["Total_Sales"].append(total_sales if randint(0, 10) > 1 else 0)  # 10% chance of Total_Sales being 0

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV if needed
df.to_csv("large_sales_data.csv", index=False)

print("DataFrame generated successfully:")
print(df.head())