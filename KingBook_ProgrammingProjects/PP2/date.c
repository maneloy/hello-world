/*********************************************
 * date: accepts a date of format mm/dd/yyyy *
 *       and prints it in format yyyymmdd    *
 *********************************************/
 
#include <stdio.h>

int main(void)
{
    int day, month, year;
    
    printf("Enter a date (mm/dd/yyyy): ");
    scanf("%d / %d / %d", &month, &day, &year);
    
    printf("%4d%.2d%.2d\n", year, month, day);
    
    return 0;
}
