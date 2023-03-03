# Range Minimum Query Segment Tree

# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bf

from typing import TypeVar, Callable, List
T = TypeVar('T')

# s, tが与えられた時、[s, t)の最小値を求める O(logN)
# i, xが与えられた時、i番目の値をxに更新する O(logN)
# 1-indexed
class RangeMinimumQuery:
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

        data = [INF] * (2 * N0)
        for i in range(N):
            data[N0 + i] = A[i]

        for i in range(N0 - 1, 0, -1):
            data[i] = max(data[2 * i], data[2 * i + 1])

        return cls(data, INF, N, N0)

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
            self.data[i] = min(self.data[2 * i], self.data[2 * i + 1])

    # [l, r)の最小値を求める O(logN)
    def range_min(self, l: int, r: int) -> T:
        assert 1 <= l <= r <= self.N + 1

        l += self.N0 - 1
        r += self.N0 - 1

        s = self.identity
        while l < r:
            if l & 1:
                s = min(s, self.data[l])
                l += 1
            if r & 1:
                r -= 1
                s = min(s, self.data[r])
            l = l >> 1
            r = r >> 1

        return s

# https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_A

N, Q = map(int, input().split())
RMQ = RangeMinimumQuery.new(N, (1 << 31) - 1)

for _ in range(Q):
    c, x, y = map(int, input().split())
    if c == 0:
        RMQ.update(x+1, y)
    else:
        print(RMQ.range_min(x+1, y+2))
