N = int(input())

from collections import defaultdict

d = defaultdict(bool)
for i in range(N):
    s = input()
    if not d[s]:
        print(i+1)
        d[s] = True

