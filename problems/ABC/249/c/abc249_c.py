N, K = map(int, input().split())
S = list(input() for _ in range(N))

from itertools import combinations
from collections import defaultdict

ans = 0
for i in range(1, N+1):
    for p in combinations(range(N), i):
        tmp = defaultdict(int)
        tmp_num = 0
        for i in p:
            for s in S[i]:
                tmp[s] += 1
        
        for v in tmp.values():
            if v == K:
                tmp_num += 1
        
        ans = max(ans, tmp_num)

print(ans)