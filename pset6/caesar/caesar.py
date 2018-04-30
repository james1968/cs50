import cs50
import sys

k = sys.argv[1] if len(sys.argv) == 2 else sys.exit(1)

# get the plaintext work from the user and store as a variable
encword = ""
print("plaintext: ")
plaintext = cs50.get_string()
strl = len(plaintext)
# create array for ciphered letters to be put into
cipher = []


for c in plaintext:
    if c.isalpha():
        # process lowercase letter to the encoded letter
        if c.islower():
            cipher.append(chr(((ord(c) - 97 + int(k)) % 26) + 97))

        # process upper case letters
        elif c.isupper():
            cipher.append(chr(((ord(c) - 65 + int(k)) % 26) + 65))

    # if non alpha leave unchanged
    else:
        cipher.append(c)

# convert list to string
print(f"ciphertext: {''.join(cipher)}")