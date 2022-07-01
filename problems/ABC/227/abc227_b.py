N = int(input())
S = list(map(int, input().split()))

from collections import defaultdict
square = defaultdict(bool)

for a in range(1, 250):
    for b in range(1, 250):
        m = 4*a*b + 3*a + 3*b
        if m <= 1000:
            square[m] = True

ans = 0
for s in S:
    if not square[s]:
        ans += 1

print(ans)