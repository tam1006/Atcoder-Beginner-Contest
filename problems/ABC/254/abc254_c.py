N, K = map(int, input().split())
a = list(map(int, input().split()))

ak = [[] for _ in range(K)]

for i in range(N):
    ak[i%K].append(a[i])

for i in range(K):
    ak[i].sort()

a_sort = sorted(a)

for i in range(N):
    if a_sort[i] != ak[i%K][i//K]:
        print('No')
        exit()

print('Yes')