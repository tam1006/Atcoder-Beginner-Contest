N = int(input())
S = input()

MOD = 10**9 + 7

nums = [0]*7
T = list('atcoder')

dp = [[0]*8 for _ in range(N+1)]
dp[0][0] = 1

for i in range(N):
    for j in range(7):
        dp[i+1][j] += dp[i][j]
        dp[i+1][j] %= MOD

        if S[i] == T[j]:
            dp[i+1][j+1] += dp[i][j]
            dp[i+1][j+1] %= MOD

    dp[i+1][7] += dp[i][7]
    dp[i+1][7] %= MOD

print(dp[N][7]%MOD)
