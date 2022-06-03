S = input()
N = len(S)

a = 'oxx' * (N+2)

if S in a:
    print('Yes')
else:
    print('No')