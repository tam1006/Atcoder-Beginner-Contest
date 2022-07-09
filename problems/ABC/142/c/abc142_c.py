import numpy as np

N = int(input())
A = list(map(int, input().split()))

ans = np.argsort(A) + 1
ans = [str(a) for a in ans]
ans = ' '.join(ans)
print(ans)