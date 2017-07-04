#include <stdio.h>
#include <stdlib.h>
#define MAX_INPUT 100

int power(int a, int b);
int add_digits(int number);
int checksum(long long int number);
int validate_card(long long int number);
int how_many_digits(long long int number);
int get_first_n_digits(long long int number, int n);

/* Checks the validity of a credit card number by using Luhn's algorithm and
    comparing the number of digits and the first or first two digits. 
    Recognizes VISA, MasterCard and American Express. */
int main(void) {
    int num_digits, fd, ftd;
    long long int num_card;
    char user_input[MAX_INPUT];
    char *not_converted;
    
    printf("Number (without hyphens): ");
    fgets(user_input, MAX_INPUT, stdin);
    num_card = strtoll(user_input, &not_converted, 10);
    
    if (!validate_card(num_card)) {
        printf("INVALID\n");
        return 0;
    }
    
    num_digits = how_many_digits(num_card);
    fd = get_first_n_digits(num_card, 1);           // first digit
    ftd = get_first_n_digits(num_card, 2);          // first two digits
    
    switch(num_digits) {
        case 15:
            if (ftd == 34 || ftd == 37)
                printf("AMEX\n");
            else
                printf("INVALID\n");
            break;
            
        case 16:
            if (ftd == 51 || ftd == 52 || ftd == 53 || ftd == 54 || ftd == 55)
                printf("MASTERCARD\n");
            else if (fd ==  4)
                printf("VISA\n");           
            else
                printf("INVALID\n");
            break;
            
        case 13:
            if (fd == 4)
                printf("VISA\n");
            else
                printf("INVALID\n");
            break;
        
        default:
            printf("INVALID\n");                
    }
    
    return 0;      
}

int power(int a, int b) {
    int power = 1;
    for (int i = 0; i < b; ++i)
        power *= a;
    return power;
}

int add_digits(int number) {                // Add a number's digits
    int sum, temp;
    
    sum = 0;
    temp = number;
    while (temp >= 1) {
        sum += temp % 10;
        temp /= 10;
    }
    
    return sum;
}

int checksum(long long int number) {        // Luhn's algorithm
    long long int temp;
    int sum;
    
    sum = 0;
    temp = number;
    while (temp >= 1) {
        temp /= 10;
        sum += add_digits((temp % 10) * 2);
        temp /= 10;
    }
    
    temp = number;
    while (temp >= 1) {
        sum += temp%10;
        temp /= 10;
        temp /= 10;
    }
    
    return sum;
}

int validate_card(long long int number) {       // Valid if Luhn's result ends in 0
    return ((checksum(number) % 10) == 0); 
}

int how_many_digits(long long number) {         // Counts number of digits in number
    long long int temp;
    int digits = 0;
    
    temp = number;
    while (temp >= 1) {
        ++digits;
        temp /= 10;
    }
    
    return digits;
}

int get_first_n_digits(long long int number, int n) {
    long long int temp;
    
    temp = number;
    while (temp >= power(10, n))
        temp /= 10;   
    return temp;
}
    
