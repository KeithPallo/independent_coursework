# Script to find the smallest monthly payment to the cent using binary search


def test(number_of_months, balance, monthly_payment, monthly_interest):
    # Same function from problem 2 of hw 2 - checks remaining balance after input duration with specific
    # simple interest inputs

    for n in range (0, number_of_months):
        monthly_unpaid = balance - monthly_payment
        balance = monthly_unpaid + (monthly_interest * monthly_unpaid)
    return balance


# Initialize basic interest rate variables
balance = 3329
annualInterestRate = 0.2
stop = 0
number_of_months = 12
monthly_interest = annualInterestRate / 12

# Create lower and upper bounds
lower_bound = balance / 12
upper_bound = (balance * (1+monthly_interest)**12)/12

# Define the first monthly payment guess to be in the middle of there two bounds
monthly_payment = (lower_bound+upper_bound) / 2

# Calculate the first remaining balance when using the middle "guess" calculated above
check = test(number_of_months, balance, monthly_payment, monthly_interest)

# Perform classic bisection search
while stop == 0:

    # If the remaining balance is too large, then reset the new monthly payment to be the value in the "middle"
    # of the current upper bound and the last monthly payment that was used in this round
    if check > 0:
        lower_bound = monthly_payment
        monthly_payment = (lower_bound + upper_bound)/2
        check = test(number_of_months, balance, monthly_payment, monthly_interest)

    # If the remaining balance is too small, then reset the new monthly payment to be the value in the "middle"
    # of the current lower bound and the last monthly payment that was used in this round
    if check < 0:
        upper_bound = monthly_payment
        monthly_payment = (lower_bound + upper_bound)/2
        check = test(number_of_months, balance, monthly_payment, monthly_interest)

    # If the remaining balance is 0, then lower the upper bound by 1, and recalculate the monthly payment
    if check == 0:
        upper_bound = upper_bound - 1
        monthly_payment = (lower_bound + upper_bound)/2
        print("Was equal to 0")

    # If the remaining balance is < 0, then check to see if the next lowest (by cent) payment
    # would fail to pay off the balance. If it does fail, the solution has been found.
    if check < 0 and test(number_of_months, balance, monthly_payment - .01, monthly_interest) >= 0:
        final = monthly_payment
        stop = 1

    # If the remaining balance is > 0, then check to see if the next highest (by cent) payment
    # would fail to pay off the balance. If it does fail, the solution has been found.
    if check > 0 and test(number_of_months, balance, monthly_payment + .01, monthly_interest) <= 0:
        final = monthly_payment + .01
        stop = 1

# Print the final term
print(round(final,2))
