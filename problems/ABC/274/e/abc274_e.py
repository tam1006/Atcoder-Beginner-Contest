#!/usr/bin/env python3
# from typing import *
import sys
sys.setrecursionlimit(10**6)
from functools import lru_cache

# def solve(N: int, M: int, X: List[int], Y: List[int], P: List[int], Q: List[int]) -> float:
def solve():
    global dist, P, Q
    dist = [[0 for _ in range(M+N+1)] for _ in range(M+N+1)]

    P = P + [0]
    Q = Q + [0]

    for i in range(N+M+1):
        for j in range(N+M+1):
            if i < N and j < N:
                dist[i][j] = ((X[i]-X[j])**2 + (Y[i]-Y[j])**2)**0.5
            elif i < N and j >= N:
                dist[i][j] = ((X[i]-P[j-N])**2 + (Y[i]-Q[j-N])**2)**0.5
            elif i >= N and j < N:
                dist[i][j] = ((P[i-N]-X[j])**2 + (Q[i-N]-Y[j])**2)**0.5
            else:
                dist[i][j] = ((P[i-N]-P[j-N])**2 + (Q[i-N]-Q[j-N])**2)**0.5


    see = [False for _ in range(N+M+1)]
    global t
    t = 0
    see = '0'*(N+M+1)
    return dfs(N+M, see, 1, 0)

@lru_cache(maxsize=None)
def dfs(now, see, boost, count):
    global t
    if count == N+1:
        return t
    elif count == N:
        min_time = float('inf')
        for i in range(N, N+M+1):
            # if not see[i]:
            if see[i] == '0':
                if i == N+M:
                    # see[i] = True
                    see = see[:i] + '1' + see[i+1:]
                    t += dist[now][i] / boost
                    # min_time = min(min_time, dfs(i, see, boost, count+1, t+dist[now][i]/boost))
                    min_time = min(min_time, dfs(i, see, boost, count+1))
                    t -= dist[now][i] / boost
                    # see[i] = False
                    see = see[:i] + '0' + see[i+1:]
                else:
                    # see[i] = True
                    see = see[:i] + '1' + see[i+1:]
                    t += dist[now][i] / boost
                    # min_time = min(min_time, dfs(i, see, boost*2, count, t+dist[now][i]/boost))
                    min_time = min(min_time, dfs(i, see, boost*2, count))
                    t -= dist[now][i] / boost
                    # see[i] = False
                    see = see[:i] + '0' + see[i+1:]
        return min_time
    else:
        min_time = float('inf')
        for i in range(N+M):
            # if not see[i]:
            if see[i] == '0':
                # see[i] = True
                see = see[:i] + '1' + see[i+1:]
                if i < N:
                    t += dist[now][i] / boost
                    # min_time = min(min_time, dfs(i, see, boost, count+1, t+dist[now][i]/boost))
                    min_time = min(min_time, dfs(i, see, boost, count+1))
                    t -= dist[now][i] / boost
                else:
                    t += dist[now][i] / boost
                    # min_time = min(min_time, dfs(i, see, boost*2, count, t+dist[now][i]/boost))
                    min_time = min(min_time, dfs(i, see, boost*2, count))
                    t -= dist[now][i] / boost
                # see[i] = False
                see = see[:i] + '0' + see[i+1:]
        return min_time


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    global N, M, X, Y, P, Q
    N, M = map(int, input().split())
    X = [None for _ in range(N)]
    Y = [None for _ in range(N)]
    P = [None for _ in range(M)]
    Q = [None for _ in range(M)]
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    for i in range(M):
        P[i], Q[i] = map(int, input().split())
    # a = solve(N, M, X, Y, P, Q)
    a = solve()
    print(a)


if __name__ == '__main__':
    main()