N, X = map(int, input().split())
A = []
B = []
for i in range(N):
    AB = list(map(int, input().split()))
    A.append(AB[0])
    B.append(AB[1])

ans = float('inf')
min_b = B[0]
before_time = 0

for i in range(N):
    if i > X-1:
        break
    min_b = min(min_b, B[i])
    tmp_time = before_time + A[i] + B[i]
    before_time = tmp_time
    tmp_time += min_b * (X - (i+1))
    ans = min(ans, tmp_time)

print(ans)