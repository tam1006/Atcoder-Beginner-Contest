from collections import defaultdict
import numpy as np

N = int(input())
S = list(np.array(list(input())) for i in range(N))

arg = np.argsort(S, axis=1)
ans = float('inf')

for i in range(10):
    time = arg[:, i]
    time = list(np.sort(time))
    for j, t in enumerate(time):
        if j == 0:
            continue

        elif time[j] == time[j-1]:
            time.append(time[j]+10)
    
    time.sort()
    if time[-1] < ans:
        ans = time[-1]

print(ans)
