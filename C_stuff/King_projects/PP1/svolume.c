/**************************************
 *  King, chapter 1, prog project 2,3 *
 *                                    *
 *  Prints volume of sphere (r = 10)  *
 **************************************/
 
#include <stdio.h>
#include <stdlib.h>

#define PI 3.1415
#define MAX_STRING 30
 
int main(void) {
    char radius[MAX_STRING];
    float rad;
    
    printf("Enter sphere radius: ");
    fgets(radius, MAX_STRING, stdin);
    rad = strtof(radius, NULL);
    
    printf("Radius: %.0f, volume of sphere: %.2f\n", rad, (4.0/3.0)*PI*rad*rad*rad);
    return 0;
}
