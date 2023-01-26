import sys
sys.setrecursionlimit(10**6)

N = int(input())
X = list(map(int, input().split()))
C = list(map(int, input().split()))

# 0: not visited
# 1: visited(calculating)
# 2: visited(calculated)
visited = [0] * N

def dfs(now):
    if visited[now] == 1:
        return now

    if visited[now] == 2:
        return -1

    visited[now] = 1

    next = X[now] - 1
    res = dfs(next)

    visited[now] = 2

    if res != -1:
        cycles.append(C[now])
        if res == now:
            return -1
    return res

ans = 0
for i in range(N):
    if visited[i] > 0:
        continue

    cycles = []
    dfs(i)

    if len(cycles) > 0:
        ans += min(cycles)

print(ans)
