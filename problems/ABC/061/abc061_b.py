from collections import Counter

N, M = map(int, input().split())
ab = []
for i in range(M):
    x = list(map(int, input().split()))
    ab.append(x[0])
    ab.append(x[1])

c = Counter(ab)
for i in range(N):
    print(c[i+1])