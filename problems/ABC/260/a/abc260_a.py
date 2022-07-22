#!/usr/bin/env python3
# from typing import *
from collections import Counter

# def solve(S: str) -> str:
def solve(S):
    S = list(S)
    c = Counter(S)
    for k, v in c.items():
        if v == 1:
            return k

    return -1

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    S = input()
    a = solve(S)
    print(a)


if __name__ == '__main__':
    main()
