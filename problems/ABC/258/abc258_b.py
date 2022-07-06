N = int(input())
A = list(list(input()) for _ in range(N))

direction = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

ans = 0
for i in range(N):
    for j in range(N):
        for dx, dy in direction:
            temp = ''
            for k in range(N):
                if k == 0:
                    x = i
                elif x + dx < 0:
                    x = N-1
                elif x + dx >= N:
                    x = 0
                else:
                    x += dx
                
                if k == 0:
                    y = j
                elif y + dy < 0:
                    y = N-1
                elif y + dy >= N:
                    y = 0
                else:
                    y += dy
                
                temp = temp + A[x][y]
            ans = max(ans, int(temp))

print(ans)

