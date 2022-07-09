N, X = map(int, input().split())
m = [int(input()) for _ in range(N)]

m.sort()


print(N + (X-sum(m[:N]))//m[0])