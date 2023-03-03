# graph: 2D array of # and . : # is wall, . is path
# H: height of graph
# W: width of graph
# sx: start x
# sy: start y
# gx: goal x
# gy: goal y
def bfs(graph, H, W, sx, sy, gx, gy):
    from collections import deque
    # up, right, down, left
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    # initialize
    INF = pow(10, 18)
    dist = [[INF for _ in range(W)] for __ in range(H)]

    # start point
    dist[sy][sx] = 0
    que = deque()
    que.append([sx, sy])

    while que:
        x, y = que.popleft()
        if x == gx and y == gy:
            break

        for sx, sy in zip(dx, dy):
            nx = x + sx
            ny = y + sy

            if 0 <= nx < W and 0 <= ny < H and graph[ny][nx] != '#' and dist[ny][nx] == INF:
                dist[ny][nx] = dist[y][x] + 1
                que.append([nx, ny])

    return dist[gy][gx]

H, W = 10, 10
graph = [
    '#S######.#',
    '......#..#',
    '.#.##.##.#',
    '.#........',
    '##.##.####',
    '....#....#',
    '.#######.#',
    '....#.....',
    '.####.###.',
    '....#...G#',
    ]

for h in range(H):
    for w in range(W):
        if graph[h][w] == 'S':
            sx, sy = w, h

        if graph[h][w] == 'G':
            gx, gy = w, h

print(bfs(graph, H, W, sx, sy, gx, gy))
