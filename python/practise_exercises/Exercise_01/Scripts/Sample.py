import pandas as pd

# Sample data
data = {
    'Order_ID': [1, 2, 3, 4, 5, 6, 7, 8],
    'Date': ['2023-01-15', '2023-02-02', '2023-02-15', '2023-03-10', '2023-03-15', '2023-04-05', '2023-05-10', '2023-06-20'],
    'Customer': ['John Doe', 'Jane Roe', 'John Doe', 'Alice', 'Bob', 'Jane Roe', 'Alice', 'John Doe'],
    'Category': ['Apparel', 'Apparel', 'Electronics', 'Electronics', 'Apparel', 'Electronics', 'Apparel', 'Electronics'],
    'Product': ['T-Shirt', 'Jacket', 'Smartphone', 'Headphones', 'T-Shirt', 'Laptop', 'Jacket', 'Smartphone'],
    'Quantity': [3, 1, 2, 4, 5, 1, 2, 3],
    'Price': [20.0, 100.0, 500.0, 50.0, 20.0, 800.0, 100.0, 500.0],
    'Total_Sales': [60.0, 100.0, 1000.0, 200.0, 100.0, 800.0, 200.0, 1500.0]
}

# Create DataFrame and save as CSV
df = pd.DataFrame(data)
df.to_csv('Exercise_01_Sales_data.csv', index=False)
print("CSV file 'Exercise_01_Sales_data.csv' has been created successfully.")
