N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        for k in range(N):
            if i == j or j ==k or k == i:
                continue
            x1 = [xy[i][0] - xy[j][0], xy[i][1] - xy[j][1]]
            x2 = [xy[i][0] - xy[k][0], xy[i][1] - xy[k][1]]
            if x1[0]*x2[1] == x1[1]*x2[0]:
                print('Yes')
                exit()

print('No')