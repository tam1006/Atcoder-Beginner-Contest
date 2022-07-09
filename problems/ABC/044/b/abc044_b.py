from collections import Counter

w = input()
c = Counter(w)

for key in c.keys():
    if c[key] % 2 != 0:
        print('No')
        exit()

print('Yes')
