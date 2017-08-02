/******************************************************
 *  King, chapter 1, prog project 8                   *
 *                                                    *
 *  Calculates the remaining balance on a loan after  * 
 *  a certain number (default 3) of monthly payments. *
 ******************************************************/
 
#include <stdio.h>
#include <stdlib.h>

#define MAX_INPUT 100
#define MONTHS 3

int main(void) {
    char input1[MAX_INPUT], input2[MAX_INPUT], input3[MAX_INPUT];
    float balance, rate, payment;
    
    printf("Enter amount of loan: ");
    fgets(input1, MAX_INPUT, stdin);
    balance = strtof(input1, NULL);
    
    printf("Enter interest rate: ");
    fgets(input2, MAX_INPUT, stdin);
    rate = (strtof(input2, NULL) / 100) / 12; // monthly interest rate
    
    printf("Enter monthly payment: ");
    fgets(input3, MAX_INPUT, stdin);
    payment = strtof(input3, NULL);
    
    for (int i = 0; i < MONTHS; i++) {
        balance += balance * rate;
        balance -= payment;
        printf("Balance remaining after payment %d: $%.2f\n", i + 1, balance);
    }
    
    return 0;
}
        
