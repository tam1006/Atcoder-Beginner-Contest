N, M = map(int, input().split())
X = list(map(int, input().split()))

if N >= M:
    print(0)
    exit()

# X.sort()
# diff = [[X[i] - X[i-1], i] for i in range(1, M)]
# diff.sort(reverse=True, key=lambda x: x[0])
# print(diff)

# flag = [False] * M
# for i in range(N):
#     flag[diff[i][1]] = True

# print(flag)