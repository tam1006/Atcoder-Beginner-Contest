#!/usr/bin/env python3
# from typing import *


# def solve(a: str) -> str:
def solve(a):
    if ord(a) < ord('a'):
        return 'A'
    else:
        return 'a'

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    a = input()
    a1 = solve(a)
    print(a1)


if __name__ == '__main__':
    main()