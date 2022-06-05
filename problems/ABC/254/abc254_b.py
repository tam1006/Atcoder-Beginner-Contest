N = int(input())

from operator import mul
from functools import reduce


def combinations_count(n, r):
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom

for i in range(N):
    for j in range(i+1):
        if j != i:
            print(combinations_count(i, j), end = ' ')
        else:
            print(combinations_count(i, j))
