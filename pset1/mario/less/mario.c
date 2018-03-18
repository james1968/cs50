#include <cs50.h>
#include <stdio.h>
#include <cs50.h>

int main(void)

{
    int rows;
    int spaces;
    int hashes;
    //get number of rows required from user
    do
    {
        rows = get_int("Please enter a number of blocks between 1 and 23: ");
    }
    //continue with loop to get number of rows if a valid number isn't entered
    while (rows < 0 || rows > 23);

    //loop for the spaces and dashes per row
    for (int i = 1; i <= rows; i++)
    {
        for (spaces = (rows - i); spaces > 0; spaces--)
        {
            printf(" ");
        }
        for (hashes = 1; hashes <= (i + 1); hashes++)
        {
            printf("#");
        }

        printf("\n");
    }
    return 0;
}