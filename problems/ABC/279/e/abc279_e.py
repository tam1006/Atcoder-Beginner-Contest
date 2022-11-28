#!/usr/bin/env python3
# from typing import *


# def solve(N: int, M: int, A: List[int]) -> List[str]:
def solve(N, M, A):
    skip = []
    B = [i for i in range(1, N+1)]
    indexes = {}
    for i in range(1, N+1):
        indexes[i] = i

    for i in range(M):
        if B[A[i]-1] == 1:
            skip.append(B[A[i]])
        elif B[A[i]] == 1:
            skip.append(B[A[i]-1])
        else:
            skip.append(1)

        indexes[B[A[i]-1]] += 1
        indexes[B[A[i]]] -= 1
        B[A[i]-1], B[A[i]] = B[A[i]], B[A[i]-1]

    ans = []
    for i in range(M):
        ans.append(indexes[skip[i]])

    return ans





# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    M = int(next(tokens))
    A = [None for _ in range(M)]
    for i in range(M):
        A[i] = int(next(tokens))
    assert next(tokens, None) is None
    ans = solve(N, M, A)
    for i in range(M):
        print(ans[i])


if __name__ == '__main__':
    main()
