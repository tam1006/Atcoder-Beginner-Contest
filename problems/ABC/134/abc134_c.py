import numpy as np

N = int(input())
A = np.array([int(input()) for _ in range(N)])

max_index = np.argsort(A)
for i in range(N):
    if i == max_index[-1]:
        print(A[max_index[-2]])
    else:
        print(A[max_index[-1]])
