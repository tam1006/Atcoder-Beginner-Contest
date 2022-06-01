N = int(input())
S = [input() for _ in range(N)]

color = [0, 0]

for i in range(N):
    if S[i] == 'black':
        color[0] += 1
    else:
        color[1] += 1

if color[0] > color[1]:
    print('black')
else:
    print('white')