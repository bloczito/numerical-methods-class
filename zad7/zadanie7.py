import copy
import numpy as np
import matplotlib.pyplot as plt

def Lagrange(x, index, points):
    sum = 1
    for i in range(len(points)):
        if i == index:
            continue
        sum *= (x-points[i])
        sum /= (points[index]-points[i])
    return sum

def p(x, a):
    sum = 0
    for i in range(8):
        sum += a[i]*pow(x, i)
    return sum

points = [0.062500, 0.187500, 0.312500, 0.437500, 0.562500, 0.687500, 0.812500, 0.937500]
values = [0.687959, 0.073443, -0.517558, -1.077264, -1.600455, -2.080815, -2.507266, -2.860307]
startValues = copy.deepcopy(values)
a = [0, 0, 0, 0, 0, 0, 0, 0]

for i in range(8):
    for j in range(8):
        a[i] +=Lagrange(0, j, points)*values[j]
    for j in range(8):
        values[j] = (values[j] - a[i])/points[j]

print(a)
print(values)

plt.scatter(points, startValues, c='k')


xx = np.linspace(-1, 1, endpoint=True)
plt.plot(xx, p(xx, a) , linestyle=':')
plt.show()
plt.savefig('interpolacja.png')