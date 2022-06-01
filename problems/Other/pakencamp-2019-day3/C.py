N, M = map(int, input().split())
A = list(list(map(int, input().split())) for _ in range(N))

ans = 0
for i in range(M):
    for j in range(M):
        if i == j:
            continue
        tmp = 0
        for k in range(N):
            tmp += max(A[k][i], A[k][j])
        ans = max(ans, tmp)

print(ans)