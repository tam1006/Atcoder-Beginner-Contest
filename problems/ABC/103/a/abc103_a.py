A = list(map(int, input().split()))

cost = [abs(A[0] - A[1]), abs(A[1] - A[2]), abs(A[2] - A[0])]
cost.sort()

print(sum(cost[:2]))