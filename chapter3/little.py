import random
import numpy as np

eps = 1e-5

n = 10
m = 8
u = m / n
a = 0.05

C = np.zeros((n+1, n+1))
C[0, 0] = 1
C[1, 0] = C[1, 1] = 1
for i in range(2, n + 1):
    C[i, 0] = 1
    for j in range(1, i + 1):
        C[i, j] = C[i - 1, j - 1] + C[i - 1, j]

def lower(P, N, M, C):
    s = 0
    for i in range(0, M + 1):
        s = s + C[N, i] * (P ** i) * ((1 - P) ** (N - i))
    return s

def upper(P, N, M, C):
    s = 0
    for i in range(M + 1, N + 1):
        s = s + C[N, i] * (P ** i) * ((1 - P) ** (N - i))
    return s

l = 0
r = 1
while (r - l) > eps:
    mid = (l + r) * 0.5
    s = lower(mid, n, m, C)
    if s < a / 2:
        r = mid
    else:
        l = mid
pu = (l + r) * 0.5

l = 0
r = 1
while (r - l) > eps:
    mid = (l + r) * 0.5
    s = upper(mid, n, m, C)
    if s < a / 2:
        l = mid
    else:
        r = mid

pl = (l + r) * 0.5
p = lower(pu, n, m, C) + upper(pl, n, m, C)
print(f'[{pl}, {pu}], {1 - p}')