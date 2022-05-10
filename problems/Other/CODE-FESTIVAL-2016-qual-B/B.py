N, A, B = map(int, input().split())
S = input()

a = 0
b = 0

for i in range(N):
    if S[i] == 'a':
        if a+b < A+B:
            a += 1
            print('Yes')
        else:
            print('No')
    elif S[i] == 'b':
        if a+b < A+B and b+1 <= B:
            b += 1
            print('Yes')
        else:
            print('No')
    else:
        print('No')
