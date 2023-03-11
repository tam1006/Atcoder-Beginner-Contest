H, W = map(int, input().split())
rs, cs = map(int, input().split())
rt, ct = map(int, input().split())
S = [input() for _ in range(H)]

rs -= 1
cs -= 1
rt -= 1
ct -= 1

from collections import deque

INF = pow(10, 9)
dist = [[INF for _ in range(W)] for _ in range(H)]

que = deque()

dist[rs][cs] = 0
for k in range(4):
    que.append((rs, cs, k, 0))

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

while que:
    qx, qy, qk, cost = que.popleft()

    for k in range(4):
        nx = qx + dx[k]
        ny = qy + dy[k]

        if 0 <= nx < H and 0 <= ny < W and S[nx][ny] == '.':
            if k == qk:
                d = cost
                if d <= dist[nx][ny]:
                    dist[nx][ny] = d
                    que.appendleft((nx, ny, k, d))
            else:
                d = cost + 1
                if d <= dist[nx][ny]:
                    dist[nx][ny] = d
                    que.append((nx, ny, k, d))

print(dist[rt][ct])
