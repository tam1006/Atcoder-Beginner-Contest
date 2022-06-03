N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

W = S - R + 1
H = Q - P + 1

mass = [['.']*W for _ in range(H)]

k_min = max(1-A, 1-B)
min_condision = max(P-A, R-B)
k_min = max(k_min, min_condision)

k_max = min(N-A, N-B) + 1
max_condision = min(H+P-A, W+R-B)
k_max = min(k_max, max_condision)

for k in range(k_min, k_max):
    h = A+k - P
    w = B+k - R

    if h < 0 or w < 0 or h >= H or w >= W:
        # print(h, w)
        continue

    mass[h][w] = '#'


for k in range(max(B-S, P-A), min(Q-A+1, B-R+1)):
    h = A+k - P
    w = B-k - R

    if h < 0 or w < 0 or h >= H or w >= W:
        # print(h, w)
        continue

    mass[h][w] = '#'

for i in range(H):
    print(''.join(mass[i]))