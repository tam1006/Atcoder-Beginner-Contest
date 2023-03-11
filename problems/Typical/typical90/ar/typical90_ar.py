N, Q = map(int, input().split())
A = list(map(int, input().split()))

n = 0
for i in range(Q):
    T, x, y = map(int, input().split())
    x -= 1
    y -= 1

    if T == 1:
        x = (x - n) % N
        y = (y - n) % N
        A[x], A[y] = A[y], A[x]
    elif T == 2:
        n = (n + 1) % N
    else:
        x = (x - n) % N
        print(A[x])
