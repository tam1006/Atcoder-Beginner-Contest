N = int(input())
S = input()
W = list(map(int, input().split()))

for i in range(N):
    W[i] = [W[i], int(S[i])]

W.sort(key=lambda x:x[0])
num = sum(map(int, list(S)))

zero = 0
ans = max(num, N-num)
one = 0
for i in range(N):
    if W[i][1] == 0:
        zero += 1
    else:
        one += 1

    if i == N-1 or W[i][0] != W[i+1][0]:
        ans = max(ans, zero+(num-one))

print(ans)

