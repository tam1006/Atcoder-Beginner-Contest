import numpy as np

H, W = map(int, input().split())
a = np.array([list(input()) for _ in range(H)])

A = np.full((a.shape[0]+2, a.shape[1]+2), '#')
A[1:-1, 1:-1] = a

for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        print(A[i, j], end='')
    print()