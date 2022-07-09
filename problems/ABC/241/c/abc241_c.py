N = int(input())
S  = list(input() for _ in range(N))

for i in range(N):
    for j in range(N):
        tate = []
        yoko = []
        naname1 = []
        naname2 = []
        for k in range(6):
            if i+k < N:
                tate.append(S[i+k][j])
            if j+k < N:
                yoko.append(S[i][j+k])
            if i+k < N and j+k < N:
                naname1.append(S[i+k][j+k])
            if i+k < N and -j-k-1 >= 0:
                naname2.append(S[i+k][-j-k-1])
        
        if tate.count('#') >= 4 or yoko.count('#') >= 4 or naname1.count('#') >= 4 or naname2.count('#') >= 4:
            print('Yes')
            exit()

print('No')
