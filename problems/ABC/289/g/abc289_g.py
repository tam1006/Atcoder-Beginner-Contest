#!/usr/bin/env python3
# from typing import *
import sys

sys.setrecursionlimit(10**7)
from functools import lru_cache


# def solve(N: int, M: int, B: List[int], C: List[int]) -> List[str]:
def solve(N, M, B, C):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    M = int(next(tokens))
    B = [None for _ in range(N)]
    C = [None for _ in range(M)]
    for i in range(N):
        B[i] = int(next(tokens))
    for i in range(M):
        C[i] = int(next(tokens))
    assert next(tokens, None) is None
    ans = solve(N, M, B, C)
    print(*[ans[i] for i in range(M)])


if __name__ == '__main__':
    main()
