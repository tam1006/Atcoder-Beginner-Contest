X = int(input())

from collections import deque

deq = deque()
deq.append(0)
i = 0

flag = True
while flag:
    tmp = []
    while deq:
        d = deq.pop()
        tmp.append(d)
        tmp.append(abs(d+i))
        tmp.append(abs(d-i))
        if d+i == X or d-i == X:
            flag = False
            break
    i += 1
    deq = deque(list(set(tmp)))
    print(deq)
    input()

print(i-1)
