/**
 * Implements a dictionary's functionality.
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>
#include "dictionary.h"

typedef struct node             // we implement a "trie"
{                       
    struct node *children[27];
    bool is_word;    
} 
node;

node *root;

int word_count = 0;

void free_node(node* cur) 
{
    for (int i = 0; i < 27; i++) 
    {
        if (cur -> children[i] != NULL)
            free_node(cur -> children[i]);
    }

    free(cur);
}

/**
 * Returns true if word is in dictionary else false.
 */
bool check(const char *word)
{
    int index;
    int i = 0;
    node* current = root;
    while (word[i] != '\0') {          
        char character = tolower(word[i]);   
        if (word[i] == '\'')
            character = 'z' + 1;
        index = character - 'a';
        if (current -> children[index] != NULL) {
            current = current->children[index];
            i++;
        }
        else
            return false;
    }
    
    if (current->is_word == true)
        return true;
    else
        return false;
}

/**
 * Loads dictionary into memory. Returns true if successful else false.
 */
bool load(const char *dictionary)
{
    int character = 0;
    FILE *dict = fopen(dictionary, "r");
    
    if (dict == NULL) 
    {
        return false;
    }
        
    root = (node*) calloc(27, sizeof(node));
    node *current = NULL;
    
    while ((character = fgetc(dict)) != EOF) {
        current = root;
        while (character != '\n') {
            if (character == '\'')
                character = 'z' + 1;
            if (current->children[character - 'a'] == NULL) {
                current->children[character - 'a'] = (node*) calloc(27, sizeof(node));
                current = current->children[character - 'a'];                
            } else
                current = current->children[character - 'a'];
            character = fgetc(dict);
        }
        current->is_word = true;
        word_count++; 
    }
    
    fclose(dict);
    return true;
}

/**
 * Returns number of words in dictionary if loaded else 0 if not yet loaded.
 */
unsigned int size(void)
{
    int n = word_count;
    return n;
}

/**
 * Unloads dictionary from memory. Returns true if successful else false.
 */
bool unload(void)
{
    free_node(root);
    return true;
}
