N = int(input())
st = input().split()
sxy = (int(st[0]), int(st[1]))
txy = (int(st[2]), int(st[3]))
xyr = list(tuple(map(int, input().split())) for _ in range(N))

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

uf = UnionFind(N)

for i in range(N):
    if ((xyr[i][0] - sxy[0])**2 + (xyr[i][1] - sxy[1])**2) == xyr[i][2]**2:
        s = i
    if ((xyr[i][0] - txy[0])**2 + (xyr[i][1] - txy[1])**2) == xyr[i][2]**2:
        t = i

    for j in range(N):
        if i == j:
            continue
        d2 = (xyr[i][0] - xyr[j][0])**2 + (xyr[i][1] - xyr[j][1])**2
        
        if (xyr[i][2] - xyr[j][2])**2 <= d2 <= (xyr[i][2] + xyr[j][2])**2:
            uf.union(i, j)

if uf.same(s, t):
    print('Yes')
else:
    print('No')