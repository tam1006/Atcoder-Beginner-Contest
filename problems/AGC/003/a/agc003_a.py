from collections import Counter
S = list(input())

c = Counter(S)

if c['N'] > 0 or c['S'] > 0:
    if c['S']*c['N'] <= 0:
        print('No')
        exit()

if c['W'] > 0 or c['E'] > 0:
    if c['W']*c['E'] <= 0:
        print('No')
        exit()

print('Yes')
