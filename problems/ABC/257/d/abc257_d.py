N = int(input())
xyP = []
zahyo = []
P = []
for i in range(N):
    xyP = list(map(int, input().split()))

    zahyo.append((xyP[0], xyP[1]))
    P.append(xyP[2])

S = [[0]*N for i in range(N)]

for i in range(N):
    for j in range(N):
        S[i][j] = (abs(zahyo[i][0] - zahyo[j][0]) + abs(zahyo[i][1] - zahyo[j][1])) / P[j]
        S[i][j] = (abs(zahyo[i][0] - zahyo[j][0]) + abs(zahyo[i][1] - zahyo[j][1])) / P[i]

for i in range(N):
    for j in range(N):
        S[i][j] = min(S[i][k] + S[k][j] for k in range(N))

for i in range(N):
    print(*S[i])