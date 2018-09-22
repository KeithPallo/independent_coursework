# Finds the remaining balance in an account when using simple interest

# Initialize basic interest rate variables
balance = 42;
annualInterestRate = 0.2;
monthlyPaymentRate = 0.04

# Define monthly interest equation
monthly_interest = (annualInterestRate / 12)

# Define number of months in the desired period, which is a year
number_of_months = 12

# For each month, calculate the new balance accounting for monthly basic interest
for i in range (1, number_of_months+1):
    monthly_payment = balance * monthlyPaymentRate
    balance = (balance - monthly_payment) + (monthly_interest * (balance - monthly_payment))

# Round the balance and return the appropriate information
balance_print = round(balance,2)
print("Remaining balance: ",end='')
print(balance_print)