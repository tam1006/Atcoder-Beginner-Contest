H, W, C, Q = map(int, input().split())
tnc = [list(map(int, input().split())) for _ in range(Q)]

from collections import defaultdict

color = [0] * (C+1)
see_H = defaultdict(int)
see_W = defaultdict(int)
num_H = 0
num_W = 0

for i in range(-1, -Q-1, -1):

    if tnc[i][0] == 1:
        if see_W[tnc[i][1]] == 1:
            continue
        color[tnc[i][2]] += W - num_H
        see_W[tnc[i][1]] = 1
        num_W += 1
    else:
        if see_H[tnc[i][1]] == 1:
            continue
        color[tnc[i][2]] += H - num_W
        see_H[tnc[i][1]] = 1
        num_H += 1

print(*color[1:])