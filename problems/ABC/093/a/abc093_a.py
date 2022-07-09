from collections import Counter
S = input()

c = Counter(S)

if c['a'] == 1 and c['b'] == 1 and c['c'] == 1:
    print('Yes')
else:
    print('No')