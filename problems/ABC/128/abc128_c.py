import itertools

N, M = map(int, input().split())
k = []
s = []
for i in range(M):
    ks = list(map(int, input().split()))
    k.append(ks[0])
    s.append(ks[1:])
p = list(map(int, input().split()))

ans = 0
for i in range(2**N):
    tmp = [0]*M
    for j in range(N):
        if ((i >> j) & 1):
            for k in range(M):
                if j+1 in s[k]:
                    tmp[k] += 1
        
    flag = True
    for k in range(M):
        if tmp[k] % 2 != p[k]:
            flag = False
            break
    
    if flag:
        ans += 1

print(ans)
