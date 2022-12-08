#!/usr/bin/env python3
# from typing import *

MOD = 998244353


# def solve(N: int, M: int, K: int) -> int:
def solve(N, M, K):
    Minv = pow(M, MOD - 2, MOD)

    dp = [[0 for _ in range(N+1)] for _ in range(K+1)]
    dp[0][0] = 1

    for i in range(K):
        for j in range(N+1):
            if j == N:
                dp[i+1][j] += dp[i][j]
                dp[i+1][j] %= MOD
                continue

            for k in range(1, M+1):
                if j+k >= N+1:
                    n = 2*N - (j+k)
                else:
                    n = j+k

                dp[i+1][n] += dp[i][j] * Minv % MOD
                dp[i+1][n] %= MOD

    return dp[K][N]

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, M, K = map(int, input().split())
    a = solve(N, M, K)
    print(a)


if __name__ == '__main__':
    main()
