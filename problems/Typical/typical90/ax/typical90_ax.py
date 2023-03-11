N, L = map(int, input().split())

dp = [0] * (N+1)
dp[0] = 1

MOD = 10**9 + 7

for i in range(N):
    dp[i+1] += dp[i]
    dp[i+1] %= MOD
    if i+L <= N:
        dp[i+L] += dp[i]
        dp[i+L] %= MOD

print(dp[N])
