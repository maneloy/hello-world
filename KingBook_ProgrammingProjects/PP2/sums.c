/************************************************************
 * sums: prompts the user to enter the numbers from 1 to 16 *
 *       in any order, then prints a 4x4 square with them   *
 *       as well as the sums of the rows, columns, and      *
 *       diagonals.                                         *
 ************************************************************/

#include <stdio.h>

int main(void)
{
    int i, j, sum_rows, sum_columns, sum_diag;
    int table[4][4];
    
    i = j;
    sum_rows = 0;
    sum_columns = 0;
    sum_diag = 0;
    
    printf("Enter the numbers from 1 to 16 in any order: ");
    for (i = 0; i < 4; i++)             // initialize table
    {
        for(j = 0; j < 4; j++)
        {
            scanf("%d", &table[i][j]);
        }
    }
    
    printf("\n");
    
    for (i = 0; i < 4; i++)             // print table
    {
        for(j = 0; j < 4; j++)
        {
            printf("%3d", table[i][j]);
            if (j == 3)
            {
                printf("\n");
            }
        }
    }
    
    printf("Row sums: ");               // row sums
    for (i = 0; i < 4; i++)
    {
        for(j = 0; j < 4; j++)
        {
            sum_rows += table[i][j];
        }
        printf("%d ", sum_rows);
        sum_rows = 0;
    }
    
    printf("\nColumn sums: ");          // column sums
    for (i = 0; i < 4; i++)
    {
        for(j = 0; j < 4; j++)
        {
            sum_columns += table[j][i];
        }
        printf("%d ", sum_columns);
        sum_columns = 0;
    }
    
    printf("\nDiagonal sums: ");        // diagonal sums
    for (i = 3; i > -1; i--)
    {
        sum_diag += table[i][i];
    }
    printf("%d ", sum_diag);
        
    sum_diag = 0;
    for (i = 0; i < 4; i++)
    {        
        sum_diag += table[i][i];
    }
    printf("%d\n", sum_diag);
    
    return 0;
}
    
    
