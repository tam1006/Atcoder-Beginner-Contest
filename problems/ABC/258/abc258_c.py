N, Q = map(int, input().split())
S = input()
que = list(tuple(map(int, input().split())) for _ in range(Q))

zero = 0
for q in que:
    if q[0] == 2:
        print(S[zero + q[1] - 1])
    else:
        zero -= q[1]
        if zero < -N:
            zero += N