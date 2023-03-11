N, M = map(int, input().split())
edges = [[] for _ in range(N+M)]

from collections import deque

for i in range(M):
    K = int(input())
    R = list(map(int, input().split()))

    for r in R:
        edges[N+i].append(r-1)
        edges[r-1].append(N+i)


que = deque()
que.append(0)

INF = pow(10, 10)
dist = [INF] * (N+M)
dist[0] = 0

while que:
    q = que.popleft()

    for e in edges[q]:
        if dist[e] == INF:
            dist[e] = dist[q] + 1
            que.append(e)

for i in range(N):
    if dist[i] == INF:
        print(-1)
    else:
        print(dist[i]//2)
