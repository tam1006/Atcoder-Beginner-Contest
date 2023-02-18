N, M = map(int, input().split())
A, B, C = [], [], []

for _ in range(M):
    a, b, c = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)

edges = [[] for _ in range(N)]

for i in range(M):
    edges[A[i]-1].append((B[i]-1, C[i]))
    edges[B[i]-1].append((A[i]-1, C[i]))

import heapq
INF = pow(10, 18)

d_1 = [INF] * N
d_1[0] = 0

d_N = [INF] * N
d_N[N-1] = 0

def dijkstra(s, d):
    que = []
    heapq.heappush(que, (0, s))

    while que:
        cost, v = heapq.heappop(que)

        if d[v] < cost:
            continue

        for nv, ncost in edges[v]:
            if d[nv] > cost + ncost:
                d[nv] = cost + ncost
                heapq.heappush(que, (d[nv], nv))

dijkstra(0, d_1)
dijkstra(N-1, d_N)

for i in range(N):
    print(d_1[i] + d_N[i])
