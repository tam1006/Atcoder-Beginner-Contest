#!/usr/bin/env python3
import sys

sys.setrecursionlimit(10**7)
input = lambda: sys.stdin.readline().rstrip()
from functools import lru_cache

import platform
if platform.python_implementation() == 'PyPy':
    import pypyjit
    pypyjit.set_param('max_unroll_recursion=-1')

YES = 'Yes'
NO = 'No'

import sys
sys.setrecursionlimit(10 ** 9)
from typing import Tuple
import heapq

# 0-indexed
class TopologicalSort:
    def __init__(self, N):
        self.N = N   # 頂点数
        self.G = [[] for _ in range(N)]  # 隣接リスト
        self.indeg = [0] * N   # 入次数

    def add_edge(self, fr, to):
        assert 0 <= fr < self.N
        assert 0 <= to < self.N

        self.G[fr].append(to)
        self.indeg[to] += 1

    def sort(self) -> Tuple[bool, list]:
        # 入次数が0の頂点をキューに入れる
        que = []
        for i in range(self.N):
            if self.indeg[i] == 0:
                heapq.heappush(que, i)

        if len(que) == 0:
            # DAGではない
            return False, []

        # トポロジカルソート
        res = []
        while que:
            if len(que) >= 2:
                return False, []

            v = heapq.heappop(que)
            res.append(v)
            for to in self.G[v]:
                self.indeg[to] -= 1
                if self.indeg[to] == 0:
                    heapq.heappush(que, to)

        if len(res) != self.N:
            # DAGではない
            return False, []
        else:
            return True, res

# def solve(N: int, M: int, X: List[int], Y: List[int]) -> Any:
def solve(N, M, X, Y):
    ts = TopologicalSort(N)

    for x, y in zip(X, Y):
        ts.add_edge(x - 1, y - 1)

    is_dag, order = ts.sort()

    if not is_dag:
        print(NO)

    else:
        ans = [0] * N
        for i in range(N):
            ans[order[i]] = i+1

        print(YES)
        print(*ans)





# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, M = map(int, input().split())
    X = [None for _ in range(M)]
    Y = [None for _ in range(M)]
    for i in range(M):
        X[i], Y[i] = map(int, input().split())

    solve(N, M, X, Y)


if __name__ == '__main__':
    main()