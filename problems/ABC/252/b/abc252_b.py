import numpy as np

N, K = map(int, input().split())
A = np.array(list(map(int, input().split())))
B = list(map(int, input().split()))

ma = np.argsort(A)[::-1]

saidai = -1
for i in ma:
    if A[i] >= saidai:
        saidai = A[i]
        if i+1 in B:
            print('Yes')
            exit()
    else:
        break

print('No')