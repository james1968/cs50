#include <cs50.h>
#include <stdio.h>

int main(void)

{
    float change;
    int cents;
    int count = 0;

    do
    {
        change = get_float("Please enter the amount of your change: ");
    }
    //continue with loop until a positive value is entered
    while (change <= 0);

    //convert float in dollars to cents as an int
    cents = (change * 1000) / 10;

    // calculate the number of quaters, nickels, dimes and pennies
    while (cents >= 25)
    {
        count += 1;
        cents -= 25;
    }

    while (cents >= 10)
    {
        count += 1;
        cents -= 10;
    }

    while (cents >= 5)
    {
        count += 1;
        cents -= 5;
    }

    while (cents >= 1)
    {
        count += 1;
        cents -= 1;
    }

    //print out the answer
    printf("%i\n", count);

}
