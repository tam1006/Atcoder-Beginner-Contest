# 二部グラフ判定

import sys
sys.setrecursionlimit(10**9)

# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_ao
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

color = [0 for _ in range(N)]

def dfs(v, c):
    color[v] = c
    for u in G[v]:
        if color[u] == c:
            return False
        # if color[u] == 0 and not dfs(v, -c):
        if color[u] == 0:
            if not dfs(u, -c):
                return False

    return True

def bipartite_graph():
    for i in range(N):
        if color[i] == 0:
            if not dfs(i, 1):
                return False

    return True

if bipartite_graph():
    print('Yes')
else:
    print('No')
