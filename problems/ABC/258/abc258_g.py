N = int(input())
A = list(list(input()) for _ in range(N))

ans = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        if A[i][j] == '1':
            

print(ans)