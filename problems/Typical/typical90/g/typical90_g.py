N = int(input())
A = list(map(int, input().split()))
Q = int(input())
B = []
for _ in range(Q):
    B.append(int(input()))

A.sort()
import bisect

for i in range(Q):
    index = bisect.bisect_left(A, B[i])
    if index == N:
        print(abs(A[index-1]-B[i]))
    elif index == 0:
        print(abs(A[index]-B[i]))
    else:
        print(min(abs(A[index]-B[i]), abs(A[index-1]-B[i])))
