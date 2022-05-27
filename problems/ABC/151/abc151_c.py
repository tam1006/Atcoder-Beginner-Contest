from collections import defaultdict

N, M = map(int, input().split())
pS = [input().split() for _ in range(M)]

correct = defaultdict(lambda: -1)
bad = defaultdict(int)
correct_num = 0
bad_num = 0
for i in range(M):
    if pS[i][1] == 'WA':
        bad[pS[i][0]] += 1
    else:
        if correct[pS[i][0]] == -1:
            correct[pS[i][0]] = 0
            bad_num += bad[pS[i][0]]
            correct_num += 1

print(len(correct), bad_num)