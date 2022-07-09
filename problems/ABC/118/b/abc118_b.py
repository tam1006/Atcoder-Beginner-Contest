import numpy as np
N, M = map(int, input().split())
K = []
A = []
for _ in range(N):
    i = list(map(int, input().split()))
    K.append(i[0])
    A.append(i[1:])

food = [True]*M

for i in range(N):
    A[i] = np.array(A[i]) - 1
    for j in range(M):
        if not j in A[i]:
            food[j] = False

print(sum(food))