#!/usr/bin/env python3
# from typing import *
from collections import defaultdict

# def solve(N: int, A: List[int], Q: int, B: List[int], C: List[int]) -> List[str]:
def solve(N, A, Q, B, C):
    d = defaultdict(int)
    for i in range(N):
        d[A[i]] += 1

    S = sum(A)
    ans = []
    for i in range(Q):
        S -= d[B[i]] * B[i]
        S += d[B[i]] * C[i]
        d[C[i]] += d[B[i]]
        d[B[i]] = 0
        ans.append(S)

    return ans




# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    A = [None for _ in range(N)]
    for i in range(N):
        A[i] = int(next(tokens))
    Q = int(next(tokens))
    B = [None for _ in range(Q)]
    C = [None for _ in range(Q)]
    for i in range(Q):
        B[i] = int(next(tokens))
        C[i] = int(next(tokens))
    assert next(tokens, None) is None
    S = solve(N, A, Q, B, C)
    for i in range(Q):
        print(S[i])


if __name__ == '__main__':
    main()