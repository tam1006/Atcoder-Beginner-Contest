N = int(input())
D, X = map(int, input().split())

A = []
for i in range(N):
    A.append(int(input()))

num = X
for i in range(N):
    day = 1
    num += 1
    while day <= D:
        if day + A[i] <= D:
            day += A[i]
            num += 1
        else:
            break

print(num)