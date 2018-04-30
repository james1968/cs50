import cs50

# request an amount of change from the user
while True:
    change = cs50.get_float("Please enter the amount of your change: ")
    if change > 0:
        break
# change to cents from dollars and create count variable
cents = (change * 1000) / 10
count = 0

# calculate the number of quaters, nickels, dimes and pennies
while (cents >= 25):
    count += 1
    cents -= 25

while (cents >= 10):
    count += 1
    cents -= 10

while (cents >= 5):
    count += 1
    cents -= 5

while (cents >= 1):
    count += 1
    cents -= 1

# print out the answer
print(count)
