"""Calculate the credit card balance after one year if a person only pays the
minimum monthly payment required by the credit card company each month. 
For each month, print the minimum monthly payment, remaining balance, principle paid in the
format shown in the test cases below. All numbers should be rounded to the nearest penny.
Finally, print the result, which should include the total amount paid that year and the remaining
balance. 
"""

def main():
    balance = float(input("Enter the outstanding balance on your credit card: "))
    interest_rate = float(input("Enter the anual credit card interest rate as a decimal: "))
    payment_rate = float(input("Enter the minimum monthly payment rate as a decimal: "))
    month = 1
    payment = 0.0
    interest_paid = 0.0
    principal_paid = 0.0
    total_paid = 0.0
    
    while (month < 13):
        payment = payment_rate * balance
        interest_paid = (interest_rate / 12.0) * balance
        principal_paid = payment - interest_paid
        balance -= principal_paid
        total_paid += payment
        print("Month: {}".format(month))
        print("Minimum monthly payment: ${:.2f}".format(payment))
        print("Principle paid: ${:.2f}".format(principal_paid))
        print("Remaining balance: ${:.2f}".format(balance))
        
        month += 1
    
    print("RESULT")
    print("Total amount paid: {:.2f}".format(total_paid))
    print("Remaining balance: {:.2f}".format(balance))
    
    return 0

main()
