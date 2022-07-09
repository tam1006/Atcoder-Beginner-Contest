N, M = map(int, input().split())
import itertools

friend = [[False]*(N+1) for _ in range(N+1)]

for i in range(M):
    x, y = map(int, input().split())
    friend[x][y] = True
    friend[y][x] = True

ans = 0
for i in range(2**N):
    tmp = []
    for j in range(N):
        if ((i >> j) & 1):
            tmp.append(j+1)
        
    flag = True
    for k in itertools.combinations(tmp, 2):
        if not friend[k[0]][k[1]]:
            flag = False
            break
    
    if flag:
        ans = max(ans, len(tmp))

print(ans)