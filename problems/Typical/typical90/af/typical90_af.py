N = int(input())
A = list(list(map(int, input().split())) for _ in range(N))
M = int(input())
X, Y = [], []
for _ in range(M):
    x, y = map(int, input().split())
    X.append(x-1)
    Y.append(y-1)

edges = [[True] * N for _ in range(N)]
for i in range(M):
    edges[X[i]][Y[i]] = False
    edges[Y[i]][X[i]] = False

from itertools import permutations

ans = pow(10, 10)
l = [i for i in range(N)]

for p in permutations(l):
    t = 0
    flag = True
    for i in range(N-1):
        if not edges[p[i]][p[i+1]]:
            flag = False
            break
        t += A[p[i]][i]

    if flag:
        t += A[p[N-1]][N-1]
        ans = min(ans, t)

if ans == pow(10, 10):
    print(-1)
else:
    print(ans)
