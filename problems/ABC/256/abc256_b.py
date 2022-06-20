N = int(input())
A = list(map(int, input().split()))

P = 0
mass = [0, 0, 0, 0]

for i in range(N):
    mass[0] += 1
    tmp = [0, 0, 0, 0]
    for j in range(4):
        if j + A[i] <= 3:
            tmp[j + A[i]] += mass[j]
        else:
            P += mass[j]
    mass = tmp

print(P)
