import pandas as pd

# Data for Main Sheet
main_sheet_data = {
    "Summary": ["Credit Card Balance Status", "Recurring Expense Status"],
    "Value": [0, 0]  # Placeholder values
}
main_sheet_df = pd.DataFrame(main_sheet_data)

# Data for Credit Cards & Debts Sheet
credit_cards_debts_data = {
    "Card/Loan Name": ["Card A", "Card B", "Loan 1"],
    "Balance Due": [1200, 500, 10000],
    "Interest Rate (%)": [18, 20, 5],
    "Monthly Payment": [100, 50, 200]
}
credit_cards_debts_df = pd.DataFrame(credit_cards_debts_data)

# Data for Planned Future Expenses Sheet
planned_future_expenses_data = {
    "Expense Name": ["Vacation", "New Car", "Home Renovation"],
    "Estimated Cost": [1500, 20000, 5000],
    "Expected Date": ["2024-06-01", "2025-01-01", "2024-09-01"]
}
planned_future_expenses_df = pd.DataFrame(planned_future_expenses_data)

# Data for Recurring Expenses Sheet
recurring_expenses_data = {
    "Expense Name": ["Rent", "Utilities", "Gym Membership", "Internet"],
    "Monthly Cost": [1000, 200, 50, 60],
    "Payment Date": ["1st", "5th", "10th", "15th"]
}
recurring_expenses_df = pd.DataFrame(recurring_expenses_data)

# Specify the output file name
output_file = "Budget_Sheet_Sample.xlsx"

# Write data to Excel with separate sheets
with pd.ExcelWriter(output_file) as writer:
    main_sheet_df.to_excel(writer, sheet_name='Main Sheet', index=False)
    credit_cards_debts_df.to_excel(writer, sheet_name='Credit Cards & Debts', index=False)
    planned_future_expenses_df.to_excel(writer, sheet_name='Planned Future Expenses', index=False)
    recurring_expenses_df.to_excel(writer, sheet_name='Recurring Expenses', index=False)

print(f"Excel file '{output_file}' created successfully!")