/******************************************************
 *  King, chapter 1, prog project 5,6                 *
 *                                                    *
 *  Takes valid x value and evaluates the polinomial  * 
 *          3x^5 + 2x^4 - 5x^3 - x^2 + 7x             *
 ******************************************************/
 

#include <stdio.h>
#include <stdlib.h>
#define MAX_INPUT 100

int main(void) {
    char user_input[MAX_INPUT];
    float x;
    
    printf("Enter valid x value: ");
    fgets(user_input, MAX_INPUT, stdin);
    x = strtof(user_input, NULL);
    
    printf("p(%.2f) = %.2f\n", x, ((((3.0 * x + 2) * x - 5.0) * x - 1.0) * x + 7.0) * x - 6);
    return 0;
}
