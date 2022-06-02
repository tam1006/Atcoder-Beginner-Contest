N = int(input())
A = [0]
A.extend(list(map(int, input().split())))
A.append(0)


money = 0
for i in range(N+2):
    money += abs(A[i-1] - A[i])

for i in range(1, N+1):
    ans = money
    ans -= abs(A[i] - A[i-1])
    ans -= abs(A[i+1] - A[i])
    ans += abs(A[i-1] - A[i+1])

    print(ans)

