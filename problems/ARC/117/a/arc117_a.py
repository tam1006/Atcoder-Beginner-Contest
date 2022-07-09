A, B = map(int, input().split())

E = []
if A < B:
    A_flag = False
else:
    A_flag = True


if A_flag:
    b_max = 0
    for i in range(1, A+1):
        E.append(i)
        if i >= B:
            b_max += -i
    
    for i in range(1, B):
        E.append(-i)
    
    E.append(b_max)

else:
    a_max = 0
    for i in range(1, B+1):
        E.append(-i)
        if i >= A:
            a_max += i
    
    for i in range(1, A):
        E.append(i)
    
    E.append(a_max)

print(*E)