#include <stdio.h>
#include <stdlib.h>
#define INPUT_SIZE 3
#define GAP_SIZE 2

/* User inputs height, and the program prints a mario style tower with a gap in the middle. */
int main(void) {
    char input[INPUT_SIZE];
    char *nc;
    int height = -1;
    int i, j, k, gap;
    
    while (height < 0 || height > 23) {
        printf("Height: ");
        fgets(input, INPUT_SIZE + 2, stdin);    // + 2 to account for \0 and \n in buffer
        height = (int)strtol(input, &nc, 10);
    }
    
    for (i = 0; i < height; ++i) {
        for (j = 0; j < height - i - 1; ++j)
            printf(" ");
        for (k = 0; k < i + 1; ++k)
            printf("#");
        for (gap = 0; gap < GAP_SIZE; ++gap)
            printf(" ");
        for (k = 0; k < i + 1; ++k)
            printf("#");
        printf("\n");
    }
    
    return 0;
}
    
