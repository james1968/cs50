# Questions

## What's `stdint.h`?

stdint.h is a header file that provides a set of typedefs that specify exact-width integer types.

## What's the point of using `uint8_t`, `uint32_t`, `int32_t`, and `uint16_t` in a program?

The main reason is that the bit size of each is defined and equal across all of the platforms and knowing the size makes it easier to manipulate.

## How many bytes is a `BYTE`, a `DWORD`, a `LONG`, and a `WORD`, respectively?

BYTE = 8 bits = 1 byte
DWORD= 32 bits = 4 bytes
LONG = 32 bits = 4 bytes
WORD = 16 bits = 2 bytes

## What (in ASCII, decimal, or hexadecimal) must the first two bytes of any BMP file be? Leading bytes used to identify file formats (with high probability) are generally called "magic numbers."

ASCII = BM
hexadecimal = 42 4D

## What's the difference between `bfSize` and `biSize`?

bfSize = the total number of bytes in the file.
biSize = the number of bytes in the info header.

## What does it mean if `biHeight` is negative?

For uncompressed RGB bitmaps, if biHeight is positive, the bitmap is a bottom-up DIB with the origin at the lower left corner.
If biHeight is negative, the bitmap is a top-down DIB with the origin at the upper left corner.

## What field in `BITMAPINFOHEADER` specifies the BMP's color depth (i.e., bits per pixel)?

biBitCount specifies the number of bits per pixel (bpp).
For uncompressed formats, this value is the average number of bits per pixel.
For compressed formats, this value is the implied bit depth of the uncompressed image, after the image has been decoded.


## Why might `fopen` return `NULL` in lines 24 and 32 of `copy.c`?

Because it can't find the file.

## Why is the third argument to `fread` always `1` in our code?

The third argument is the number of elements and we are interested in only reading one structure e.g. BITMAPFILEHEADER structure.

## What value does line 63 of `copy.c` assign to `padding` if `bi.biWidth` is `3`?

If biWidth is 3:
int padding =  (4 - (bi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4 = 3.
This step ensures the number of bytes in every row is a multiple of 4.

## What does `fseek` do?

fseek is used to move the file position to a desired location within the file.

## What is `SEEK_CUR`?

SEEK_CUR is used with fseek to move the pointer to the current location.
