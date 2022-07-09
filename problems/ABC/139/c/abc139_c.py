N = int(input())
H = list(map(int, input().split()))

ans = 0
now = 0

for i in range(N-1):
    if H[i] >= H[i+1]:
        now += 1
        ans = max(ans, now)
    else:
        ans = max(ans, now)
        now = 0

print(ans)