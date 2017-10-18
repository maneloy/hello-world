#include <stdio.h>
#include <stdlib.h>                 // compilation raises undefined error on "round" function
#include <math.h>                   // unless '-lm' is specified in terminal
#define MAX_INPUT 100
               
int main(void) {
    float change;
    int coins, cents;
    char input[MAX_INPUT];
    char *not_converted;

    change = -1;
    coins  = 0;
    cents = 0;

    printf("O hai! How much change is owed?\n");
    while (change < 0) {
        fgets(input, MAX_INPUT, stdin);
        change = strtof(input, &not_converted);
        if (change > 0)
            break;
        printf("How much change is owed?\n");
    }

    change = round(change * 100);   // convert to cents
    cents = change;                 // convert to int to avoid float imprecision

    while (cents > 0) {
        if (cents >= 25) {
            cents -= 25;
            ++coins;
        }

        else if (cents >= 10) {
            cents -= 10;
            ++coins;
        }

        else if (cents >= 5) {
            cents -= 5;
            ++coins;
        }

        else {
            cents -= 1;
            ++coins;
        }
    }

    printf("%d coins needed\n", coins);
    return 0;
}
