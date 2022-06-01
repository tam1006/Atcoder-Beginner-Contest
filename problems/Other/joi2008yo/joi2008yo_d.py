m = int(input())
star1 = list(tuple(map(int, input().split())) for _ in range(m))
n = int(input())
star2 = list(tuple(map(int, input().split())) for _ in range(n))

for mx, my in star1:
    for nx, ny in star2:
        dx = nx - mx
        dy = ny - my
        for i in range(m):
            lx, ly = star1[i]
            if (lx+dx, ly+dy) not in star2:
                break

            if i == m-1:
                print(dx, dy)
                exit()
