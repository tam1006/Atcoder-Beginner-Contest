N, K = map(int, input().split())

primes = [0] * (N+1)
ans = 0

for i in range(2, N+1):
    if primes[i] == 0:
        x = i
        while x <= N:
            primes[x] += 1
            x += i

    if primes[i] >= K:
        ans += 1

print(ans)
