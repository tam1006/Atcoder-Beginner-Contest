# 二部グラフ判定

# 与えられたグラフが二部グラフかどうかを判定する

N = int(input())
color = [0] * N

# 隣接リスト
G = [[] for _ in range(N)]

def dfs(v, c):
    color[v] = c
    for u in G[v]:
        if color[u] == c:
            return False
        if color[u] == 0:
            if not dfs(u, -c):
                return False
    return True


flag = dfs(0, 1)
