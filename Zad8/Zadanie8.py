import matplotlib.pyplot as plt
import numpy as np


# liczy wartosc funkcji dla danego x
def valueOfFunction(x):
    temp = 5 * x * x + 1.0
    return 1.0 / temp


# zwraca element bazy wektora x(y), gdzie i to i-ty element bazy
def base(vecX, index, y):
    tmp = 1
    for i in range(len(vecX)):
        if i == index:
            continue
        else:
            tmp *= (y - vecX[i])

    return tmp


# obliczanie wspolczynnikow wielomianu lagrange'a
def coefficients(vecX, vecY, vecA):
    for i in range(len(vecA)):
        vecA[i] = vecY[i] / base(vecX, i, vecX[i])


# oblicza wartosc funkcji dla x
def calculate(vecX, vecA, y):
    result = 0
    for i in range(len(vecA)):
        result += vecA[i] * base(vecX, i, y)
    return result


def p(x, vecX, a):
    sum = 0
    for i in range(len(a)):
        tmp = 1
        for j in range(len(vecX)):
            tmp *= (x - vecX[j])
        sum = sum + a[i]*tmp

    return sum


vecX = [0] * 65
vecY = [0] * 65
vecA = [0] * 65

j = -1
for i in range(len(vecX)):
    vecX[i] = j
    vecY[i] = valueOfFunction(j)
    j += (1.0 / 32)

coefficients(vecX, vecY, vecA)

# plt.scatter(vecX, vecY)
print("Wspolczynniki:")
print(vecA)

# print(vecY)
x = np.linspace(-1, 1, endpoint=True)
plt.plot(x, calculate(vecX, vecA, x))
# plt.plot(x, valueOfFunction(x), linestyle=':')
plt.show()
