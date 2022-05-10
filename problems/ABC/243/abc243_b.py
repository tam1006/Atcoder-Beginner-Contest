N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

AandB = set(A) & set(B)

same = 0
for i in range(N):
    if A[i] == B[i]:
        same += 1

print(same)
print(len(AandB) - same)