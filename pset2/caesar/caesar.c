#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    //check for number of arguments and return 1 if not 2
    int k;
    if (argc == 2)
    {
        k = atoi(argv[1]);
    }
    else
    {
        return 1;
    }
    //initialise variables for plaintext word and the resulting enciphered word
    string encword;
    string plaintext;
    printf("plaintext: ");
    plaintext = get_string();
    int strl = strlen(plaintext);
    //create array for ciphered letters to be put into
    char cipher[strl];

    for (int i = 0; i < strl; i++)
    {
        if (isalpha(plaintext[i]))
        {
            //process lowercase letter to the encoded letter
            if (islower(plaintext[i]))
            {
                char plainchar = plaintext[i];
                int plainascii = (((int)plainchar - 97 + k) % 26);
                char encoded = plainascii + 97;
                cipher[i] = encoded;
            }
            // process upper case letters
            else if (isupper(plaintext[i]))
            {
                char plainchar = plaintext[i];
                int plainascii = (((int)plainchar - 65 + k) % 26);
                char encoded = plainascii + 65;
                cipher[i] = encoded;
            }
        }
        // process no alpha letters, leave unchanged
        else
        {
            char plainchar = plaintext[i];
            cipher[i] = plainchar;
        }
        // convert resulting array to string
        encword = cipher;

    }
    printf("ciphertext: %s\n", encword);
    return 0;
}
