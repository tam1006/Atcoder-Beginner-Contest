#!/usr/bin/env python3
# from typing import *

# def solve(S: str) -> int:
def solve(S):
    ans = 0
    for s in S:
        if s == 'v':
            ans += 1
        elif s == 'w':
            ans += 2

    return ans


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    S = input()
    a = solve(S)
    print(a)


if __name__ == '__main__':
    main()
