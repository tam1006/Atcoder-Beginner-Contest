N = int(input())
K = int(input())
x = list(map(int, input().split()))

ans = 0
for i in range(N):
    ans += min(x[i], K-x[i])*2

print(ans)