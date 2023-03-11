import sys
sys.setrecursionlimit(10**6)

N = int(input())
A, B = [], []
for _ in range(N-1):
    a, b = map(int, input().split())
    A.append(a-1)
    B.append(b-1)
Q = int(input())
que = list(list(map(int, input().split())) for _ in range(Q))

if N > 5000 or Q > 5000:
    print("N or Q is too large")
    exit()

edges = [[] for _ in range(N)]
for i in range(N-1):
    edges[A[i]].append(B[i])
    edges[B[i]].append(A[i])

def dfs(i, parent):
    global ans
    if i+1 in necessary_v:
        dp[i] += 1

    for j in edges[i]:
        if j == parent:
            continue

        dfs(j, i)

        dp[i] += dp[j]

    if 1 <= dp[i] <= k-1:
        ans += 1
    return dp[i]

for i in range(Q):
    dp = [0] * N
    k, necessary_v = que[i][0], set(que[i][1:])
    ans = 0
    dfs(0, -1)
    print(ans)

