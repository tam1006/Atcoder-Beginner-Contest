N, T = map(int, input().split())
A = list(map(int, input().split()))

if sum(A) % T == 0:
    print(sum(A) // T)
else:
    print(sum(A) // T + 1)