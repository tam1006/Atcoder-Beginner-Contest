g = [list(input()) for i in range(10)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(x, y):
    field[x][y] = "x"

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx and nx< 10 and 0 <= ny and ny < 10 and field[nx][ny] == "o":
            dfs(nx, ny)

for i in range(10):
    for j in range(10):
        if g[i][j] == "x":
            # なぜcopyだと上手くいかないのか不明
            # field = g.copy()
            field = [k[:] for k in g]
            field[i][j] = 'o'
            
            # for a in g:
            #     print(*a)

            count = 0

            for p in range(10):
                for q in range(10):
                    if field[p][q] == 'o':
                        dfs(p, q)
                        count += 1
            
            if count == 1:
                print("YES")
                exit()

print("NO")
