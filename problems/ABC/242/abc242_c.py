# PyPyなら通る
N = int(input())

dp = [1]*9

for i in range(1, N):
    temp = [0]*9
    for j in range(9):
        if j == 0:
            temp[j] = (dp[j] + dp[j+1]) % 998244353
        elif j == 8:
            temp[j] = (dp[j-1] + dp[j]) % 998244353
        else:
            temp[j] = (dp[j-1] + dp[j] + dp[j+1]) % 998244353
    dp = temp

print(sum(dp) % 998244353)