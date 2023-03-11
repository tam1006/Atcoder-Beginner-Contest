N, K = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(N)]

INF = pow(10, 20)

def dist_2(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

# dist[S]: 集合Sに含まれる点のペアの距離の最大値
dist = [0] * (1<<N)

for S in range(1<<N):
    # 集合Sに含まれる任意の２点間の距離の最大値を求める
    for i in range(N):
        if (S >> i) % 2 == 0:
            continue

        for j in range(i+1, N):
            if (S >> j) % 2 == 0:
                continue

            dist[S] = max(dist[S], dist_2(points[i], points[j]))

# dp[i][S]: i個のグループを既に作った時、既に選んだものの集合がSである時の最小コスト
dp = [[INF] * (1<<N) for _ in range(K+1)]
dp[0][0] = 0

for i in range(1, K+1):
    for S in range(1<<N):
        # UはSの部分集合
        # dp[i][S] = min(max(dp[i-1][S-U], dist[U]) for U in Sの部分集合)
        # dist[S]: 集合Sに含まれる点のペアの距離の最大値
        # つまり、集合Sを、i-1個のグループで構成される集合S-Uと、残りの点の集合Uに分割する
        U = S
        while U:
            dp[i][S] = min(dp[i][S], max(dp[i-1][S-U], dist[U]))
            # 次のUはU未満の最大のSの部分集合
            U = (U-1) & S

print(dp[K][(1<<N)-1])
