#!/usr/bin/env python3
# from typing import *

YES = 'Yes'
NO = 'No'


# def solve(N: int, A: List[int]) -> Tuple[str, str, List[str], str, List[str]]:
def solve(N, A):
    mod = [0] * 200

    x = -1
    y = -1
    if N <= 2**8:
        for i in range(2**N):
            tmp = 0
            for j in range(N):
                if i >> j & 1:
                    tmp += A[j]
                    tmp %= 200

            if mod[tmp] == 0:
                mod[tmp] = i
            else:
                x = mod[tmp]
                y = i
                break
    else:
        for i in range(2**8):
            tmp = 0
            for j in range(8):
                if i >> j & 1:
                    tmp += A[j]
                    tmp %= 200

            if mod[tmp] == 0:
                mod[tmp] = i
            else:
                x = mod[tmp]
                y = i
                break

    if x == -1:
        print('No')
    else:
        B = []
        C = []

        xx = x
        yy = y

        x = 0
        y = 0
        for i in range(8):
            if xx >> i & 1:
                B.append(i+1)
                x += 1
            if yy >> i & 1:
                C.append(i+1)
                y += 1

        print('Yes')
        print(x, *B)
        print(y, *C)

def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    A = [None for _ in range(N)]
    for i in range(N):
        A[i] = int(next(tokens))
    assert next(tokens, None) is None

    solve(N, A)


if __name__ == '__main__':
    main()
