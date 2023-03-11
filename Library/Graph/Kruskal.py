# 最小全域木（クラスカル法）
# O(|E|log|V|)

from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

class Kruskal:
    def __init__(self, N: int):
        self.N = N
        self.edges = []

    # u: from, v: to
    def add_edge(self, u: int, v: int, cost: int):
        assert 0 <= u < self.N
        assert 0 <= v < self.N

        self.edges.append((cost, u, v))

    def min_cost(self):
        self.edges.sort(key=lambda x: x[0])

        uf = UnionFind(self.N)

        res = 0
        for cost, u, v in self.edges:
            if not uf.same(u, v):
                uf.union(u, v)
                res += cost

        return res



# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_12_A
N = int(input())
A = list(list(map(int, input().split())) for _ in range(N))

k = Kruskal(N)
for i in range(N):
    for j in range(N):
        if A[i][j] != -1:
            k.add_edge(i, j, A[i][j])

ans = k.min_cost()
print(ans)








