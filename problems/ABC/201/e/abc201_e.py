#!/usr/bin/env python3
# from typing import *
import sys

sys.setrecursionlimit(10**7)
from functools import lru_cache

MOD = 1000000007


# def solve(N: int, u: List[int], v: List[int], w: List[int]) -> int:
def solve(N, u, v, w):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = int(input())
    u = [None for _ in range(N - 1)]
    v = [None for _ in range(N - 1)]
    w = [None for _ in range(N - 1)]
    for i in range(N - 1):
        u[i], v[i], w[i] = map(int, input().split())
    a = solve(N, u, v, w)
    print(a)


if __name__ == '__main__':
    main()