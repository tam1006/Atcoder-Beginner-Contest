N = int(input())
a = list(map(int, input().split()))

ans = 0
i = 1

for j in range(N):
    if a[j] != i:
        ans += 1
    else:
        i += 1

if ans == N:
    print(-1)
else:
    print(ans)