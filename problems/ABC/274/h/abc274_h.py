#!/usr/bin/env python3
# from typing import *

YES = 'Yes'
NO = 'No'


# def solve(a: int, b: int, c: List[int], d: List[int], e: List[int], f: List[int], g: List[int], h: List[int], m: List[int]) -> List[str]:
def solve(a, b, c, d, e, f, g, h, m):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    a = int(next(tokens))
    b = int(next(tokens))
    c = [None for _ in range(a)]
    d = [None for _ in range(b)]
    e = [None for _ in range(b)]
    f = [None for _ in range(b)]
    g = [None for _ in range(b)]
    h = [None for _ in range(b)]
    m = [None for _ in range(b)]
    for i in range(a):
        c[i] = int(next(tokens))
    for i in range(b):
        d[i] = int(next(tokens))
        e[i] = int(next(tokens))
        f[i] = int(next(tokens))
        g[i] = int(next(tokens))
        h[i] = int(next(tokens))
        m[i] = int(next(tokens))
    assert next(tokens, None) is None
    n = solve(a, b, c, d, e, f, g, h, m)
    for i in range(b):
        print(n[i])


if __name__ == '__main__':
    main()
