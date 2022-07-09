S = input()

ans = 0
now = 0

for s in S:
    if s in ['A', 'C', 'G', 'T']:
        now += 1
        ans = max(ans, now)
    else:
        now = 0

print(ans)