import cs50
import sys

# check for number of arguments
if len(sys.argv) != 2:
    sys.exit(1)
else:
    k = sys.argv[1]

# check the codeword is characters only
strl = len(k)
for c in k:
    while c.isalpha() == False:
        print("Please enter keyword as all one word with letters only.")
        sys.exit(1)

# prompt user to enter plaintext and store as variable and get length
print("plaintext: ")
plaintext = cs50.get_string()
plaintext_len = len(plaintext)

# create an array 'm' with with the key numbers
code = sys.argv[1]
m = []
p = 0
for j in range(plaintext_len):
    p = j % strl
    if code[p].isalpha() and code[p].isupper():
        m.append(ord(code[p]) - 65)
    elif code[p].isalpha() and code[p].islower():
        m.append(ord(code[p]) - 97)

# create cipher text from plan text to increment the letters in plaintext
cipher = []
t = 0
for l in plaintext:
    # leave no alpha untouched
    if l.isalpha() == False:
        cipher.append(l)

    # process lower case letters and encode them
    elif l.islower():
        cipher.append((chr((((ord(l) - 97) + int(m[t])) % 26) + 97)))
        # only increment t if used
        t += 1

        # process upper case letters and encode them
    elif l.isupper():
        cipher.append((chr((((ord(l) - 65) + int(m[t])) % 26) + 65)))
        # only increment t if used
        t += 1

print(f"ciphertext: {''.join(cipher)}")
