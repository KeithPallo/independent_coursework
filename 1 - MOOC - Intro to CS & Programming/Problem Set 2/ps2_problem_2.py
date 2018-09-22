# Script to determine the minimum monthly payment required to pay off a balance in a years time
# This is a brute force method, where we start at a monthly payment that clearly would not 0 out the balance
# and increase payment value until the remaining balance is either 0 or less than 0

# Initialize basic inputs

balance = 3329
annualInterestRate = 0.2
pay_helper = 10  # This variable will be increased during the
monthly_interest = annualInterestRate / 12
check = 0
i = 1
number_of_months = 12


def test(number_of_months, balance, monthly_payment, monthly_interest):
    # Function to calculate the remaining balance after a specified duration when paying a specific
    # ammount per month, starting from a predetermine balance (debt)
    for n in range (0, number_of_months):
        monthly_unpaid = balance - monthly_payment
        balance = monthly_unpaid + (monthly_interest * monthly_unpaid)
    return balance


# Control loop statement that keeps incrementing the amount paid per month and calling
# the test function to see if the balance has been paid down

while check == 0:
    monthly_payment = i * pay_helper
    final = test(number_of_months, balance, monthly_payment, monthly_interest)
    if final <= 0:
        answer = monthly_payment
        check = 1
    if final > 0:
        i += 1

# Print the calculated min payment based on the input parameters

print("Lowest Payment: ",end='')
print(answer)