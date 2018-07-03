# ----------------------------------
#
# Created by Volodymyr Burtsev
#
# on 03.07.2018 in 10:02
#
# The project is < OdooTestTask >
#
# ----------------------------------

import random


def createString():
    print("Creating the string...")

    # ---- create list with 40k of each letter
    lst = list(letters * lettersRepeats)

    # ---- shuffling letters in the list
    random.shuffle(lst)

    print("String was created")
    # ---- convert to string
    return ''.join(lst)


# letter to be used
letters = "abcdefghijklmnopqrstuvwxyz"

# variables for conditions
lettersRepeats = 40_000
seq2 = 1700
seq3 = 100

string = createString()

# ---- checking the conditions :
#           * each letter should be used only 40'000 tms     -> Done! :)
#           * each sequence in string with 2 letters
#               should be repeated not greater 2000 tms
#           * each sequence in string with 3 letters
#               should be repeated not greater 100 tms
flag = False
while True:
    print("Checking conditions...\n")
    i = 0
    # checking all possible combinations
    for a in list(letters):
        for b in list(letters):
            iteration2 = string.count(a + b)
            if iteration2 > seq2:
                flag = True
                break
            for c in list(letters):
                iteration3 = string.count(a + b + c)
                if iteration3 > seq3:
                    flag = True
                    break
        if flag:
            break

    # if conditions are not met it will start new try
    if flag:
        print("Conditions are violated. Starting another try...")
        flag = False
        string = createString()
    else:
        break

print("The string was created and tested according to the conditions successfully.")
