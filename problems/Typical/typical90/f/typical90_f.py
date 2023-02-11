N, K = map(int, input().split())
S = input()

c = [[0] * (N + 1) for _ in range(26)]

for i in range(26):
    index = -1
    for j in range(N-1, -1, -1):
        if S[j] == chr(ord('a') + i):
            index = j
        c[i][j] = index

ans = ''
j = 0
while len(ans) < K:
    index = -1
    for i in range(26):
        if c[i][j] == -1 or (N-c[i][j]) + len(ans) < K:
            continue
        index = i
        break
    ans += chr(ord('a') + index)
    j = c[index][j] + 1


print(ans)
