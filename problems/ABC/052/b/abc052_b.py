N = int(input())
S = input()

x = 0
ans = x
for s in S:
    if s == 'I':
        x += 1
    elif s == 'D':
        x -= 1
    ans = max(ans, x)

print(ans)