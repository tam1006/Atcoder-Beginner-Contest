R, C = map(int, input().split())
a = list(list(map(int, input().split())) for _ in range(R))

ans = 0
for i in range(2**R):
    now = [[0]*C for _ in range(R)]
    for j in range(R):
        if ((i >> j) & 1):
            for k in range(C):
                if a[j][k] == 0:
                    now[j][k] = 1
                else:
                    now[j][k] = 0
        else:
            for k in range(C):
                now[j][k] = a[j][k]
    
    tmp = 0
    for j in range(C):
        s = sum(now[k][j] for k in range(R))
        tmp += max(s, R-s)
    
    ans = max(ans, tmp)

print(ans)