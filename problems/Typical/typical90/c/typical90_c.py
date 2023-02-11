import sys
sys.setrecursionlimit(10**6)

N = int(input())

edges = [[] for _ in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)

dist = [float('inf')] * N
dist[0] = 0
max_dist = {'node': -1, 'dist': -1}

def dfs(x, prev):
    for y in edges[x]:
        if y == prev:
            continue
        dist[y] = dist[x] + 1
        if max_dist['dist'] < dist[y]:
            max_dist['dist'] = dist[y]
            max_dist['node'] = y
        dfs(y, x)

dfs(0, -1)
dist = [float('inf')] * N
node = max_dist['node']
dist[node] = 0
max_dist = {'node': -1, 'dist': -1}
dfs(node, -1)

print(max_dist['dist'] + 1)
