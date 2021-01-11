import numpy as np

def power_iteration(A):
    n = len(A)
    b_k = [1,1,1,1,1,1]
    b_k = np.linalg.norm(b_k)
    for i in range(n):
        b_k1 = np.linalg.dot(A, b_k)
        bk = np.linalg.norm(b_k1)

A = [[19/12, 13/12, 10/12, 10/12, 13/12, -17/12],
     [13/12, 13/12, 10/12, 10/12, -11/12, 13/12],
     [10/12, 10/12, 10/12,  -2/12, 10/12, 10/12],
     [10/12, 10/12,  -2/12, 10/12, 10/12, 10/12],
     [13/12, -11/12, 10/12, 10/12, 13/12, 13/12],
     [-17/12, 13/12, 10/12, 10/12, 13/12, 19/12]]




