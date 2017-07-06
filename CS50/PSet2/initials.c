#include <stdio.h>
#define MAX_NAME_LEN 100

int to_capitals(int letter);

int main(void) {
    char name[MAX_NAME_LEN];
    int i;
    
    printf("Name: ");
    fgets(name, MAX_NAME_LEN, stdin);
    
    i = 0;
    while (name[i] != '\0') {
        while (name[i] == ' ')          // skip spaces
            ++i;
        if (name[i] != '\0') {          // print first letter of word
            printf("%c", to_capitals(name[i]));
            while (name[i] != ' ') {    // skip other letters in word
                if (name[i] == '\0') {
                    printf("\n");
                    return 0;
                }
                ++i;
            }
        }   else
               break;
        ++i;
    }
    
    printf("\n");
    return 0;
}

int to_capitals(int letter) {       // if character is lower, return upper case, else return character. assumes input is letter
    if (letter >= 97 && letter <= 122)
        return letter - 32;
    else
        return letter;
}
