from collections import Counter
N = list(input())

c = Counter(N)

for key in c.keys():
    if c[key] >= 3:
        print('Yes')
        exit()

print('No')