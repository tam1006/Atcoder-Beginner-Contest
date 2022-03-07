N, M = map(int, input().split())
g = [[]*N for i in range(N)]
for i in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)

# 訪れたことがあるか
memo = [False for i in range(N)]

def dfs(now, prev):
    global flag

    for next in g[now]:
        if next != prev:
            if memo[next]:
                flag = False
            else:
                memo[next] = True
                dfs(next, now)

ans = 0
for i in range(N):
    if not memo[i]:
        flag = True
        dfs(i, -1)
        if flag:
            # 閉路がなければ木
            ans += 1

print(ans)
