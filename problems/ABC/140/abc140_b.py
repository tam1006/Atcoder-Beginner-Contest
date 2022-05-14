N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = 0
before = -1
for i in range(N):
    ans += B[A[i]-1]
    if A[i] - 1 == before:
        ans += C[before-1]
    before = A[i]

print(ans)