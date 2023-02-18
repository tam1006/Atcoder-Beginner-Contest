N = int(input())

C, P = [], []
for _ in range(N):
    c, p = map(int, input().split())
    C.append(c)
    P.append(p)

S1 = [0]
S2 = [0]

for i in range(N):
    if C[i] == 1:
        S1.append(S1[-1] + P[i])
        S2.append(S2[-1])
    else:
        S1.append(S1[-1])
        S2.append(S2[-1] + P[i])

Q = int(input())

for _ in range(Q):
    L, R = map(int, input().split())

    print(f"{S1[R] - S1[L-1]} {S2[R] - S2[L-1]}")

