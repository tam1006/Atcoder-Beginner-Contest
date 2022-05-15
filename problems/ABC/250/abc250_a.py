H, W = map(int, input().split())
R, C = map(int, input().split())

ans = 0
for i in range(1, H+1):
    for j in range(1, W+1):
        if abs(i - R) + abs(j - C) == 1:
            ans += 1

print(ans)