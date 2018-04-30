from nltk.tokenize import sent_tokenize


def lines(a, b):
    # split file into lines and store in variables
    a_lines = a.splitlines()
    b_lines = b.splitlines()
    # new list for storing the same lines
    same_lines = []
    # loop to identify new lines
    for i in a_lines:
        if i in b_lines:
            same_lines.append(i)
    return same_lines


def sentences(a, b):
    # break file up into sentences
    a_sent = sent_tokenize(a)
    b_sent = sent_tokenize(b)
    # new list for same sentences
    same_sent = []
    # loop for identifying the same sentences
    for i in a_sent:
        if i in b_sent:
            same_sent.append(i)
    return list(set(same_sent))


def substrings(a, b, n):
    # split file into individual strings
    a_strings = a.split(' ')
    a_len = len(a_strings)
    a_substrings = []
    # iterate over each string and to get the substrings
    for l in range(a_len):
        s = n
        t = 0
        for m in range((len(a_strings[l]) + 1) - n):
            a_substrings.append(a_strings[l][t:s])
            t += 1
            s += 1
    # same iteration for second file
    b_strings = b.split(' ')
    b_len = len(b_strings)
    b_substrings = []
    for l in range(b_len):
        s = n
        t = 0
        for m in range((len(b_strings[l]) + 1) - n):
            b_substrings.append(b_strings[l][t:s])
            t += 1
            s += 1
    # compare the substrings for the two files
    same_substrings = []
    for p in a_substrings:
        if p in b_substrings:
            same_substrings.append(p)

    return list(set(same_substrings))