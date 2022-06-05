N, M = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(M)]

one_to = []
N_to = []

for a, b in ab:
    if a == 1:
        one_to.append(b)
    elif b == 1:
        one_to.append(a)
    elif a == N:
        N_to.append(b)
    elif b == N:
        N_to.append(a)

if len(set(one_to)) + len(set(N_to)) == len(set(one_to + N_to)):
    print('IMPOSSIBLE')
else:
    print('POSSIBLE')