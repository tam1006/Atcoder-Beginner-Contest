N, X = map(int, input().split())
L = []
a = []
for i in range(N):
    La = list(map(int, input().split()))
    L.append(La[0])
    a.append(La[1:])

nums = [n for n in a[0]]
ans = 0

for i in range(1, N):
    if i < N-1:
        tmp = []
        for j in range(len(nums)):
            for k in range(L[i]):
                tmp.append(nums[j]*a[i][k])
        nums = tmp
    else:
        for j in range(len(nums)):
            for k in range(L[i]):
                if nums[j]*a[i][k] == X:
                    ans += 1

print(ans)