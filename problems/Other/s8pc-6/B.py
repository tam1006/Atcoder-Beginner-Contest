N = int(input())
A = []
B = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

A.sort()
B.sort()

s = A[N//2]
g = B[N//2]

ans = 0
for a, b in zip(A, B):
    ans += abs(a - s) + abs(b - g)
    ans += b - a

print(ans)