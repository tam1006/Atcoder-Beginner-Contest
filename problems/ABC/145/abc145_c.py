N = int(input())
coordinate = list(tuple(map(int, input().split())) for _ in range(N))

from itertools import permutations

n = 1
for i in range(1, N+1):
    n *= i

ans = 0
for p in permutations(coordinate):
    tmp = 0
    for i in range(N-1):
        tmp += ((p[i][0] - p[i+1][0])**2 + (p[i][1] - p[i+1][1])**2)**0.5
    ans += tmp / n

print(ans)
