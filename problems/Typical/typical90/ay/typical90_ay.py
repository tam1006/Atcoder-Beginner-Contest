N, K, P = map(int, input().split())
A = list(map(int, input().split()))

import bisect

n = N//2
m = N - n
zenhan = [[] for _ in range(n + 1)]
kohan = [[] for _ in range(m + 1)]


for i in range(1 << n):
    total = 0
    count = 0
    for j in range(n):
        if i >> j & 1:
            total += A[j]
            count += 1

    zenhan[count].append(total)

for i in range(1 << m):
    total = 0
    count = 0
    for j in range(m):
        if i >> j & 1:
            total += A[n+j]
            count += 1

    kohan[count].append(total)

for i in range(len(zenhan)):
    zenhan[i].sort()

for i in range(len(kohan)):
    kohan[i].sort()


ans = 0
for i in range(len(zenhan)):
    for money in zenhan[i]:
        if money > P:
            break
        if 0 <= K-i < len(kohan): 
            ans += bisect.bisect_right(kohan[K-i], P-money)

print(ans)
