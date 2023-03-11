N = int(input())

A = list(list(map(int, input().split())) for _ in range(N))

MOD = 10**9 + 7

res = 1
for a in A:
    res *= sum(a)
    res %= MOD

print(res)
