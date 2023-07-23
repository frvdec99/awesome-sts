import numpy as np

def mc(n, p):
    r = np.random.binomial(1, p, size=n)
    rs = np.sum(r)
    f = 0
    mx = 0
    for i in range(0, n):
        if r[i]:
            f = f + 1
            mx = max(mx, f)
        else:
            f = 0
    return int(mx)

n = 300
p = 0.78
e = 0

T = 100000
for i in range(T):
    e = e + mc(n, p)

print(e / T)



