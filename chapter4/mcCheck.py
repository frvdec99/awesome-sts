import numpy as np

n = 300
p = 0.78

def mc(n, p):
    r = np.random.binomial(1, p, size=n)
    f = np.zeros([n + 1, 2])
    f[0, 0] = 0
    f[0, 1] = 0
    mx = 0
    for i in range(1, n + 1):
        if r[i - 1]:
            f[i, 0] = f[i-1, 0] + 1
            f[i, 1] = f[i-1, 1] + 1
        else:
            f[i, 0] = 0
            f[i, 1] = f[i-1, 0] + 1
        mx = max(f[i, 0], mx)
        mx = max(f[i, 1], mx)
    return int(mx)

e = 0
T = 10000
for i in range(T):
    e = e + mc(n, p)

print(e / T)



