import numpy as np

def r(x, y, z):
    g = np.zeros(z + 1)
    bound = min(x + 2, z + 1)

    g[0] = 1
    for i in range(1, bound):
        g[i] = 1 - y

    coef = (1 - y) * (y ** (x + 1))

    for i in range(bound, z + 1):
        g[i] = g[i - 1] - coef * g[i - x - 2]

    h = g[z]
    for i in range(0, x):
        h += g[z - i - 1] * (y ** (i + 1))
    return h

y = 0.78
z = 300
e = 0
pre = 0

for x in range(1, z + 1):
    p = r(x, y, z)
    e = e + (p - pre) * x
    pre = p 

print(e)
