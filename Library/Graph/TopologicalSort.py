# トポロジカルソート
# 有向グラフの頂点をトポロジカル順に並べる
# 有向グラフの閉路探索にも使える

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


# https://atcoder.jp/contests/abc223/tasks/abc223_d

N, M = map(int, input().split())
ts = TopologicalSort(N)
for _ in range(M):
    A, B = map(int, input().split())
    ts.add_edge(A - 1, B - 1)

ok, res = ts.sort()
if not ok:
    print(-1)
else:
    print(*[x + 1 for x in res])
