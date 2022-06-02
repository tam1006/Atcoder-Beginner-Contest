N = int(input())

if N % sum(map(int, list(str(N)))) == 0:
    print('Yes')
else:
    print('No')