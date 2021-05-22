# AtcoderのABC問題のリポジトリです

## グラフ問題の入力の受け方
N, M = map(int, input().split())
g = [[]*N for i in range(N)]
for i in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)

これでgのインデックスに、繋がっている頂点が格納される。