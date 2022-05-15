S = input()

ans = 0
num = 0
for i in range(len(S)):
    if S[i] == 'W':
        ans += num
    else:
        num += 1

print(ans)