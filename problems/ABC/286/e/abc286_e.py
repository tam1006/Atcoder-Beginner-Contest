#!/usr/bin/env python3
# from typing import *

NO = 'Impossible'

# def solve(N: int, A: List[int], S: List[str], Q: int, U: List[int], V: List[int]) -> Any:
def solve(N, A, S, Q, U, V):
    d = [[[float('inf'), -float('inf')]] * N for _ in range(N)]

    for i in range(N):
        d[i][i] = [0, 0]
        for j in range(N):
            if S[i][j] == 'Y':
                d[i][j] = [1, A[j]]

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if d[i][j][0] > d[i][k][0] + d[k][j][0]:
                    d[i][j] = [d[i][k][0] + d[k][j][0], d[i][k][1] + d[k][j][1]]
                elif d[i][j][0] == d[i][k][0] + d[k][j][0]:
                    d[i][j][1] = max(d[i][j][1], d[i][k][1] + d[k][j][1])


    for u, v in zip(U, V):
        if d[u-1][v-1][0] == float('inf'):
            print(NO)
        else:
            print(d[u-1][v-1][0], d[u-1][v-1][1] + A[u-1])


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    A = [None for _ in range(N)]
    S = [None for _ in range(N)]
    for i in range(N):
        A[i] = int(next(tokens))
    for i in range(N):
        S[i] = next(tokens)
    Q = int(next(tokens))
    U = [None for _ in range(Q)]
    V = [None for _ in range(Q)]
    for i in range(Q):
        U[i] = int(next(tokens))
        V[i] = int(next(tokens))
    assert next(tokens, None) is None
    solve(N, A, S, Q, U, V)


if __name__ == '__main__':
    main()
