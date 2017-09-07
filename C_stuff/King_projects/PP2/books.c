/***************************************************
 * books: breaks down an ISBN entered by the user. *
 ***************************************************/

#include <stdio.h>

int main(void)
{
    int prefix, identifier, code, number, digit;
    
    printf("Enter ISBN: ");
    scanf("%d-%d-%d-%d-%d", &prefix, &identifier, &code, &number, &digit);
    
    printf("GS1 prefix: %d\n", prefix);
    printf("Group identifier: %d\n", identifier);
    printf("Publisher code: %d\n", code);
    printf("Item number: %d\n", number);
    printf("Check digit: %d\n", digit);
    
    return 0;
}
    

