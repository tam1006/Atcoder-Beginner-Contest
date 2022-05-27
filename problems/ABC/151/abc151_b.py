N, K, M = map(int, input().split())
A = list(map(int, input().split()))

rest = max(0, M*N - sum(A))

if rest > K:
    print(-1)
else:
    print(rest)