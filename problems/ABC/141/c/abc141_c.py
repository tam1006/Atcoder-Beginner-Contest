import collections

N, K, Q = map(int, input().split())
A = [int(input()) for _ in range(Q)]

c = collections.Counter(A)

for i in range(N):
    if c[i+1] <= Q - K:
        print('No')
    else:
        print('Yes')