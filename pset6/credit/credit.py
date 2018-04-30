import cs50
import sys

cardnumber = 0
# ask for credit card details and check for a positive number
while True:
    print("Please enter a credit card number: ")
    cardnumber = cs50.get_int()
    if (cardnumber > 0):
        break

# check the number of digits
if len(str(cardnumber)) != 13 and len(str(cardnumber)) != 15 and len(str(cardnumber)) != 16:
    print("INVALID")

# create an integer array for storing card numbers
number_by_two = []
number = list(map(int, list(str(cardnumber))))
reverse_number = number[::-1]

# mulitply every second digit by two
for i in range(0, len(number)):
    if i % 2 != 0:
        number_by_two.append(reverse_number[i] * 2)
    else:
        number_by_two.append(reverse_number[i])

# get the sum of the card digits with every second number multiplied by 2
card_sum = (sum([x // 10 + x % 10 for x in number_by_two]))

if len(str(cardnumber)) == 13:
    if number[0] == 4 and card_sum % 10 == 0:
        print("VISA")
    else:
        print("INVALID")

# logic to check for Amex card based on length
if len(str(cardnumber)) == 15:
    if number[0] == 3 and card_sum % 10 == 0 and ((number[1] == 4) or (number[1] == 7)):
        print("AMEX")
    else:
        print("INVALID")

# logic for Mastercard with 16 digits.  Checks length and first digit
if len(str(cardnumber)) == 16 and number[0] == 5:
    if card_sum % 10 == 0 and ((number[1] == 1) or (number[1] == 2) or (number[1] == 3) or (number[1] == 4) or (number[1] == 5)):
        print("MASTERCARD")
    else:
        print("INVALID")

# logic for Visa with 16 digits. Checks length and first digit.
if len(str(cardnumber)) == 16 and number[0] == 4:
    if card_sum % 10 == 0:
        print("VISA")
    else:
        print("INVALID")