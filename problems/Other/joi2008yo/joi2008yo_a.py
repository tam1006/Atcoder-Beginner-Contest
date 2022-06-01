n = int(input())
A = list(map(int, input().split()))
int(input())
m_list = list(map(int, input().split()))

ans = [[False for _ in range(2001)] for i in range(n+1)]
ans[0][0] = True

for i in range(n):
    for j in range(2001):
        if ans[i][j]:
            ans[i+1][j] = True
            ans[i+1][j+A[i]] = True


for m in m_list:
    if ans[-1][m]:
        print("yes")
    else:
        print("no")