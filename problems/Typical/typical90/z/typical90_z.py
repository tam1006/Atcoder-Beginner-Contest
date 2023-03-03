import sys
sys.setrecursionlimit(10 ** 9)

import platform
if platform.python_implementation() == 'PyPy':
    import pypyjit
    pypyjit.set_param('max_unroll_recursion=-1')

N = int(input())
color = [0] * N

# 隣接リスト
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

def dfs(v, c):
    color[v] = c
    for u in G[v]:
        if color[u] == c:
            return False
        if color[u] == 0:
            if not dfs(u, -c):
                return False
    return True

flag = dfs(0, 1)

a = []
b = []
for i in range(N):
    if color[i] == 1:
        a.append(i+1)
    else:
        b.append(i+1)

if len(a) > len(b):
    print(*a[:N//2])
else:
    print(*b[:N//2])
