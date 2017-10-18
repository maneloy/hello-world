#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_INPUT 300

char rotate(char letter, int key);

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: ./caesar k\n");
        return 1;
    }
    
    int key, i;
    char *not_converted;
    char user_input[MAX_INPUT];
    char output[MAX_INPUT];
    
    not_converted = 0;
    key = 0;
    key = strtol(argv[1], &not_converted, 10);
    
    printf("plaintext: ");
    fgets(user_input, MAX_INPUT, stdin);
    
    for (i = 0; i <= strlen(user_input); ++i)
        output[i] = rotate(user_input[i], key);   
    
    printf("ciphertext: %s\n", output);
    return 0;
}
    
char rotate(char letter, int key) {
    int alphabetical_index, i, increment, beginning, end;
    
    increment = (key % 26);    
    alphabetical_index = 0;
    if (letter >= 'a' && letter <= 'z') {
        beginning = 'a';
        end = 'z';
    } else if (letter >= 'A' && letter <= 'Z') {
        beginning = 'A';
        end = 'Z';
    } else return letter; // the char is not a letter
    
    alphabetical_index = letter - beginning;
    for (i = 0; i < increment; ++i) {
        if (alphabetical_index >= (end - beginning))
            alphabetical_index = 0;
        else
            ++alphabetical_index;
    }      
    return (alphabetical_index + beginning);
} 
