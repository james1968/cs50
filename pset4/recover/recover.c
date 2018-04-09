#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(int argc, char *argv[])
{
    // ensure proper usage
    if (argc != 2)
    {
        fprintf(stderr, "Usage: file to recover images from\n");
        return 1;
    }

    // create pointer for file with images on
    char *infile = argv[1];

    // open the input file
    FILE *inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 2;
    }

    typedef uint8_t  BYTE;
    BYTE buffer[512];
    int counter = 0;
    char outptr[8];
    FILE *img;

    while (fread(&buffer, 512, 1, inptr) == 1)
    {
        if ((buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff) && (buffer[3] == 0xe0 || buffer[3] == 0xe1))
        {
            //close an open jpeg file
            if (counter > 0)
            {
                fclose(img);
            }
            //counter for finding a jpeg
            counter++;

            //create output file
            sprintf(outptr, "%03d.jpg", counter - 1);

            //open output file and write jpeg header to file
            img = fopen(outptr, "w");
            fwrite(&buffer, 512, 1, img);
        }
        else
        {
            // if file is a jpeg write bytes to file
            if (counter > 0)
            {
                fwrite(&buffer, 512, 1, img);
            }
        }
    }
    // close input file
    fclose(inptr);
}