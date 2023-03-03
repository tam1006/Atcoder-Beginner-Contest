# ベルマンフォード法
# 負の辺があっても動く。負の閉路の検出にも使用できる。
# 計算量はO(|V| x |E|)。ただし、Vは頂点数、Eは辺数。

# edges: list of edges like [(i, j, c)] : i: from, j: to, c: cost
# N: number of nodes
# s: start node

def shortest_path(edges, N, E, s):
    INF = pow(10, 18)
    # dist = [INF for _ in range(N)]
    dist = [INF] * N
    dist[s] = 0

    for j in range(N):
        update = False
        # for i in range(E):
        for e in edges:
            u = e[0]
            v = e[1]
            c = e[2]

            if dist[u] != INF and dist[v] > dist[u] + c:
                dist[v] = dist[u] + c
                # update = True    # 単に負閉路を検出するだけならこれでいい

                # 頂点Nに関連する、負閉路があるかどうかであれば、このように書く
                if v == N-1:
                    update = True

        if not update:
            break

        if j == N-1 and update:
            # print('Negative cycle')
            return False

    return dist


# https://atcoder.jp/contests/abc061/tasks/abc061_d
N, M = map(int, input().split())
edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edges.append([a, b, -c])

dist = shortest_path(edges, N, M, 0)
if dist:
    print(-dist[N-1])
else:
    print('inf')
