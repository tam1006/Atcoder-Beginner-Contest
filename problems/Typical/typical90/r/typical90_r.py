T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())
E = []
for _ in range(Q):
    e = int(input())
    E.append(e)

import math

def coor(t):
    t %= T
    theta = t/T * 2 * math.pi
    x = 0
    y = -L/2 * math.sin(theta)
    z = L/2*(1 - math.cos(theta))

    return (x, y, z)

for e in E:
    x, y, z = coor(e)

    vec1 = (x - X, y - Y, z)
    vec2 = (x - X, y - Y, 0)

    x = math.sqrt(vec2[0]**2 + vec2[1]**2)
    y = z

    print(math.degrees(math.atan2(y, x)))


