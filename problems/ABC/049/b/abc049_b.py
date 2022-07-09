H, W = map(int, input().split())
C = [list(input()) for _ in range(H)]

for i in range(2*H):
    for j in range(W):
        print(C[(i)//2][j], end='')
    print()