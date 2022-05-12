N = int(input())
H = list(map(int, input().split()))

ans = 1
highest = H[0]
for i in range(1, N):
    if H[i] >= highest:
        highest = H[i]
        ans += 1

print(ans)