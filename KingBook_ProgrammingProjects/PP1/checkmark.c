/********************************************
 * King, chapter 1, prog project 1          * 
 * Prints a check mark of default height 6. *
 ********************************************/
 
#include <stdio.h>

int main(void) {
    
    int height = 6;             // minimum: 4
    int rheight = height;
    int lheight = rheight / 2;
    int padding = lheight + rheight - 1;
    int i, j, k, aux;
    i = j = k = 0;
    
    aux = (height % 2 == 0) ? 3:4;
    
    while (rheight > lheight) {          
        for (i = 0; i < padding - 1; i++)
            printf(" ");
        padding--;
        rheight--;
        printf("*\n");
    }
    
    while (k < lheight - 1) {
        for (i = 0; i < k; i++)
            printf(" ");
        printf("*");
        for (i = 0; i < (height-aux) - j- k; i++)
            printf(" ");
        printf("*\n");
        k++;
        j++;
    }
    
    for (i = 0; i < lheight - 1; i++) 
        printf(" ");
    printf("*\n");
        
    return 0;
}
