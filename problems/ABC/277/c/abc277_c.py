#!/usr/bin/env python
# from typing import *


from collections import defaultdict
import copy
import sys

sys.setrecursionlimit(1000000)

# def solve(N: int, A: List[int], B: List[int]) -> int:
def solve(N, A, B):
    d = defaultdict(list)
    for i in range(N):
        d[A[i]].append(B[i])
        d[B[i]].append(A[i])

    global visited
    visited = defaultdict(bool)
    ans = dfs(1, d, 1)
    return ans


def dfs(x, d, val):
    global visited
    visited[x] = True
    # if not x in d.keys():
        # return val
    if len(d[x]) == 0:
        return val

    for y in d[x]:
        val = max(val, y)
        if not visited[y]:
            val = dfs(y, d, val)

    return val



# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = int(input())
    A = [None for _ in range(N)]
    B = [None for _ in range(N)]
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    a = solve(N, A, B)
    print(a)


if __name__ == '__main__':
    main()

