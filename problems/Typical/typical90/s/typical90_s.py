import sys
sys.setrecursionlimit(10**6)

from functools import lru_cache

N = int(input())
A = list(map(int, input().split()))

INF = pow(10, 12)
dp = [[INF for _ in range(2*N)] for _ in range(2*N)]


@lru_cache(maxsize=None)
def dfs(i, j) -> int:
    if dp[i][j] != INF:
        return dp[i][j]

    if j <= i:
        dp[i][j] = INF
        return INF
    elif j - i == 1:
        dp[i][j] = abs(A[i] - A[j])
        return dp[i][j]
    else:
        # res = dfs(i+1, j-1) + abs(A[i] - A[j])
        res = min(INF, dfs(i+1, j-1) + abs(A[i] - A[j]))
        for k in range(i+1, j-1, 2):
            res = min(res, dfs(i, k) + dfs(k+1, j))
        # dp[i][j] = res
        dp[i][j] = min(dp[i][j], res)
        return dp[i][j]

print(dfs(0, 2*N-1))
