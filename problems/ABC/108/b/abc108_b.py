import numpy as np
x = list(map(int, input().split()))

x1 = (x[0], x[1])
x2 = (x[2], x[3])

v = (x1[0] - x2[0], x1[1] - x2[1])
v3 = (v[1], -v[0])
x3 = (x2[0] + v3[0], x2[1] + v3[1])
x4 = (x3[0] + v[0], x3[1] + v[1])

ans = [x3[0], x3[1], x4[0], x4[1]]
print(*ans)