import numpy as np

N, M = map(int, input().split())
LR = []
for i in range(M):
    LR.append(list(map(int, input().split())))

LR = np.array(LR)

cross = [max(LR[:, 0]), min(LR[:, 1])]
if cross[0] > cross[1]:
    print(0)
else:
    print(cross[1] - cross[0] +1)