# https://betrue12.hateblo.jp/entry/2018/12/08/000020
# 縦横の迷路のような、道の重みが０か１のグラフに対して使えるアルゴリズム
# 最短路の距離をO(|V|+|E|)で求めることができる

# graph: adjacency list
# H: height of graph
# W: width of graph
# s: start coordinate
# g: goal coordinate
def zero_one_BFS_graph(graph, H, W, sx, sy, gx, gy):
    from collections import deque

    INF = pow(10, 18)
    dist = [[INF for _ in range(W)] for __ in range(H)]

    dist[sy][sx] = 0
    que = deque()
    que.append([sx, sy])

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    while que:
        x, y = que.popleft()
        if x == gx and y == gy:
            break

        for sx, sy in zip(dx, dy):
            nx = x + sx
            ny = y + sy

            if 0 <= nx < W and 0 <= ny < H:
                if graph[ny][nx] == '#':
                    d = dist[y][x] + 1
                else:
                    d = dist[y][x]

                if d < dist[ny][nx]:
                    dist[ny][nx] = d
                    if graph[ny][nx] == '#':
                        que.append([nx, ny])
                    else:
                        que.appendleft([nx, ny])

    return dist

# edges: list of edges like [(j, c)] : j: to, c: cost
# N: number of nodes
# s: start node
def zero_one_BFS_edges(edges, N, s):
    from collections import deque

    INF = pow(10, 18)
    dist = [INF for _ in range(N)]

    dist[s] = 0
    que = deque()
    que.append(s)

    while que:
        i = que.popleft()
        for j, c in edges[i]:
            d = dist[i] + c
            if d < dist[j]:
                dist[j] = d
                if c == 1:
                    que.append(j)
                else:
                    que.appendleft(j)

    return dist


# https://atcoder.jp/contests/arc005/tasks/arc005_3

H, W = map(int, input().split())
graph = [list(input()) for _ in range(H)]

for h in range(H):
    for w in range(W):
        if graph[h][w] == 's':
            s = (w, h)
        if graph[h][w] == 'g':
            g = (w, h)

dist = zero_one_BFS_graph(graph, H, W, s[0], s[1], g[0], g[1])
if dist[g[1]][g[0]] <= 2:
    print('YES')
else:
    print('NO')
