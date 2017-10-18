#include <stdio.h>
#include <stdlib.h>
#define USAGE_RATE 12   // in bottles per minute
#define MAX_INPUT 3     // unlikely to spend >999 min in shower

/* Asks user how long it takes them to shower in minutes,
    returns the water usage rate in bottles. */
int main(void) {
    char minutes[MAX_INPUT];
    char *ptr;
    printf("Minutes: ");
    fgets(minutes, MAX_INPUT, stdin);
    printf("\nBottles: %li\n", strtol(minutes, &ptr, 10) * USAGE_RATE);
}
