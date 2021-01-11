import time
from copy import deepcopy


def seidel_old(a, x, b):
    n = len(a)
    # for loop for 128 times as to calculate x, y , z
    for r in range(0, n):
        # temp variable d to store b[j] 
        d = b[r]

        # to calculate respective xi, yi, zi 
        for i in range(0, n):
            if (r != i):
                d -= a[r][i] * x[i]
                # updating the value of our solution
        x[r] = d / a[r][r]
        # returning our updated solution
    return x


def seidel(a, x, b):
    length = len(a)
    for row in range(128):
        d = b[row]
        if row - 4 >= 0:
            d -= a[row][row - 4] * x[row - 4]
        if row - 1 >= 0:
            d -= a[row][row - 1] * x[row - 1]
        if row + 1 < length:
            d -= a[row][row + 1] * x[row + 1]
        if row + 4 < length:
            d -= a[row][row + 4] * x[row + 4]
        x[row] = d / a[row][row]
    return x


n = 128
b = [1] * 128
x = [0] * 128
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if (i == j):
            a[i][j] = 4
        elif (j == i + 1) or (j == i - 1) or (j == i + 4) or (j == i - 4):
            a[i][j] = 1

# for i in range (n):
#    print(a[i])


aa = deepcopy(a)
xx = deepcopy(x)
bb = deepcopy(b)

"""
start = time.time()
#loop run for m times depending on m the error value
for i in range(0, 10):
    x = seidel_old(a, x, b)

end = time.time()
print("Zajelo to ", (end - start), " sekundy")
print("x: ", x)
print("xx: " ,xx)

start = time.time()
#loop run for m times depending on m the error value
for i in range(0, 10):
    xx = seidel(aa, xx, bb)

end = time.time()
print("Zajelo to ", (end - start), " sekundy")
print(xx)
"""

for i in range(20):
    x = seidel_old(a, x, b)
    xx = seidel(a, xx, b)
    print(i)
    print(f'{x =}')
    print(f'{xx=}')
