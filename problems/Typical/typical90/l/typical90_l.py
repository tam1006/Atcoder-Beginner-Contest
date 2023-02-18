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

H, W = map(int, input().split())
Q = int(input())

uf = UnionFind(H*W)
field = [[0]*W for _ in range(H)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(Q):
    q = list(map(int, input().split()))

    if q[0] == 1:
        r, c = q[1], q[2]
        r -= 1
        c -= 1

        field[r][c] = 1

        for x, y in zip(dx, dy):
            nx = r + x
            ny = c + y

            if 0 <= nx < H and 0 <= ny < W and field[nx][ny] == 1:
                uf.union(r*W+c, nx*W+ny)

    else:
        ra, ca, rb, cb = q[1], q[2], q[3], q[4]
        ra -= 1
        ca -= 1
        rb -= 1
        cb -= 1

        if field[ra][ca] == 1 and field[rb][cb] == 1 and uf.same(ra*W+ca, rb*W+cb):
            print('Yes')
        else:
            print('No')
