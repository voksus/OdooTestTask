# ----------------------------------
#
# Created by Volodymyr Burtsev
#
# on 03.07.2018 in 16:46
#
# The project is < OdooTestTask >
#
# ----------------------------------


def calculate(inputData):
    # the calculations working in pence
    incomTax = inputData[0][0]
    targetTax = inputData[0][1]

    lst = []
    for data in inputData[1:]:
        lst.append(int(data[0] * data[1] * incomTax))

    resultTax = round(sum(lst) / 100, 2)
    taxCorrector = round((targetTax - resultTax) * 100)

    # adding possible missing coin to price of the first item
    lst[0] += taxCorrector

    # convert in money
    for i in range(len(lst)):
        lst[i] /= 100

    return lst


# incoming data
inputData = [
    [20, 1434.07],
    [397.01, 1],
    [435.0, 2],
    [435.0, 2],
    [443.33, 2],
    [443.33, 2],
    [370.0, 2],
    [630.0, 1],
    [630.0, 1],
    [630.0, 2]
]

lst = calculate(inputData)

for data in lst:
    print(data)
