import math
A = int(input())
B = int(input())

A = math.log(A)
B = math.log(B)

if A > B:
    print('GREATER')
elif A < B:
    print('LESS')
else:
    print('EQUAL')