# Range Maximum Query Segment Tree

# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bf

from typing import TypeVar, Callable, List
T = TypeVar('T')

# s, tが与えられた時、[s, t)の最大値を求める O(logN)
# i, xが与えられた時、i番目の値をxに更新する O(logN)
# 1-indexed
class RangeMaximumQuery:
    def __init__(self, data: List[T], identity: T, N: int, N0: int):
        self.data = data
        self.identity = identity
        self.N = N
        self.N0 = N0

    # 初期値を配列Aで初期化, 全てidentityの値からの実行
    @classmethod
    def from_list(cls, A: List[T]):
        N = len(A)
        N0 = 1 << (N - 1).bit_length()
        INF = (1 << 31) - 1

        data = [-INF] * (2 * N0)
        for i in range(N):
            data[N0 + i] = A[i]

        for i in range(N0 - 1, 0, -1):
            data[i] = max(data[2 * i], data[2 * i + 1])

        return cls(data, -INF, N, N0)

    # 長さNの配列を作成, 全てidentityの値で初期化
    @classmethod
    def new(cls, N: int, identity: T):
        N0 = 1 << (N - 1).bit_length()
        data = [identity] * (2 * N0)
        return cls(data, identity, N, N0)

    # i番目の値をxに更新する O(logN)
    def update(self, i: int, x: T):
        assert 1 <= i <= self.N

        i += self.N0 - 1
        self.data[i] = x
        while i > 0:
            i = i >> 1
            self.data[i] = max(self.data[2 * i], self.data[2 * i + 1])

    # [l, r)の最大値を求める O(logN)
    def range_max(self, l: int, r: int) -> T:
        assert 1 <= l <= r <= self.N + 1

        l += self.N0 - 1
        r += self.N0 - 1

        s = self.identity
        while l < r:
            if l & 1:
                s = max(s, self.data[l])
                l += 1
            if r & 1:
                r -= 1
                s = max(s, self.data[r])
            l = l >> 1
            r = r >> 1

        return s

    # i番目の値を返す O(1)
    def get(self, i: int) -> T:
        assert 1 <= i <= self.N

        return self.data[i + self.N0 - 1]


W, N = map(int, input().split())
L, R, V = [], [], []
for _ in range(N):
    l, r, v = map(int, input().split())
    L.append(l)
    R.append(r)
    V.append(v)

INF = pow(10, 9)
# 0, 1, 2, ..., W -> 1, 2, 3, ..., W+1
dp = RangeMaximumQuery.new(W + 1, -INF)
dp.update(1, 0)

for i in range(N):
    l, r, v = L[i], R[i], V[i]
    for w in range(l, W+2)[::-1]:
        max_value = dp.range_max(max(1, w - r), w - l + 1)
        if max_value >= 0 and dp.get(w) < max_value + v:
            dp.update(w, max_value + v)

ans = dp.get(W+1)
if ans == -INF:
    print(-1)
else:
    print(ans)
