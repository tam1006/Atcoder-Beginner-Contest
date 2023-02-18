N = int(input())
D, C, S = [], [], [] 

for _ in range(N):
    d, c, s = map(int, input().split())
    D.append(d)
    C.append(c)
    S.append(s)

D_MAX = max(D)

D, C, S = zip(*sorted(zip(D, C, S), key=lambda x: x[0]))


# dp[i][j]: i番目まで見た時に、選びうる仕事の組み合わせに対して、最短で終えられるように選んだ時の、j日目の報酬の最大値
# あくまでも最短で選ぶから、dp[i][j]で仕事を選んだ結果は、dp[i][j+1:]には影響しない。こうすることで、仕事をしている最中に重複して
# 他の仕事を選ぶということを防ぐ。
dp = [[0] * (D_MAX + 2) for _ in range(N + 1)]

for i in range(N):
    for j in range(1, D_MAX+1):
        if j + C[i] - 1 <= D[i]:
            dp[i+1][j+C[i]] = max(dp[i+1][j+C[i]], dp[i][j] + S[i])
        dp[i+1][j] = max(dp[i+1][j], dp[i][j])

print(max(dp[N]))
