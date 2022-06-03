S = list(input() for _ in range(12))

ans = 0
for i in range(12):
    if 'r' in S[i]:
        ans += 1

print(ans)