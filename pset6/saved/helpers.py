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
    print(a)
    print(b)