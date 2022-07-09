N = int(input())
W = [input() for _ in range(N)]

duplicate = set(W)
if len(duplicate) != len(W):
    print('No')
    exit()

end = W[0][-1]
for i in range(1, N):
    start = W[i][0]
    if start != end:
        print('No')
        exit()
    end = W[i][-1]

print('Yes')