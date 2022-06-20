N = int(input())
LR = [list(map(int, input().split())) for _ in range(N)]

ans = []
LR.sort(key=lambda x: x[0])
left = LR[0][0]
right = LR[0][1]

for i in range(1, N):
    if LR[i][0] <= right:
        right = max(right, LR[i][1])
    else:
        ans.append([left, right])
        left = LR[i][0]
        right = LR[i][1]

ans.append([left, right])

for i in ans:
    print(i[0], i[1])