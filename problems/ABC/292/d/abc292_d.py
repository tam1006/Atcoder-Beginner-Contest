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

# def solve(N: int, M: int, u: List[int], v: List[int]) -> str:
def solve(N, M, u, v):
    edges = [[] for _ in range(N)]

    uf = UnionFind(N)
    for i in range(M):
        edges[u[i]-1].append(v[i]-1)
        edges[v[i]-1].append(u[i]-1)
        uf.union(u[i]-1, v[i]-1)

    visited = [False] * N

    for i in range(N):
        if visited[i]:
            continue

        members = uf.members(i)
        edge_count = 0
        for member in members:
            edge_count += len(edges[member])
            visited[member] = True

        edge_count //= 2
        if edge_count != len(members):
            return NO

    return YES





# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, M = map(int, input().split())
    u = [None for _ in range(M)]
    v = [None for _ in range(M)]
    for i in range(M):
        u[i], v[i] = map(int, input().split())
    a = solve(N, M, u, v)
    print(a)


if __name__ == '__main__':
    main()
