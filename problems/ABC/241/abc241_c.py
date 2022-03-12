N = int(input())
S  = list(input() for _ in range(N))

maze = [[True]*N for _ in range(N)]

def dfs(i, j, count=0):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if not maze[x][y]:
            continue

        if 0 <= x < N and 0 <= y < N and S[x][y]:
            dfs(x, y, count+1)

for i in range(N):
    for j in range(N):
        if maze[i][j]:
            if S[i][j] == '.':
                maze[i][j] = False
                continue

