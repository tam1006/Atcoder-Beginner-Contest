N, A, B = map(int, input().split())

ans = 0

for i in range(1, N+1):
    num = list(str(i))
    s = sum(int(x) for x in num)
    if A <= s <= B:
        ans += i

print(ans)