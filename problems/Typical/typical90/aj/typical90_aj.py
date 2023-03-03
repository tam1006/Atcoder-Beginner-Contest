N, Q = map(int, input().split())
x, y = [], []
for _ in range(N):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

q = [int(input()) for _ in range(Q)]

INF = pow(10, 10)
max_x, max_y, min_x, min_y = -INF, -INF, INF, INF

for i in range(N):
    X = x[i] - y[i]
    Y = x[i] + y[i]

    max_x = max(max_x, X)
    max_y = max(max_y, Y)
    min_x = min(min_x, X)
    min_y = min(min_y, Y)

for i in range(Q):
    X = x[q[i]-1] - y[q[i]-1]
    Y = x[q[i]-1] + y[q[i]-1]

    ans = max(abs(max_x - X), abs(max_y - Y), abs(min_x - X), abs(min_y - Y))
    print(ans)
