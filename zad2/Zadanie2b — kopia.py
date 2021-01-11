import math
import time
from copy import deepcopy

import numpy

def incomplete_cholesky(a,h):
    #niekompletny rozkład Cholesky'ego
    n = len(a)
    for k in range (0,n):
        h[k][k] = a[k][k]
        for j in range (0,k-1):
            h[k][k] = h[k][k] - (h[k][j]*h[k][j])
        h[k][k] = math.sqrt(h[k][k])
        for l in range (k+1,n):
            h[l][k] = a[l][k]
            if(a[l][k]!=0):
                for j in range (0,k-1):
                    h[l][k] = h[l][k] - h[l][j]*h[k][j]
                h[l][k] = h[l][k]/h[k][k]

def new_incomplete_cholesky(a,h):
    #niekompletny rozkład Cholesky'ego
    n = len(a)
    for k in range (0,n):
        h[k][k] = a[k][k]
        # pierwsza petla for
        if k - 4 >= 0:
            h[k][k] = h[k][k] - (a[k][k-4] * a[k][k-4])
        if k - 1 >= 0:
            h[k][k] = h[k][k] - (a[k][k-1] * a[k][k-1])

        h[k][k] = math.sqrt(h[k][k])
        # print(type(h[k][k]))
        if k+1 < len(h):
            h[k+1][k] = a[k+1][k]
            if k-4 >=0:
                h[k+1][k] = h[k+1][k] - h[k+1][k-4]*h[k][k-4]
            if k-1 >=0:
                h[k+1][k] = h[k+1][k] - h[k+1][k-1]*h[k][k-1]
            h[k+1][k] = h[k+1][k] / h[k][k]

        if k+4 < len(h):
            h[k+4][k] = a[k+4][k]
            if k-4 >=0:
                h[k+4][k] = h[k+4][k] - h[k+4][k-4]*h[k][k-4]
            if k-1 >=0:
                h[k+4][k] = h[k+4][k] - h[k+4][k-1]*h[k][k-1]
            h[k+4][k] = h[k+4][k] / h[k][k]

def matrix_solution(h, r):
    n = len(r)
    z = [0] * n
    y = [0] * n
    y[0] =r[0]/h[0][0]

    # oblicanie pomocnego y
    for i in range(1, n):
        sum = h[i][i-1] * y[i-1]
        y[i] = (r[i]-sum) / h[i][i]

    # obliczanie z
    z[n-1] = y[n-1] / h[n-1][n-1]

    for i in range(n-2, -1, -1):
        sum = h[i+1][i] * z[i+1]
        z[i] = (y[i] - sum) / h[i][i]
    return z

def vec_length(r):
    tmp = 0
    for i in range(len(r)):
        tmp += pow(r[i], 2)
    tmp = math.sqrt(tmp)
    return tmp

def alfaK(r, z, p, A):
    numerator = 0
    denominator = 0
    n = len(r)
    y = [0] * n
    for i in range(n):
        numerator += r[i] * z[i]
    for i in range(n):
        for j in range(n):
            y[i] = p[i] * A[j][i]
    for i in range(n):
        denominator += y[i] * p[i]
    return numerator/denominator

def betaK(rk1, zk1, rk, zk):
    numerator = 0
    denominator = 0
    for i in range(len(rk1)):
        numerator += rk1[i] * zk1[i]
    for i in range(len(rk)):
        denominator += rk[i] * zk[i]
    return numerator/denominator

def new_vector_rk1(r, alfa, A, p):
    vector = [0] * len(r)
    for i in range(len(r)):
        for j in range(len(r)):
            vector[i] += A[i][j] * p[j]
    for i in range(len(r)):
        vector[i] = r[i] - alfa*vector[i]
    return vector

def new_vector_pk1(z, beta, p):
    vector = [0] * len(p)
    for i in range(len(p)):
        vector[i] = z[i] + beta*p[i]
    return vector

def new_vector_xk1(x, alfa, p):
    vector = [0] * len(x)
    for i in range(len(p)):
        vector[i] = x[i] + alfa*p[i]
    return vector

def vecNorm(rk, rk1):
    result = 0
    for i in range(len(rk1)):
        tmp = rk1[i] - rk[i]
        result += tmp*tmp
    result = math.sqrt(result)
    return result


N = 128
A = [[0] * N for i in range(N)]
H = [[0] * N for i in range(N)]
b = [1] * N
xk = [0] * N     # x(k)
xk1 = [0] * N    # x(k+1)
zk = [0] * N     # z(k)
zk1 = [0] * N    # z(k+1)
pk = [0] * N     # p(k)
pk1 = [0] * N    # p(k+1)
epsilon = 0.5

for i in range(N):
    for j in range(N):
        if i == j:
            A[i][j] = 4
        elif (j == i + 1) or (j == i - 1) or (j == i + 4) or (j == i - 4):
            A[i][j] = 1

incomplete_cholesky(A,H)

rk = b # zakładamy początkowe przybliżenie x1 = 0, uzywamy rk, zk jako r1, z1
zk = matrix_solution(H, rk)
pk = zk

# while vec_length(rk) > epsilon:
for i in range(100):
    alfa = alfaK(rk, zk, pk, A)
    rk1 = new_vector_rk1(rk, alfa, A, pk)
    zk1 = matrix_solution(H, rk1)
    beta = betaK(rk1, zk1, rk, zk)
    pk1 = new_vector_pk1(zk1, beta, pk)
    xk1 = new_vector_xk1(xk, alfa, pk)
    tmp = vecNorm(rk, rk1)
    print(tmp)
    rk = rk1
    zk = zk1
    pk = pk1
    xk = xk1
#
# for i in range(len(xk)):
#     xk[i] /= 100

# print("rk")
# print(rk)
# print("pk")
# print(pk)
# print("zk")
# print(zk)
print("xk")
print(xk)



