import cs50

# get integer from user and check for value between 0 and 23
while True:
    rows = cs50.get_int("Please enter a number of blocks between 1 and 23: ")
    if rows >= 0 and rows <= 23:
        break
# create half pyramid based in number of rows input by user
for i in range(1, (rows + 1)):
    print(" " * (rows - i) + "#" * (i + 1))