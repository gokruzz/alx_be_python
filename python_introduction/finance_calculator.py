# a script that will calculate the user’s monthly savings based on inputted monthly income and expenses. It will then project these savings over a year, assuming a fixed interest rate, to demonstrate compound interest’s effect on savings.

# Prompt the user for financial inputs
income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = income - expenses

# Project annual savings with 5% interest
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Convert to integers for display
monthly_savings = int(monthly_savings)
projected_savings = int(projected_savings)

# Display the results
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")

