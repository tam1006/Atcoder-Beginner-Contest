N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A_mod = [0] * 46
B_mod = [0] * 46
C_mod = [0] * 46

for i in range(N):
    A_mod[A[i] % 46] += 1
    B_mod[B[i] % 46] += 1
    C_mod[C[i] % 46] += 1

ans = 0
for i in range(46):
    for j in range(46):
        # k = (46 - i - j) % 46
        for k in range(46):
            if (i+j+k) % 46 == 0:
                ans += A_mod[i] * B_mod[j] * C_mod[k]

print(ans)
