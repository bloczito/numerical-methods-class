import math
import numpy
import copy


def calcNorm(prev_x, x):
    result = 0

    for i in range(len(x)):
        tmp = x[i] - prev_x[i]
        result += tmp * tmp

    result = math.sqrt(result)
    return result


def scalar(a, b):
    tmp = 0
    for i in range(len(b)):
        tmp += a[i] * b[i]
    return tmp


def ConjugateGradients(A, x, b):
    r = copy.deepcopy(b)
    p = copy.deepcopy(r)
    prev_x = copy.deepcopy(x)
    Apk = [0] * len(x)

    prev_r = copy.deepcopy(r)

    for j in range(len(x)):
        Apk[j] = numpy.dot(A[j], p)

    # alfa = numpy.dot(r, r) / numpy.dot(p, Apk)
    alfa = scalar(r, r) / scalar(p, Apk)

    for j in range(len(x)):
        prev_x[j] = x[j]
        x[j] = x[j] + alfa * p[j]

    for j in range(len(x)):
        r[j] = r[j] - alfa * Apk[j]

    # beta = numpy.dot(r, r) / numpy.dot(prev_r, prev_r)
    beta = scalar(r, r) / scalar(prev_r, prev_r)

    for j in range(len(x)):
        p[j] = r[j] + beta * p[j]

    norm = calcNorm(prev_x, x)
    return norm


def fill(A):
    for i in range(N):
        for j in range(N):
            if i == j:
                A[i][j] = 4
            elif (j == i + 1) or (j == i - 1) or (j == i + 4) or (j == i - 4):
                A[i][j] = 1


N = 128
A = [[0] * N for i in range(N)]
b = [1] * N
x = [1] * N

fill(A)

for i in range(20):
    ConjugateGradients(A, x, b)
    # print(i+1)
    # print(f'{x = }')
print(x)
