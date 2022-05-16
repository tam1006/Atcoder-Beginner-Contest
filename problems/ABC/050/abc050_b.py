N = int(input())
T = list(map(int, input().split()))
M = int(input())
PX = [list(map(int, input().split())) for _ in range(M)]

total = sum(T)

for i in range(M):
    print(total - (T[PX[i][0]-1] - PX[i][1]))