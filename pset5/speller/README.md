# Questions

## What is pneumonoultramicroscopicsilicovolcanoconiosis?

It is the longest word in the English language published in a dictionary, the Oxford English Dictionary,
which defines it as "an artificial long word said to mean a lung disease caused by inhaling very fine ash and sand dust."

## According to its man page, what does `getrusage` do?

returns resource usage measures for who, which can be one of the following:

RUSAGE_SELF - Return resource usage statistics for the calling process, which is the sum of resources used by all threads in the process.
RUSAGE_CHILDREN - Return resource usage statistics for all children of the calling process that have terminated and been waited for. These statistics will include the resources used by grandchildren, and further removed descendants, if all of the intervening descendants waited on their terminated children.
RUSAGE_THREAD (since Linux 2.6.26) - Return resource usage statistics for the calling thread.

## Per that same man page, how many members are in a variable of type `struct rusage`?

16

## Why do you think we pass `before` and `after` by reference (instead of by value) to `calculate`, even though we're not changing their contents?

Beacause its quicker and users less memory than passing the values.

## Explain as precisely as possible, in a paragraph or more, how `main` goes about reading words from a file. In other words, convince us that you indeed understand how that function's `for` loop works.
The for loop sets an int variable to the character from the file using fgetc(file).  It then loops until the end of the file and going through each character individually.
It then checks the word characters are alphabetical or an aposrophe and if so adds the character into the word array.  Once done there is a check for the word being too long i.e. more than 45 characters.
Similarly there is a check for digits and the string is passed over if there are digits in it.  The next else if clause confirms a word has been found and then does
the spell check.

## Why do you think we used `fgetc` to read each word's characters one at a time rather than use `fscanf` with a format string like `"%s"` to read whole words at a time? Put another way, what problems might arise by relying on `fscanf` alone?

If we use fscanf with a format string like "%s" it will read all subsequent characters until a whitespace is found, in which case it might include punctuation which we don't want.

## Why do you think we declared the parameters for `check` and `load` as `const` (which means "constant")?

The value being pointed to i.e. *word or *dictionary can't be changed, which is needed for this programme as we don't want the work or dictionary to be changed.
