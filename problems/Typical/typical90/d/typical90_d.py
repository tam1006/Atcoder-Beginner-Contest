H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

H_sum = [0] * H
W_sum = [0] * W

for h in range(H):
    for w in range(W):
        H_sum[h] += A[h][w]
        W_sum[w] += A[h][w]

for i in range(H):
    for j in range(W):
        print(H_sum[i] + W_sum[j] - A[i][j], end='')
        if j != W - 1:
            print(' ', end='')
    print()
