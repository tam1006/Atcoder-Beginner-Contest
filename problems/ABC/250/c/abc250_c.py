N, Q = map(int, input().split())
x = [int(input()) for _ in range(Q)]

def swap(boll_num, index, i, j):
    boll_1 = boll_num[i]
    boll_2 = boll_num[j]

    index[boll_1] = j
    index[boll_2] = i

    boll_num[i] = boll_2
    boll_num[j] = boll_1

boll = [i for i in range(1, N+1)]
boll_index = dict()
for i in range(1, N+1):
    boll_index[i] = i-1

for i in range(Q):
    if boll_index[x[i]] == N-1:
        target = boll_index[x[i]] - 1
        original = boll_index[x[i]]
    else:
        target = boll_index[x[i]] + 1
        original = boll_index[x[i]]

    swap(boll, boll_index, original, target)


print(*boll)
