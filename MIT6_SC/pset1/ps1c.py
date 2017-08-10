"""find the smallest monthly payment to the cent (no more multiples of$10) 
such that we can pay off the debt within a year.
"""

def main():
    balance = float(input("Enter the outstanding balance on your credit card: "))
    interest_rate = float(input("Enter the anual credit card interest rate as a decimal: "))
    month = 1
    payment = 0.0
    interest_paid = 0.0
    principal_paid = 0.0
    current_balance = balance
    
    lower_payment = balance / 12
    higher_payment = (balance * (1 + (interest_rate / 12.0)) ** 12.0) / 12.0
    
    while (current_balance > 0):
        month = 0
        current_balance = balance
        interest_paid = 0.0
        principal_paid = 0.0      
        payment = (lower_payment + higher_payment) / 2.0
        while ((month < 12) and (current_balance > 0)):
            interest_paid = (interest_rate / 12.0) * current_balance
            principal_paid = payment - interest_paid
            current_balance -= principal_paid
            month += 1
        if (current_balance > 0):
            lower_payment = payment
        else:
            higher_payment = payment
            
        if (higher_payment - lower_payment > 0.001): # Small enough search space found
            break
            
    payment = lower_payment
    month = 0
    current_balance = balance
    interest_paid = 0.0
    principal_paid = 0.0
    
    while (current_balance > 0):
        month = 0
        current_balance = balance
        interest_paid = 0.0
        principal_paid = 0.0
        payment += 0.01
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
