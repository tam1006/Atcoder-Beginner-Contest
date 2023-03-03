# Range Add Query Segment Tree

from typing import TypeVar, Callable, List
T = TypeVar('T')

# l, r, xが与えられた時、[l, r)にxを足す O(logN)
# xが与えられた時、xの値を返す O(logN)
# 1-indexed
class RangeAddQuery:
    def __init__(self, data: List[T], N: int, N0: int):
        self.data = data
        self.N = N
        self.N0 = N0

    # 初期値を配列Aで初期化, 全てidentityの値からの実行
    @classmethod
    def from_list(cls, A: List[T]):
        N = len(A)
        N0 = 1 << (N - 1).bit_length()
        INF = (1 << 31) - 1

        data = [0] * (2 * N0)

        for i in range(N):
            data[N0 + i] = A[i]

        return cls(data, N, N0)

    # 長さNの配列を作成, 全てidentityの値で初期化
    @classmethod
    def new(cls, N: int, identity: T):
        N0 = 1 << (N - 1).bit_length()
        data = [0] * (2 * N0)

        for i in range(N):
            data[N0 + i] = identity

        return cls(data, N, N0)

    # i番目の値を返す O(logN)
    def get(self, i: int) -> int:
        assert 1 <= i <= self.N

        i += self.N0 - 1
        s = 0
        while i > 0:
            s += self.data[i]
            i = i >> 1

        return s

    # [l, r)にxを足す O(logN)
    def range_add(self, l: int, r: int, x: T):
        assert 1 <= l < r <= self.N + 1

        l += self.N0 - 1
        r += self.N0 - 1

        while l < r:
            if l & 1:
                self.data[l] += x
                l += 1
            if r & 1:
                r -= 1
                self.data[r] += x
            l = l >> 1
            r = r >> 1

# https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_E

N, Q = map(int, input().split())
RAQ = RangeAddQuery.new(N, 0)

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 0:
        s, t, x = q[1:]
        RAQ.range_add(s, t + 1, x)
    else:
        i = q[1]
        print(RAQ.get(i))
