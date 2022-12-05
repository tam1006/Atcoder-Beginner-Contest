#!/usr/bin/env python3
# from typing import *


# def solve(H: int, W: int, S: List[str]) -> int:
def solve(H, W, S):
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                ans += 1
    return ans


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    H, W = map(int, input().split())
    S = [None for _ in range(H)]
    for i in range(H):
        S[i] = input()
    a = solve(H, W, S)
    print(a)


if __name__ == '__main__':
    main()
