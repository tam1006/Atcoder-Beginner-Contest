N, M = map(int, input().split())

# SCC: 強連結成分分解
import sys
sys.setrecursionlimit(10 ** 9)

# 2回dfsを行うことで達成可能 O(|V| + |E|)
class StronglyConnectedComponent:
    def __init__(self, N):
        self.N = N
        self.G = [[] for _ in range(N)]
        self.rG = [[] for _ in range(N)]
        self.used = [False] * N
        self.vs = []
        # 頂点iが属する強連結成分のトポロジカル順序
        self.cmp = [-1] * N
        # 強連結成分のリスト
        self.scc_vs = []

    def add_edge(self, fr, to):
        assert 0 <= fr < self.N
        assert 0 <= to < self.N

        self.G[fr].append(to)
        self.rG[to].append(fr)

    def dfs(self, v):
        self.used[v] = True
        for to in self.G[v]:
            if not self.used[to]:
                self.dfs(to)
        self.vs.append(v)

    def rdfs(self, v, k):
        self.used[v] = True
        self.cmp[v] = k
        if len(self.scc_vs) <= k:
            self.scc_vs.append([])
        self.scc_vs[k].append(v)
        for to in self.rG[v]:
            if not self.used[to]:
                self.rdfs(to, k)

    def scc(self):
        self.used = [False] * self.N
        self.vs = []
        for v in range(self.N):
            if not self.used[v]:
                self.dfs(v)
        self.used = [False] * self.N
        k = 0
        for v in reversed(self.vs):
            if not self.used[v]:
                self.rdfs(v, k)
                k += 1
        return k, self.cmp, self.scc_vs


SCC = StronglyConnectedComponent(N)
for _ in range(M):
    a, b = map(int, input().split())
    SCC.add_edge(a-1, b-1)

k, cmp, scc_vs = SCC.scc()

ans = 0
for i in range(k):
    n = len(scc_vs[i])
    ans += n * (n - 1) // 2

print(ans)
