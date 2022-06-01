W = list(input())

ans = []
for i in range(len(W)):
    if not W[i] in ['a', 'i', 'u', 'e', 'o']:
        ans.append(W[i])

print(''.join(ans))
