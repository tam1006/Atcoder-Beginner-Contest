S = list(input())
Q = int(input())
query = [input().split() for _ in range(Q)]

from collections import deque

S = deque(S)
isReverse = False

for q in query:
    if q[0] == '1':
        isReverse = not isReverse
    else:
        if q[1] == '1':
            if isReverse:
                S.append(q[2])
            else:
                S.appendleft(q[2])
        else:
            if isReverse == 1:
                S.appendleft(q[2])
            else:
                S.append(q[2])

S = list(S)
if isReverse == 1:
    S = S[::-1]

print(''.join(S))