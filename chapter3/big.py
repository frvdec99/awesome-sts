import math

n = 300
m = 234
a = 0.05
za = 1.96

u = m / n 
lower = u - za * math.sqrt(u * (1 - u) / n)
upper = u + za * math.sqrt(u * (1 - u) / n)
print(f'[{lower}, {upper}]')
