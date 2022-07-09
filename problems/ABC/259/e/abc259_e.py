N = int(input())

from collections import defaultdict
d_num = defaultdict(int)
d_index = defaultdict(int)
num = defaultdict(int)

for i in range(N):
    m = int(input())
    for j in range(m):
        p, e = map(int, input().split())
        if d_num[p] < e:
            d_num[p] = e
            d_index[p] = i
            num[p] = 0
        elif d_num[p] == e:
            num[p] = 1

ans = min(len(set(d_index.values()))+1-sum(num.values()), N)
print(ans)