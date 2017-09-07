/****************************************
 *  King, chapter 1, prog project 4     *
 *                                      *
 *  Takes a dollars amount and adds tax *
 ****************************************/
 
#include <stdio.h>
#include <stdlib.h>
 
#define MAX_INPUT 100
#define TAX_PERCENT 5
 
int main(void) {
    char user_input[MAX_INPUT];
    float dollars;
    
    printf("Enter amount in dollars: ");
    fgets(user_input, MAX_INPUT, stdin);
    dollars = strtof(user_input, NULL);
    
    printf("Amount after tax: %.2f\n", dollars + ((float)TAX_PERCENT * dollars) / 100);
    return 0;
}
