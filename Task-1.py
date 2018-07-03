# ----------------------------------
#
# Created by Volodymyr Burtsev
#
# on 03.07.2018 in 0:33
#
# The project is < OdooTestTask >
#
# ----------------------------------

global num

def checkEvenOdd(n):
    if n % 2 == 0:
        s = "Even"
    else:
        s = "Odd"
    return s


# ----------------- S T A R T ----------------------

# starting the app
number = [1, 7, -67890000, 0, 321, 456789, -10, 333, -222222222]

for num in number:
    print(checkEvenOdd(num))
