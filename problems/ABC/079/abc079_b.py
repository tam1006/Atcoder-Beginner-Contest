N = int(input())

L = [2, 1]
while len(L) <= N:
    L.append(L[-1] + L[-2])

print(L[N])