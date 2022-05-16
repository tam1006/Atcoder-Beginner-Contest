N = int(input())
S, T = input().split()

ans = []
for i in range(N):
    ans.append(S[i] + T[i])

print(''.join(ans))