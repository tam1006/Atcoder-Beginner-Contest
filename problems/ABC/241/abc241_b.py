import collections

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a = collections.Counter(A)
b = collections.Counter(B)

for k, v in b.items():
    if v > a[k]:
        print('No')
        exit()

print('Yes')