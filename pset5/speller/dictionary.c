// Implements a dictionary's functionality

#include <stdbool.h>
#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

#include "dictionary.h"

// define hash table from walkthrough

typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

node *hashtable[HASH_SIZE];

// hash function from https://cs50.stackexchange.com/questions/26639/16-letter-words-show-up-as-misspelled-from-pset5
int hash_it(char* needs_hashing)
{
    unsigned int hash = 0;
    for (int i=0, n=strlen(needs_hashing); i<n; i++)
        hash = (hash << 2) ^ needs_hashing[i];
    return hash % HASH_SIZE;
}

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    // creates an array to store lowercase version of the word to be spell checked
    char lower_word[LENGTH + 1];
    int word_len = strlen(word);
    for(int i = 0; i < word_len; i++)
    {
        lower_word[i] = tolower(word[i]);
        lower_word[word_len] = '\0';
    }
    // use hash function to find index for lowercase word
    int index = hash_it(lower_word);

    // return null if word not in dictionary hashtable
    if (hashtable[index] == NULL)
    {
        return false;
    }

    // create cursor to compare to word
    node* cursor = hashtable[index];

    // while cursor is not null compare to the word and return true if it matches
    while (cursor != NULL)
    {
        if (strcmp(lower_word, cursor->word) == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }
    // if you don't find the word, return false
return false;
}

// variable to track dictionary size
int dict_size = 0;

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // open dictionary
    FILE* dict = fopen(dictionary, "r");
    if (dict == NULL)
    {
        printf("Could not open dictionary.\n");
        return false;
    }

    // create an array for word to go in
    char word[LENGTH + 1];

    while (fscanf(dict, "%s", word) != EOF)
    {
        // counter for dictionary size
        dict_size++;

        // malloc a node* for each new word from walkthrough
        node* new_node = malloc(sizeof(node));
        if (new_node == NULL)
        {
            printf("Could not malloc a new node.\n");
            unload();
            return false;
        }

        // copy the node into word from walkthrough
        strcpy(new_node->word, word);

        // find the index of word in the hashtable
        int index = hash_it(word);

        // check if hashtable is empty and append new_node
        if (hashtable[index] == NULL)
        {
            hashtable[index] = new_node;
            new_node->next = NULL;
        }

        // else append new_node to hashtable
        else
        {
            new_node->next = hashtable[index];
            hashtable[index] = new_node;
        }
    }
        fclose(dict);
        return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    if (dict_size > 0)
    {
        return dict_size;
    }
    else
    return 0;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    for (int i = 0; i < HASH_SIZE; i++)
    {
        node* cursor = hashtable[i];
        while (cursor != NULL)
        {
            // kepp connection to linked list from walktrhough
            node* temp = cursor;
            cursor = cursor->next;
            free(temp);
        }
    }
    return true;
}