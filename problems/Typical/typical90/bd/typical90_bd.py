N, S = map(int, input().split())
A, B = [], []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

dp = [[False] * (S+1) for _ in range(N+1)]
dp[0][0] = True

for i in range(N):
    for j in range(S+1):
        if dp[i][j]:
            if j + A[i] <= S:
                dp[i+1][j+A[i]] = True

            if j + B[i] <= S:
                dp[i+1][j+B[i]] = True

if dp[N][S]:
    ans = ''
    for i in range(N, 0, -1):
        if S-A[i-1] >= 0 and dp[i-1][S-A[i-1]]:
            ans = 'A' + ans
            S -= A[i-1]
        else:
            ans = 'B' + ans
            S -= B[i-1]

    print(ans)
else:
    print('Impossible')
