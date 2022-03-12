N = int(input())
a = list(map(int, input().split()))

res = []
for i in range(N):
    res.append(a[i])
    # print(res[-a[i]:])
    if len(res) >= a[i] and res[-a[i]:] == [a[i]]*a[i]:
        res = res[:-a[i]]
    print(len(res))
    # print(res)