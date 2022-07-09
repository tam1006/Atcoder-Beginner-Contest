N, M = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(M)]
Q = int(input())
xk = [tuple(map(int, input().split())) for _ in range(Q)]

from collections import defaultdict
import sys

sys.setrecursionlimit(10**3)

graph = defaultdict(list)

def dfs(x, k, times, ans):
    if times >= k:
        return ans
        
    for u in graph[x]:
        ans.append(u)
        ans = dfs(u, k, times+1, ans)
    
    return ans

for i in range(M):
    graph[ab[i][0]].append(ab[i][1])
    graph[ab[i][1]].append(ab[i][0])

for i in range(Q):
    x, k = xk[i]
    ans = dfs(x, k, 0, [x])
    print(sum(set(ans)))
