N = int(input())
A = list(map(int, input().split()))
X = int(input())

ans = 0
S = sum(A)
ans += (X//S)*N
X -= (X//S)*S

for i in range(N):
    if X >= 0:
        ans += 1
        X -= A[i]
    else:
        break

print(ans)
