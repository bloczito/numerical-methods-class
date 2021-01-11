import numpy as np
import copy
import math
import time
import matplotlib.pyplot as plt


def fill(A, x, b):
    for i in range(N):
        x[i] = 0
        b[i] = 1
        for j in range(N):
            if i == j:
                A[i][j] = 4
            elif (j == i + 1) or (j == i - 1) or (j == i + 4) or (j == i - 4):
                A[i][j] = 1


def calcNorm(x, prev_x):
    result = 0
    for i in range(len(x)):
        tmp = x[i] - prev_x[i]
        result += pow(tmp, 2)
    result = math.sqrt(result)
    return result


def seidel(A, x, b, iters, gaussNorms):
    length = len(A)
    for i in range(iters):
        prev_x = copy.deepcopy(x)
        for row in range(length):
            d = b[row]
            if row - 4 >= 0:
                d -= A[row][row - 4] * x[row - 4]
            if row - 1 >= 0:
                d -= A[row][row - 1] * x[row - 1]
            if row + 1 < length:
                d -= A[row][row + 1] * x[row + 1]
            if row + 4 < length:
                d -= A[row][row + 4] * x[row + 4]
            x[row] = d / A[row][row]
        gaussNorms.append(calcNorm(x, prev_x))


def calcAPK(A, p):
    length = len(A)
    vec = [0] * len(p)
    for i in range(len(p)):
        tmp = 0
        if i - 4 >= 0:
            tmp += A[i][i - 4] * p[i - 4]
        if i - 1 >= 0:
            tmp += A[i][i - 1] * p[i - 1]
        if i + 1 < length:
            tmp += A[i][i + 1] * p[i + 1]
        if i + 4 < length:
            tmp += A[i][i + 4] * p[i + 4]
        tmp += A[i][i] * p[i]
        vec[i] = tmp
    return vec


def gradients(A, x, b, iters, gradientNorms):
    r = copy.deepcopy(b)
    p = copy.deepcopy(r)

    for i in range(iters):
        prev_r = copy.deepcopy(r)
        Apk = calcAPK(A, p)
        alfa = np.dot(r, r) / np.dot(p, Apk)

        for j in range(len(r)):
            r[j] = prev_r[j] - alfa * Apk[j]

        beta = np.dot(r, r) / np.dot(prev_r, prev_r)
        prev_p = copy.deepcopy(p)

        for j in range(len(p)):
            p[j] = r[j] + beta * prev_p[j]

        prev_x = copy.deepcopy(x)

        for j in range(len(x)):
            x[j] = prev_x[j] + alfa * prev_p[j]

        gradientsNorms.append(calcNorm(x, prev_x))


iters = 50
N = 128
A = [[0] * N for i in range(N)]
b = [1] * N
x = [0] * N
gradientsNorms = []
gaussNorms = []

# Wypelnienie poczatkowymi wartosciami
fill(A, x, b)

# Metoda Gaussa-Seidela
start = time.time()
seidel(A, x, b, iters, gaussNorms)
end = time.time()
print("Metoda Gaussa-Seidela")
print("Zajelo to ", (end - start), " sekundy")
print("Pierwsze 5 wyrazów:\nx: ", end = ' ')
for i in range(5):
    print(x[i], end = ' ')
print("\n")

# Ponowne wypelnianie poczatkowyni wartosciami
fill(A, x, b)

# Metoda Gradientów sprzężonych
start = time.time()
gradients(A, x, b, iters, gradientsNorms)
end = time.time()
print("Metoda Gradientów sprzężonych")
print("Zajelo to ", (end - start), " sekundy")
print("Pierwsze 5 wyrazów:\nx: ", end = ' ')
for i in range(5):
    print(x[i], end = ' ')

print("\n")

# Rysowanie wykresu
xRange = [0] * iters
for j in range(iters):
    xRange[j] = j+1

lower = pow(10, -12)
plt.ylim(lower, 5)
plt.yscale("log")
plt.title('Wykres zmian norm $|| x_k - x_{k-1} ||$')
plt.xlabel("Liczba iteracji")
plt.ylabel("Norma")
plt.plot(xRange, gaussNorms, 'r', xRange, gradientsNorms, 'b')
plt.legend(('Metoda Gaussa-Seidela', 'Metoda gradientów sprzężonych'))
plt.savefig('asd.png')
plt.show()
