"""Calculates the minimum fixed monthly payment needed in order pay
off a credit card balance within 12 months. We will not be dealing with a minimum monthly
payment rate.
"""

def main():
    balance = float(input("Enter the outstanding balance on your credit card: "))
    interest_rate = float(input("Enter the anual credit card interest rate as a decimal: "))
    month = 1
    payment = 0.0
    interest_paid = 0.0
    principal_paid = 0.0
    current_balance = balance
    
    while (current_balance > 0):
        month = 0
        current_balance = balance
        interest_paid = 0.0
        principal_paid = 0.0
        payment += 10
        while ((month < 12) and (current_balance > 0)):
            interest_paid = (interest_rate / 12.0) * current_balance
            principal_paid = payment - interest_paid
            current_balance -= principal_paid
            month += 1
       
    
    print("RESULT")
    print("Monthly payment to pay off debt in one year: {:.2f}".format(payment))
    print("Number of months needed: {}".format(month))
    print("Remaining balance: {:.2f}".format(current_balance))
    
    return 0

main()
