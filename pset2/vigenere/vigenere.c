#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    //check for no argv[1] or more than two arguments and return 1
    if (argv[1] == NULL || argc > 2)
    {
        printf("Please enter keyword as all one word with letters only.\n");
        return 1;
    }
    //assign argv[1] to string and check for alpha characters only
    string k = argv[1];
    int strl = strlen(k);
    if (argc == 2)
    {
        for (int i = 0; i < strl; i++)
        {
            while (isalpha(k[i]) == false)
            {
                printf("Please enter keyword as all one word with letters only.\n");
                return 1;
            }
        }
    }

    //prompt user to enter plaintext and store as variable and get length
    string plaintext;
    printf("plaintext: ");
    plaintext = get_string();
    int plain_text_strl = strlen(plaintext);
    //create an array 'm' with with the key numbers
    string code = argv[1];
    int m[plain_text_strl];
    int p = 0;
    for (int j = 0; j < plain_text_strl; j++)
    {
        p = j % strl;
        if (isalpha(code[p]) && isupper(code[p]))
        {
            m[j] = (code[p % strl] - 'A');
        }
        else if (isalpha(code[p]) && islower(code[p]))
        {
            m[j] = (code[p % strl] - 'a');
        }
    }
    //create cipher text from plan text to increment the letters in plaintext
    char cipher[plain_text_strl + 1];
    cipher[plain_text_strl] = '\0';
    int t = 0;
    for (int l = 0; l < plain_text_strl; l++)
    {
        //leave no alpha untouched
        if (isalpha(plaintext[l]) == false)
        {
            cipher[l] = plaintext[l];
        }

        //process lower case letters and encode them
        else if (islower(plaintext[l]))
        {
            char plainchar_low = plaintext[l];
            int plainascii = (((int)plainchar_low - 'a' + m[t]) % 26);
            //only increment t if used
            t++;
            char encoded_low = plainascii + 'a';
            cipher[l] = encoded_low;
        }
        // process upper case letters and encode them
        else if (isupper(plaintext[l]))
        {
            char plainchar_up = plaintext[l];
            int plainascii = (((int)plainchar_up - 'A' + m[t]) % 26);
            //only increment t if used
            t++;
            char encoded_up = plainascii + 'A';
            cipher[l] = encoded_up;
        }
    }
    // convert array cipher to string
    char *answer = NULL;
    answer = cipher;
    printf("ciphertext: %s\n", answer);
    return 0;
}