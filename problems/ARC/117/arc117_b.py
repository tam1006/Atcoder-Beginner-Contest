N = int(input())
A = list(map(int, input().split()))

A.sort()

ans = A[0] + 1
for i in range(1, N):
    ans *= (A[i] - A[i-1] + 1)
    ans %= 1000000007

print(ans)