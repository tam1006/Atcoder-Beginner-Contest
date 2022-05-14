import numpy as np

N, D = map(int, input().split())
X = [np.array(list(map(int, input().split()))) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(i+1, N):
        if i == j:
            continue

        d = np.linalg.norm(X[i] - X[j])
        if d.is_integer():
            ans += 1

print(ans)