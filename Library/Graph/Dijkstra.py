# ダイクストラ法
# 負の辺があるときは使えない
# 取り出す頂点ごとに最短距離が決まっていく
# 計算量はO(|E|log|V|)


# N: number of nodes
# edges: list of edges like List[List[(j, c)]] : j: to, c: cost]
def dijkstra(N, edges, s):
    import heapq

    INF = pow(10, 18)
    dist = [INF for _ in range(N)]
    dist[s] = 0

    que = []
    heapq.heappush(que, (0, s))

    while que:
        d, i = heapq.heappop(que)

        if d > dist[i]:
            continue

        for to, cost in edges[i]:
            if dist[to] > dist[i] + cost:
                dist[to] = dist[i] + cost
                heapq.heappush(que, (dist[to], to))

    return dist
