N = int(input())
D = list(map(int, input().split()))
M = int(input())
T = list(map(int, input().split()))

D.sort()
T.sort()

i = 0
for j in range(M):
    if i >= N:
        print('NO')
        exit()
    
    while D[i] != T[j]:
        i += 1
        if i >= N:
            print('NO')
            exit()
    i += 1

print('YES')