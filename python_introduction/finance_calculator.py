Monthly_income=int(input(Enter your monthly income: ))
monthly_expenses=int(input(Enter your total monthly expenses:))
monthly_savings= monthly_income-monthly_expenses
Projected_Savings = Monthly_Savings * 12 + (Monthly_Savings * 12 * 0.05)
print(f"Your monthly savings are: {monthly_savings}")
print(f"Projected savings after one year, with interest, is: {Projected_Savings}")
