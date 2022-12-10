N, M = map(int, input().split())
from collections import defaultdict
dist = defaultdict(dict)
import sys
sys.setrecursionlimit(10**6)

for i in range(M):
    x, y = map(int, input().split())
    dist[x-1][y-1] = 1

from functools import lru_cache
@lru_cache(maxsize=None)
def dfs(v, path):
    max_path = 0
    for key, value in dist[v].items():
        max_path = max(max_path, dfs(key, path + value))

    return max_path

print(dfs(0, 0))
