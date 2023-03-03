# 巡回セールスマン問題
# https://atcoder.jp/contests/abc274/tasks/abc274_e

def popcount(x):
    '''xの立っているビット数をカウントする関数
    (xは64bit整数)'''

    # 2bitごとの組に分け、立っているビット数を2bitで表現する
    x = x - ((x >> 1) & 0x5555555555555555)

    # 4bit整数に 上位2bit + 下位2bit を計算した値を入れる
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)

    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f # 8bitごと
    x = x + (x >> 8) # 16bitごと
    x = x + (x >> 16) # 32bitごと
    x = x + (x >> 32) # 64bitごと = 全部の合計
    return x & 0x0000007f

# 頂点0からスタートして、全ての頂点を1回ずつ通って頂点0に戻る時の最短経路の長さを求める
# d: 隣接行列: d[i][j] = iからjへの距離
def TSP(d):
    # dp[S][v]: 集合Sに含まれる頂点をすべて通り、頂点vにいる時に、他の頂点を全て通って頂点0に戻る最短経路の長さ
    # ただし、Sは頂点0を含まない

    INF = pow(10, 18)
    N = len(d)
    dp = [[INF] * N for _ in range(1 << N)]

    # 初期条件
    dp[(1 << N) - 1][0] = 0

    for s in range((1 << N) - 2, -1, -1):
        # sの状態でvにいる時の最小値

        # 既に原点を訪れているのに、全ての頂点を訪れていない場合はINFなので、計算しなくてよい
        if s & 1 and popcount(s) < N:
            continue

        for v in range(N):
            # 次にuに移る
            for u in range(N):
                # uをまだ訪れていない場合
                if not (s >> u) & 1:
                    dp[s][v] = min(dp[s][v], dp[s | 1 << u][u] + d[v][u])

    return dp[0][0]



# https://atcoder.jp/contests/abc180/tasks/abc180_e

N = int(input())
zahyo = [list(map(int, input().split())) for _ in range(N)]

d = [[-1] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        a = zahyo[i]
        p = zahyo[j]

        d[i][j] = abs(p[0] - a[0]) + abs(p[1] - a[1]) + max(0, p[2] - a[2])

print(TSP(d))
