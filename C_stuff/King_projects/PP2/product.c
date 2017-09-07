/*********************************************
 * product: formats product information      *
 *          entered by the user.             *
 *********************************************/
 
#include <stdio.h>

int main(void)
{
    int day, month, year, item_number;
    float price;
    
    printf("Enter item number: ");
    scanf("%d", &item_number);
    
    printf("Enter unit price (must be $9999.99 or less): ");
    scanf("%f", &price);   
    while (price > 9999.99)
    {
        printf("Only quantities less than 9999.99 are accepted, please try again: ");
        scanf("%f", &price);    
    }
    
    printf("Enter purchase date (mm/dd/yyyy): ");
    scanf("%d / %d / %d", &month, &day, &year);
    
    printf("Item\t\tUnit\t\tPurchase\n");
    printf("    \t\tPrice\t\tDate\n");
    printf("%-d \t\t$%.2f\t\t%.2d/%.2d/%.4d\n", item_number, price, month, day, year);
    
    return 0;
}
