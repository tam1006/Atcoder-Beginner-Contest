import numpy as np

N, A, B = map(int, input().split())
tile = np.full((N*A, N*B), '*')

color = '.'
for i in range(0, N*A, A):
    if i != 0:
        color = '#' if tile[i-1][0] == '.' else '.'
    for j in range(0, N*B, B):
        tile[i:i+A, j:j+B] = np.full((A, B), color)
        color = '#' if color == '.' else '.'

for i in range(0, N*A):
    print(''.join(tile[i, :]))
