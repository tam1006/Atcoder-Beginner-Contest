N = int(input())
W = list(map(int, input().split()))
B = list(map(int, input().split()))

w_max = 50
b_max = 50 + 50*51 // 2

Grundy = [[0] * (b_max+1) for _ in range(w_max+1)]

def mex(s):
    for i in range(600):
        if i not in s:
            return i

for w in range(w_max+1):
    for b in range(b_max+1):
        if w < 1 and b < 2:
            continue

        s = set()
        for k in range(1, (b//2)+1):
            s.add(Grundy[w][b-k])

        if w >= 1 and b+w < b_max+1:
            s.add(Grundy[w-1][b+w])

        Grundy[w][b] = mex(s)

xor = 0
for i in range(N):
    xor ^= Grundy[W[i]][B[i]]

if xor == 0:
    print('Second')
else:
    print('First')

