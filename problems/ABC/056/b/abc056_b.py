W, a, b = map(int, input().split())

if b > a+W:
    ans = b - (a+W)
elif b+W < a:
    ans = a - (b+W)
else:
    ans = 0

print(ans)