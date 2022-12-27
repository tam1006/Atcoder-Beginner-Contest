#!/usr/bin/env python3
# from typing import *

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

def solve(N, M, A):
    edges = []
    for i in range(N):
        for j in range(i+1, N):
            cost = (pow(A[i], A[j], M) + pow(A[j], A[i], M)) % M
            edges.append((cost, i, j))

    edges.sort(reverse=True, key=lambda x: x[0])

    uf = UnionFind(N)
    ans = 0

    for i in range(len(edges)):
        cost, u, v = edges[i]
        if not uf.same(u, v):
            uf.union(u, v)
            ans += cost

    return ans

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    print(solve(N, M, A))

if __name__ == '__main__':
    main()
