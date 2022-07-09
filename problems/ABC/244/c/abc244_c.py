N = int(input())

num = [True for i in range(2*N+2)]
num[0] = False

ans = 1

print(ans)
ans += 1

for i in range(N):
    e = int(input())
    num[e] = False
    while num[ans] == False:
        ans += 1
    print(ans)
    num[ans] = False
    ans += 1