#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    long cardnumber;
    //ask for credit card details and check for a positive number
    do
    {
        printf("Please enter a credit card number: ");
        cardnumber = get_long_long();
    }
    while (cardnumber < 0);

    // check the number of digits

    int count = 0;
    long countdigits = cardnumber;
    while (countdigits > 0)
    {
        countdigits = countdigits / 10;
        count++;
    }
    if ((count != 13) && (count != 15) && (count != 16))
    {
        printf("INVALID\n");
    }
    // create an integer array for storing card numbers
    int number[count];

    for (int i = 0; i < count; i++)
    {
        number[i] = cardnumber % 10;
        cardnumber = cardnumber / 10;
    }
    // create cardnumber in an array
    int cnumber[count];

    for (int i = 0; i < count; i++)
    {
        cnumber[i] = number[i];
    }
    // mulitply every second digit by two
    for (int i = 1; i < count; i += 2)
    {
        number[i] = number[i] * 2;
    }

    int sum = 0;
    int sumdigits;
    // logic for dealing with each card type
    if (count == 13)
    {
        // calculates the sum of each of the card numbers
        for (int i = 0; i < count; i++)
        {
            sumdigits = (number[i] % 10) + (number[i] / 10 % 10);
            sum = sum + sumdigits;
        }
        // determines if Visa card
        if (cnumber[12] == 4 && sum % 10 == 0)
        {
            printf("VISA\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    // logic to check for Amex card based on length
    if (count == 15)
    {
        for (int i = 0; i < count; i++)
        {
            sumdigits = (number[i] % 10) + (number[i] / 10 % 10);
            sum = sum + sumdigits;
        }
        if (cnumber[14] == 3 && sum % 10 == 0 && ((cnumber[13] == 4) || (cnumber[13] == 7)))
        {
            printf("AMEX\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    // logic for MAstercard with 16 digits.  Checks length and first digit.
    if (count == 16 && cnumber[15] == 5)
    {
        for (int i = 0; i < count; i++)
        {
            sumdigits = (number[i] % 10) + (number[i] / 10 % 10);
            sum = sum + sumdigits;
        }
        if (sum % 10 == 0 && ((cnumber[14] == 1) || (cnumber[14] == 2) || (cnumber[14] == 3) || (cnumber[14] == 4) || (cnumber[14] == 5)))
        {
            printf("MASTERCARD\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    // logic for Visa with 16 digits. Checks length and first digit.
    if (count == 16 && cnumber[15] == 4)
    {
        for (int i = 0; i < count; i++)
        {
            sumdigits = (number[i] % 10) + (number[i] / 10 % 10);
            sum = sum + sumdigits;
        }
        if (sum % 10 == 0)
        {
            printf("VISA\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    return 0;
}