def main():
    """
    Checks the validity of a credit card number by using Luhn's
    algorithm, and comparing the number of digits as well as the
    first digit or first two digits.
    Recognizes: MasterCard, VISA, American Express.
    """
    
    number = int(input("Enter the credit card number, without hyphens: "))
    num_digits = how_many_digits(number)
    fd = get_first_n_digits(number, 1) # First digit.
    ftd = get_first_n_digits(number, 2) # First two digits.
    
    if not is_valid(number):
        print("IVALID")
        exit(0)
    
    if num_digits == 15:
        if (ftd == 34 or ftd == 37):
            print("AMEX")
        else:
            print("INVALID")
    
    elif num_digits == 16:
        if (51 <= ftd <= 55):
            print("MASTERCARD")
        elif fd == 4:
            print("VISA")
        else:
            print("INVALID")
    
    elif num_digits == 13:
        if fd == 4:
            print("VISA")
        else:
            print("INVALID")
    
    else:
        print("INVALID")
    
    exit(0)
    
def is_valid(card_number):
    """
    Returns True if the credit card number's Luhn number ends with 0,
    False otherwise.
    """
    
    return ((checksum(card_number) % 10) == 0)
    

def checksum(number):
    """
    Returns the Luhn algorith sum of a given credit card number.
    """
    
    check_sum = 0
    temp = number
    while (temp >= 1):
        temp //= 10
        check_sum += add_digits((temp%10) * 2)
        temp //= 10
    
    temp = number
    while (temp >= 1):
        check_sum += temp % 10
        temp //= 100
    
    return check_sum

def add_digits(number):
    """
    Returns the sum of a number's digits.
    """
    
    dsum = 0
    temp = number
    while(temp >= 1):
        dsum += temp % 10
        temp //= 10
    return dsum
    
    
def how_many_digits(number):
    """
    Returns the number of digits of a given number.
    """
    
    temp = number
    digits = 0
    
    while (temp >= 1):
        temp //= 10
        digits += 1
    
    return digits


def get_first_n_digits(number, n):
    """
    Takes a number and returns the first n of its digits.
    """
    
    temp = number
    while (temp >= 10**n):
        temp //= 10
    return temp


main() 
