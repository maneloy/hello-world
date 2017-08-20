#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_INPUT 300

char rotate(char letter, int key);

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: ./vigenere k\n");
        return 1;
    }
    
    int i, j, key, keys_len;
    int keys[MAX_INPUT];
    char *not_converted;
    char user_input[MAX_INPUT];
    char output[MAX_INPUT];
    char rotated_char;
    
    keys_len = 0;
    not_converted = 0;
    j = 0;
    
    for (i = 0; i < strlen(argv[1]); ++i) {
        if (argv[1][i] >= 'A' && argv[1][i] <= 'Z') 
            keys[i] = argv[1][i] - 'A';
        else
            keys[i] = argv[1][i] - 'a';
        ++keys_len; 
    }
    
    printf("plaintext: ");
    fgets(user_input, MAX_INPUT, stdin);
    
    for (i = 0; i <= strlen(user_input); ++i) {
        if (j >= keys_len)
            j = 0;
        key = keys[j];
        rotated_char = rotate(user_input[i], key);
        output[i] = rotated_char;
        if (rotated_char >= 'a' && rotated_char <= 'z')
            ++j;
        else if (rotated_char >= 'A' && rotated_char <= 'Z')
            ++j;
        else
            ;   // don't rotate char if char is not a letter
    }
    
    printf("ciphertext: %s", output);
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
