import numpy as np

N, X = map(int, input().split())
G = []
for i in range(N):
    G.append(list(map(int, input().split())))

dp = [[False]*(X+1) for _ in range(N+1)]
dp[0][0] = True

for i in range(N):
    for j in range(X+1):
        if dp[i][j]:
            if j+G[i][0] <= X:
                dp[i+1][j+G[i][0]] = True
            if j+G[i][1] <= X:
                dp[i+1][j+G[i][1]] = True

if dp[N][X]:
    print("Yes")
else:
    print("No")