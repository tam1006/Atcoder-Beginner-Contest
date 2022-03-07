import numpy as np
n, k = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]

a = np.array(a)
ans = float("inf")
for i in range(n-k+1):
    for j in range(n-k+1):
        height = a[i:i+k, j:j+k]
        height = height.flatten()
        if k%2 == 0:
            height = np.insert(height, k**2, 0)
        
        # height = height.tolist()
        # height = height[0]
        # height.sort()
        # print(height)
        median = np.median(height)
        # print(median)
        if ans > median:
            ans = median

print(int(ans))
