/******************************************************
 *  King, chapter 1, prog project 7                   *
 *                                                    *
 *  Takes dollar amount and prints minimum number of  * 
 *  bills necessary to pay it.                        *
 ******************************************************/
 
#include <stdio.h>
#include <stdlib.h>
#define MAX_INPUT 100

int main(void) {
    char user_input[MAX_INPUT];
    unsigned int dollars, twenties, tens, fives, ones;
    
    printf("Enter amount in dollars: ");
    fgets(user_input, MAX_INPUT, stdin);
    dollars = (unsigned int)strtod(user_input, NULL);
    
    twenties = tens = fives = ones = 0;
    
    while (dollars > 0) {
        if (dollars >= 20)        {
            dollars -= 20;
            twenties++;
        } else if (dollars >= 10) {
            dollars -= 10;
            tens++;
        } else if (dollars >= 5)  {
            dollars -= 5;
            fives++;
        } else                    {
            dollars -= 1;
            ones++;
        }
    }
    
    printf("$20 bills: %d\n$10 bills: %d\n $5 bills: %d\n $1 bills: %d\n", twenties, tens, fives, ones);
    return 0;
}
        
        
