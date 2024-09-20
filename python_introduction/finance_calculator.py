monthly_income = float(input('Enter your monthly income: '))
total_monthly_expenses = float(input('Enter your total monthly expenses: '))

Monthly_Savings = monthly_income - total_monthly_expenses 

Projected_Savings = Monthly_Savings * 12 +( Monthly_Savings * 12 * 0.05)

print(f"Your monthly savings are: ${Monthly_Savings:.2f}")
print(f"Projected annual savings after interest: ${Projected_Savings:.2f}")