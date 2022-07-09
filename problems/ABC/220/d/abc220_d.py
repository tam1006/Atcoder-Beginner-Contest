N = int(input())
A = list(map(int, input().split()))
mod = 998244353

from collections import deque
A = deque(A)

dp = [[0]*10 for _ in range(N)]
x = A.popleft()
dp[0][x] = 1

for i in range(N-1):
    y = A.popleft()
    for x in range(10):
        dp[i+1][(x+y)%10] = (dp[i+1][(x+y)%10]+dp[i][x])%mod
        dp[i+1][(x*y)%10] = (dp[i+1][(x*y)%10]+dp[i][x])%mod

for i in range(10):
    print(dp[N-1][i])