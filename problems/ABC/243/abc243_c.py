import numpy as np

N = int(input())
G = []
for i in range(N):
    G.append(list(map(int, input().split())))
S = input()

arg = np.argsort(G, axis=0)
i = 0
while i < N:
    flag = True
    r_min = 10**9+1
    l_max = -1

    if S[arg[i, 1]] == 'R':
        if G[arg[i, 1]][0] < r_min:
            r_min = G[arg[i, 1]][0]
    else:
        if G[arg[i, 1]][0] > l_max:
            l_max = G[arg[i, 1]][0]
    
    while flag:
        if i+1 >= N:
            print('No')
            exit()

        if G[arg[i, 1]][1] != G[arg[i+1, 1]][1]:
            flag = False
        else:
            if S[arg[i+1, 1]] == 'R':
                if G[arg[i+1, 1]][0] < r_min:
                    r_min = G[arg[i+1, 1]][0]
            else:
                if G[arg[i+1, 1]][0] > l_max:
                    l_max = G[arg[i+1, 1]][0]
        i += 1
    
    if l_max > r_min:
        print('Yes')
        exit()
