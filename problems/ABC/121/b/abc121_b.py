import numpy as np

N, M, C = map(int, input().split())
B = np.array(list(map(int, input().split())))
A = []
for i in range(N):
    A.append(np.array(list(map(int, input().split()))))

ans = 0
for i in range(N):
    if np.dot(A[i], B) + C > 0:
        ans += 1

print(ans)